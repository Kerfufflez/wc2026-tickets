"""Build HTML/JS updates from JSON + optional DERIVE merges."""

from __future__ import annotations

import json
import re

from wc2026.config import (
    ROOT,
    TEMPLATE,
    game_fetch_meta,
    game_raw_path,
    game_report_html,
)
from wc2026.dates import format_est, format_est_date, now_est
from wc2026.derive import derive_pairs
from wc2026.games import (
    _DEFAULT_MARKET_RANGE,
    _STAGE_MARKET_RANGE,
    game_categories,
    game_config_js,
    format_game_date,
)
from wc2026.utils import (
    chart_buckets,
    deal_to_js,
    inv_to_js,
    load_json,
    market_avg,
    market_deal,
    metrics_for,
    row_to_deal,
    validate_all,
)


def derived_to_row(pair: dict) -> dict:
    parent = pair["parent"]
    avg = pair["avg"]
    return {
        "block": pair["block"],
        "row": pair["row"],
        "area": parent["area"],
        "group_size": 2,
        "first_seat": pair["first_seat"],
        "last_seat": pair["last_seat"],
        "seat_numbers": f"{pair['first_seat']},{pair['last_seat']}",
        "min_price": avg,
        "max_price": avg,
        "avg_price": float(avg),
        "total_price": float(pair["total"]),
        "dominant_category": parent["dominant_category"],
        "dominant_bucket": parent["dominant_bucket"],
        "_derived": True,
    }


def _top_deals(deals: list[dict], n: int) -> list[dict]:
    seen: set[tuple] = set()
    picked: list[dict] = []
    for d in sorted(deals, key=lambda x: x["avg"]):
        key = (d["sec"], d["row"], d["gs"], d.get("derived", False))
        if key in seen:
            continue
        seen.add(key)
        picked.append(d)
        if len(picked) >= n:
            break
    return picked


def merge_derived_pairs(g2: list, g4: list) -> list:
    if not g2:
        return g2
    lookup = {
        (str(r["block"]), str(r["row"]), int(r["first_seat"]), int(r["last_seat"]))
        for r in g2
    }
    min_g2_avg = min(round(r["avg_price"]) for r in g2)
    merged = list(g2)
    added = 0
    for pair in derive_pairs(g4):
        key = (pair["block"], pair["row"], pair["first_seat"], pair["last_seat"])
        if key in lookup:
            continue
        if pair["avg"] >= min_g2_avg:
            continue
        merged.append(derived_to_row(pair))
        lookup.add(key)
        added += 1
    if added:
        merged.sort(key=lambda r: r["total_price"])
    return merged


def cap_comment(pid: str, filename: str) -> str:
    meta_path = game_fetch_meta(pid)
    if not meta_path.exists():
        return ""
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    info = meta.get(filename, {})
    if info.get("truncated"):
        total = info.get("total", "?")
        return (
            f"// Partial fetch for {filename} ({info.get('count')}/{total} groups); "
            "more inventory may exist\n"
        )
    return ""


def format_array(name: str, deals: list[dict], prefix_comment: str = "") -> str:
    lines = [prefix_comment + f"const {name} = ["]
    for d in deals:
        lines.append(f"  {deal_to_js(d)},")
    lines.append("];")
    return "\n".join(lines)


def build_category(
    cat_num: int,
    pid: str,
    g2_file: str,
    g4_file: str,
    market_range: dict[int, tuple[int, int]],
    bucket_ranges: dict[int, list[int]] | None = None,
) -> dict:
    g2_raw = load_json(game_raw_path(pid, g2_file))
    g4_raw = load_json(game_raw_path(pid, g4_file))
    g2_raw_count = len(g2_raw)
    g4_raw_count = len(g4_raw)
    g2_native = [r for r in g2_raw if market_avg(round(r["avg_price"]), cat_num, market_range)]
    g4_native = [r for r in g4_raw if market_avg(round(r["avg_price"]), cat_num, market_range)]
    g2_merged = merge_derived_pairs(g2_native, g4_native)

    g2_deals = [
        d for d in (row_to_deal(r, cat_num) for r in g2_merged)
        if market_deal(d, cat_num, market_range)
    ]
    g4_deals = [
        d for d in (row_to_deal(r, cat_num) for r in g4_native)
        if market_deal(d, cat_num, market_range)
    ]
    g2_top = sorted(g2_deals, key=lambda d: d["avg"])[:10]
    g4_top = sorted(g4_deals, key=lambda d: d["avg"])[:10]
    top3 = _top_deals(g2_deals + g4_deals, 3)
    inv = sorted(
        build_inventory_from_deals(g2_deals, g4_deals),
        key=lambda b: -(b["g2c"] + b["g4c"]),
    )

    br = bucket_ranges or {}
    c2, c4, ymax, ystep = chart_buckets(cat_num, g2_merged, g4_native, br)
    return {
        "cat": cat_num,
        "g2_file": g2_file,
        "g4_file": g4_file,
        "g2_count": len(g2_merged),
        "g4_count": len(g4_native),
        "g2_api_count": g2_raw_count,
        "g4_api_count": g4_raw_count,
        "g2_top": g2_top,
        "g4_top": g4_top,
        "top3": top3,
        "inv": inv,
        "chart": (c2, c4, ymax, ystep),
        "metrics_g2": metrics_for(g2_merged, "Groups of 2 tickets", cat_num, market_range),
        "metrics_g4": metrics_for(g4_native, "Groups of 4 tickets", cat_num, market_range),
    }


def build_inventory_from_deals(g2: list, g4: list) -> list:
    blocks: dict = {}
    for deals, cnt_key, min_key in ((g2, "g2c", "g2m"), (g4, "g4c", "g4m")):
        for d in deals:
            sec = d["sec"]
            if sec not in blocks:
                blocks[sec] = {
                    "sec": sec,
                    "stand": d["stand"],
                    "side": d["side"],
                    "g2c": 0,
                    "g2m": None,
                    "g4c": 0,
                    "g4m": None,
                }
            b = blocks[sec]
            b[cnt_key] += 1
            if b[min_key] is None or d["avg"] < b[min_key]:
                b[min_key] = d["avg"]
    return list(blocks.values())


def _collect_built_games(current_pid: str, current_match: dict) -> list[dict]:
    """Return all games with a built reports dashboard, always including current."""
    try:
        from wc2026.games import load_matches
        all_matches = load_matches()
    except FileNotFoundError:
        return [current_match]

    pid_to_match = {str(m["pid"]): m for m in all_matches}
    result = []
    reports_dir = ROOT / "reports"
    if reports_dir.exists():
        for pid_dir in sorted(reports_dir.iterdir()):
            if pid_dir.is_dir() and (pid_dir / "dashboard.html").exists():
                m = pid_to_match.get(pid_dir.name)
                if m:
                    result.append(m)
    if current_pid not in {str(m["pid"]) for m in result}:
        result.append(current_match)
    result.sort(key=lambda m: m.get("date", ""))
    return result


def patch_html(
    pid: str,
    match: dict,
    categories: list[tuple[int, str, str]],
    category_data: list[dict],
    bucket_ranges: dict[int, list[int]],
    bucket_labels: dict[int, list[str]],
    built_games: list[dict] | None = None,
) -> None:
    source = TEMPLATE if TEMPLATE.exists() else game_report_html(pid)
    html = source.read_text(encoding="utf-8")
    now = now_est()
    today = format_est_date(now)
    last_updated = format_est(now)

    # Inject game identity
    matchup = match.get("matchup", "")
    venue_date = f"{match.get('venue', '')} · {format_game_date(match)}"
    html = re.sub(r"\{\{game_title\}\}", matchup, html)
    html = re.sub(r"\{\{game_subtitle\}\}", venue_date, html)

    html = re.sub(
        r"Data captured [^.<]+",
        f"Data captured {today}",
        html,
        count=1,
    )
    html = re.sub(
        r'(<p class="last-updated" id="last-updated"[^>]*>Last updated: <strong>)[^<]+(</strong></p>)',
        rf"\g<1>{last_updated}\g<2>",
        html,
        count=1,
    )

    # Inject game config script (replaces placeholder or appends before </head>)
    config_script = game_config_js(match, built_games)
    if "<!-- __GAME_CONFIG__ -->" in html:
        html = html.replace("<!-- __GAME_CONFIG__ -->", config_script)
    else:
        html = html.replace("</head>", f"  {config_script}\n</head>", 1)

    # Patch each category section
    cat_nums = {cat_num for cat_num, _, _ in categories}
    for data in category_data:
        c = data["cat"]
        prefix = f"cat{c}"

        # Show/hide the section based on whether this game has the category
        # (cat4 is hidden in template by default; remove 'hidden' if present)
        if c in cat_nums:
            html = re.sub(
                rf'(<div id="{prefix}"[^>]*) hidden([^>]*>)',
                rf'\1\2',
                html,
                count=1,
            )

        # Find section bounds
        section_start = html.find(f'<div id="{prefix}"')
        if section_start == -1:
            continue
        if c == max(cat_nums):
            section_end = html.find('<div class="footer"', section_start)
        else:
            next_cat = c + 1
            section_end = html.find(f'<div id="cat{next_cat}"', section_start + 10)
        section = html[section_start:section_end]

        def replace_metric_block(section_html: str, label: str, m: dict, ticket_n: int) -> str:
            if label == "Groups of 2":
                end_pat = r"(?=<div class=\"metrics-row-label\">Groups of 4</div>)"
            else:
                end_pat = r"(?=<div class=\"two-col\">)"
            pattern = (
                rf'<div class="metrics-row-label">{re.escape(label)}</div>\s*'
                rf'<div class="metrics">[\s\S]*?</div>\s*'
                rf"{end_pat}"
            )
            close_grid = (
                "\n    </div>\n    " if label == "Groups of 4" else "\n      "
            )
            block = (
                f'<div class="metrics-row-label">{label}</div>\n'
                f'      <div class="metrics">\n'
                f'        <div class="metric"><div class="metric-label">Listings</div>'
                f'<div class="metric-value">{m["listings"]}</div>'
                f'<div class="metric-sub">{m["ticket_label"]}</div></div>\n'
                f'        <div class="metric"><div class="metric-label">Cheapest avg/ticket</div>'
                f'<div class="metric-value">{m["cheapest_value"]}</div>'
                f'<div class="metric-sub">{m["cheapest_sub"]}</div></div>\n'
                f'        <div class="metric"><div class="metric-label">Median avg/ticket</div>'
                f'<div class="metric-value">{m["median_value"]}</div>'
                f'<div class="metric-sub">{m["median_sub"]}</div></div>\n'
                f'        <div class="metric"><div class="metric-label">Min total ({ticket_n} tickets)</div>'
                f'<div class="metric-value">{m["min_total_value"]}</div>'
                f'<div class="metric-sub">{m["min_total_sub"]}</div></div>\n'
                f'      </div>{close_grid}'
            )
            return re.sub(pattern, block, section_html, count=1)

        section = replace_metric_block(section, "Groups of 2", data["metrics_g2"], 2)
        section = replace_metric_block(section, "Groups of 4", data["metrics_g4"], 4)
        html = html[:section_start] + section + html[section_end:]

        g2_comment = cap_comment(pid, data["g2_file"])
        g4_comment = cap_comment(pid, data["g4_file"])

        labels = bucket_labels.get(c, [])
        labels_str = "[" + ", ".join(f"'{lb}'" for lb in labels) + "]"

        g2_pat = (
            rf"(?:// (?:API returned 100 results \(limit\)|Partial fetch) for [^\n]+\n)*"
            rf"const {prefix}g2 = \[[\s\S]*?\];"
        )
        g4_pat = rf"const {prefix}g4 = \[[\s\S]*?\];"
        top3_pat = rf"const {prefix}top3 = [^;]+;"
        inv_pat = rf"const {prefix}inv = \[[\s\S]*?\];"
        chart_pat = (
            rf"makeChart\('{prefix}-chart',[^\n]+,\n[^\n]+,\n[^\n]+,\d+,\d+\);"
        )

        g2_new = format_array(f"{prefix}g2", data["g2_top"], g2_comment)
        g4_new = format_array(f"{prefix}g4", data["g4_top"], g4_comment)
        top3_new = (
            f"const {prefix}top3 = [{', '.join(deal_to_js(d) for d in data['top3'])}]"
            f".sort((a,b)=>a.avg-b.avg).slice(0,3);"
        )
        inv_new = (
            f"const {prefix}inv = [\n  "
            + ",\n  ".join(inv_to_js(b) for b in data["inv"])
            + ",\n];"
        )
        c2, c4_data, ymax, ystep = data["chart"]
        chart_new = (
            f"makeChart('{prefix}-chart',{c2},{c4_data},\n  "
            f"{labels_str},{ymax},{ystep});"
        )
        html = re.sub(g2_pat, lambda _m: g2_new, html, count=1)
        html = re.sub(g4_pat, lambda _m: g4_new, html, count=1)
        html = re.sub(top3_pat, lambda _m: top3_new, html, count=1)
        html = re.sub(inv_pat, lambda _m: inv_new, html, count=1)
        html = re.sub(chart_pat, lambda _m: chart_new, html, count=1)

    out = game_report_html(pid)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"Updated {out}")


def main(match: dict) -> int:
    from wc2026.games import (
        _STAGE_BUCKETS,
        _DEFAULT_BUCKETS,
        _STAGE_MARKET_RANGE,
        _DEFAULT_MARKET_RANGE,
        _bucket_labels,
    )
    from wc2026.render_deal_log import render_deal_log
    from wc2026.tracker import log_deals
    from wc2026.publish import publish_docs

    pid = str(match["pid"])
    stage = match.get("stage", "Semi-final")
    cats = game_categories(match)

    market_range = _STAGE_MARKET_RANGE.get(stage, _DEFAULT_MARKET_RANGE)
    bucket_preset = _STAGE_BUCKETS.get(stage, _DEFAULT_BUCKETS)

    bucket_ranges: dict[int, list[int]] = {}
    bucket_labels: dict[int, list[str]] = {}
    for cat_num, _, _ in cats:
        bp = bucket_preset.get(cat_num, [500, 1000, 2000, 4000, 8000])
        bucket_ranges[cat_num] = bp
        bucket_labels[cat_num] = _bucket_labels(bp)

    errors = validate_all(pid, cats)
    if errors:
        for e in errors:
            print(e)
        return 1

    category_data = []
    for cat_num, g2_file, g4_file in cats:
        category_data.append(
            build_category(cat_num, pid, g2_file, g4_file, market_range, bucket_ranges)
        )

    built_games = _collect_built_games(pid, match)
    patch_html(pid, match, cats, category_data, bucket_ranges, bucket_labels, built_games)

    for d in category_data:
        print(
            f"Cat {d['cat']}: G2={d['g2_count']} G4={d['g4_count']} "
            f"chart peak G2={max(d['chart'][0])} G4={max(d['chart'][1])}"
        )

    log_deals(pid)
    render_deal_log(pid)
    publish_docs(pid, match)
    return 0


if __name__ == "__main__":
    raise SystemExit("Use: python3 -m wc2026 build --game <pid>")
