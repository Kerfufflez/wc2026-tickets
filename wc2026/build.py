"""Build HTML/JS updates from JSON + optional DERIVE merges."""

from __future__ import annotations

import json
import re

from wc2026.config import (
    ROOT,
    REFRESH_JS,
    TEMPLATE,
    game_raw_path,
    game_report_html,
)
from wc2026.dates import format_est, format_est_date, now_est
from wc2026.derive import derive_pairs
from wc2026.games import (
    _DEFAULT_BUCKETS,
    _DEFAULT_MARKET_RANGE,
    _STAGE_BUCKETS,
    _STAGE_MARKET_RANGE,
    game_categories,
    game_config_js,
    format_game_date,
)
from wc2026.utils import (
    chart_buckets_single,
    load_json,
    market_avg,
    market_deal,
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


def build_gs_category(
    cat_num: int,
    pid: str,
    fname: str,
    gs: int,
    g4_raw: list,
    market_range: dict[int, tuple[int, int]],
    bucket_ranges: dict[int, list[int]] | None = None,
) -> dict:
    """Build deals + chart for one (category, group_size) combination."""
    path = game_raw_path(pid, fname)
    raw = load_json(path) if path.exists() else []

    filtered = [r for r in raw if market_avg(round(r["avg_price"]), cat_num, market_range)]

    if gs == 2:
        g4_filtered = [r for r in g4_raw if market_avg(round(r["avg_price"]), cat_num, market_range)]
        filtered = merge_derived_pairs(filtered, g4_filtered)

    deals = [
        d for d in (row_to_deal(r, cat_num) for r in filtered)
        if market_deal(d, cat_num, market_range)
    ]
    deals_sorted = sorted(deals, key=lambda d: d["avg"])[:10]

    br = bucket_ranges or {}
    if cat_num in br:
        c, ymax, ystep = chart_buckets_single(cat_num, filtered, br)
    else:
        c, ymax, ystep = [0] * 6, 5, 1

    return {
        "cat": cat_num,
        "gs": gs,
        "count": len(deals),
        "deals": deals_sorted,
        "chart": {"c": c, "ymax": ymax, "ystep": ystep},
    }


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
    data_obj: dict,
    built_games: list[dict] | None = None,
) -> None:
    source = TEMPLATE if TEMPLATE.exists() else game_report_html(pid)
    html = source.read_text(encoding="utf-8")
    now = now_est()
    today = format_est_date(now)
    last_updated = format_est(now)

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

    config_script = game_config_js(match, built_games)
    if "<!-- __GAME_CONFIG__ -->" in html:
        html = html.replace("<!-- __GAME_CONFIG__ -->", config_script)
    else:
        html = html.replace("</head>", f"  {config_script}\n</head>", 1)

    data_json = json.dumps(data_obj, separators=(',', ':'))
    data_script = f"<script>window.__wc2026Data={data_json};</script>"
    if "<!-- __GAME_DATA__ -->" in html:
        html = html.replace("<!-- __GAME_DATA__ -->", data_script)
    else:
        html = html.replace("</body>", f"  {data_script}\n</body>", 1)

    out = game_report_html(pid)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    if REFRESH_JS.exists():
        import shutil
        shutil.copy2(REFRESH_JS, out.parent / "refresh.js")
    print(f"Updated {out}")


def main(match: dict) -> int:
    from wc2026.render_deal_log import render_deal_log
    from wc2026.tracker import log_deals
    from wc2026.publish import publish_docs

    pid = str(match["pid"])
    stage = match.get("stage", "Semi-final")
    cats = game_categories(match)

    market_range = _STAGE_MARKET_RANGE.get(stage, _DEFAULT_MARKET_RANGE)
    bucket_preset = _STAGE_BUCKETS.get(stage, _DEFAULT_BUCKETS)

    bucket_ranges: dict[int, list[int]] = {}
    for cat_num, _ in cats:
        bucket_ranges[cat_num] = bucket_preset.get(cat_num, [500, 1000, 2000, 4000, 8000])

    errors = validate_all(pid, cats)
    if errors:
        for e in errors:
            print(e)
        return 1

    # Cache G4 raw rows (needed for G2 derive/merge)
    g4_raw_cache: dict[int, list] = {}
    for cat_num, gs_files in cats:
        g4_path = game_raw_path(pid, gs_files[4])
        g4_raw_cache[cat_num] = load_json(g4_path) if g4_path.exists() else []

    # Build per-gs, per-cat data
    gs_cats: dict[int, dict[int, dict]] = {gs: {} for gs in (1, 2, 3, 4)}
    for gs in (1, 2, 3, 4):
        for cat_num, gs_files in cats:
            gs_cats[gs][cat_num] = build_gs_category(
                cat_num, pid, gs_files[gs], gs,
                g4_raw_cache[cat_num],
                market_range, bucket_ranges,
            )

    # Require at least some data to build
    has_any = any(
        gs_cats[gs][cat_num]["count"] > 0
        for gs in (1, 2, 3, 4)
        for cat_num, _ in cats
    )
    if not has_any:
        print("No usable listings across any category/group size — skipping build")
        return 1

    # Assemble window.__wc2026Data
    data_obj: dict = {"top3": {}, "cats": {}}
    for cat_num, _ in cats:
        data_obj["cats"][str(cat_num)] = {}
        for gs in (1, 2, 3, 4):
            gd = gs_cats[gs][cat_num]
            data_obj["cats"][str(cat_num)][str(gs)] = {
                "deals": gd["deals"],
                "chart": gd["chart"],
            }

    for gs in (1, 2, 3, 4):
        all_deals: list[dict] = []
        for cat_num, _ in cats:
            all_deals.extend(gs_cats[gs][cat_num]["deals"])
        data_obj["top3"][str(gs)] = _top_deals(all_deals, 3)

    built_games = _collect_built_games(pid, match)
    patch_html(pid, match, data_obj, built_games)

    for cat_num, _ in cats:
        counts = " ".join(f"G{gs}={gs_cats[gs][cat_num]['count']}" for gs in (1, 2, 3, 4))
        print(f"  Cat {cat_num}: {counts}")

    log_deals(pid)
    render_deal_log(pid)
    publish_docs(pid, match)
    return 0


if __name__ == "__main__":
    raise SystemExit("Use: python3 -m wc2026 build --game <pid>")
