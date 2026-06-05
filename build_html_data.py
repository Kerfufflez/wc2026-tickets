#!/usr/bin/env python3
"""Build HTML/JS updates from JSON + optional DERIVE merges."""

from __future__ import annotations

import json
import re
from datetime import date, datetime
from pathlib import Path

from analyze_overlap import derive_pairs
from seatsidekick_utils import (
    BASE,
    BUCKET_LABELS,
    FILES,
    chart_buckets,
    deal_to_js,
    inv_to_js,
    load_json,
    metrics_for,
    row_to_deal,
    validate_all,
)

HTML_PATH = BASE / "World Cup Semi-Final Tickets.html"


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


def merge_derived_pairs(g2: list, g4: list) -> list:
    """Add G4-derived adjacent pairs to G2 when cheaper than the cheapest native G2."""
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


def cap_comment(filename: str) -> str:
    meta_path = BASE / "fetch_meta.json"
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


def format_top3(g2_deals: list, g4_deals: list) -> str:
    top = sorted(g2_deals + g4_deals, key=lambda d: d["avg"])[:3]
    items = ", ".join(deal_to_js(d) for d in top)
    return f"const cat{{cat}}top3 = [{items}].sort((a,b)=>a.avg-b.avg).slice(0,3);"


def build_category(cat_num: int, g2_file: str, g4_file: str) -> dict:
    g2_raw = load_json(BASE / g2_file)
    g4_raw = load_json(BASE / g4_file)
    g2_raw_count = len(g2_raw)
    g4_raw_count = len(g4_raw)
    g2_raw = merge_derived_pairs(g2_raw, g4_raw)

    g2_deals = [row_to_deal(r) for r in g2_raw]
    g4_deals = [row_to_deal(r) for r in g4_raw]
    g2_top = g2_deals[:10]
    g4_top = g4_deals[:10]
    top3 = sorted(g2_deals + g4_deals, key=lambda d: d["avg"])[:3]
    inv = sorted(
        build_inventory_from_deals(g2_deals, g4_deals),
        key=lambda b: -(b["g2c"] + b["g4c"]),
    )
    c2, c4, ymax, ystep = chart_buckets(cat_num, g2_raw, g4_raw)
    return {
        "cat": cat_num,
        "g2_file": g2_file,
        "g4_file": g4_file,
        "g2_count": len(g2_raw),
        "g4_count": len(g4_raw),
        "g2_api_count": g2_raw_count,
        "g4_api_count": g4_raw_count,
        "g2_top": g2_top,
        "g4_top": g4_top,
        "top3": top3,
        "inv": inv,
        "chart": (c2, c4, BUCKET_LABELS[cat_num], ymax, ystep),
        "metrics_g2": metrics_for(g2_raw, "Groups of 2 tickets"),
        "metrics_g4": metrics_for(g4_raw, "Groups of 4 tickets"),
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


def patch_html(categories: list[dict]) -> None:
    html = HTML_PATH.read_text(encoding="utf-8")
    now = datetime.now()
    today = now.strftime("%B %-d, %Y")
    last_updated = now.strftime("%B %-d, %Y at %-I:%M %p")
    html = re.sub(
        r"Data captured [^.<]+",
        f"Data captured {today}",
        html,
        count=1,
    )
    html = re.sub(
        r'(<p class="last-updated" id="last-updated">Last updated: <strong>)[^<]+(</strong></p>)',
        rf"\g<1>{last_updated}\g<2>",
        html,
        count=1,
    )

    cat_sections = {
        1: ("cat1", "id=\"cat1\""),
        2: ("cat2", "id=\"cat2\""),
        3: ("cat3", "id=\"cat3\""),
    }

    for data in categories:
        c = data["cat"]
        prefix = f"cat{c}"

        # Metrics in static HTML per category section
        section_marker = cat_sections[c][1]
        idx = html.find(f'<div {section_marker}')
        if idx == -1:
            raise RuntimeError(f"Section {c} not found")
        if c == 3:
            end = html.find('<div class="footer"', idx)
        else:
            end = html.find(f'<div id="cat{c + 1}"', idx + 10)
        section = html[idx:end]

        def replace_metric_block(section_html: str, label: str, m: dict, ticket_n: int) -> str:
            if label == "Groups of 2":
                end = r'(?=<div class="metrics-row-label">Groups of 4</div>)'
            else:
                end = r'(?=<div class="two-col">)'
            pattern = (
                rf'<div class="metrics-row-label">{re.escape(label)}</div>\s*'
                rf'<div class="metrics">[\s\S]*?</div>\s*'
                rf'{end}'
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
        html = html[:idx] + section + html[end:]

        # Script block replacements
        g2_comment = cap_comment(data["g2_file"])
        g4_comment = cap_comment(data["g4_file"])

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
        c2, c4, labels, ymax, ystep = data["chart"]
        labels_str = "[" + ", ".join(f"'{lb}'" for lb in labels) + "]"
        chart_new = (
            f"makeChart('{prefix}-chart',{c2},{c4},\n  "
            f"{labels_str},{ymax},{ystep});"
        )
        html = re.sub(g2_pat, lambda _m: g2_new, html, count=1)
        html = re.sub(g4_pat, lambda _m: g4_new, html, count=1)
        html = re.sub(top3_pat, lambda _m: top3_new, html, count=1)
        html = re.sub(inv_pat, lambda _m: inv_new, html, count=1)
        html = re.sub(chart_pat, lambda _m: chart_new, html, count=1)

    HTML_PATH.write_text(html, encoding="utf-8")
    print(f"Updated {HTML_PATH}")


def main() -> int:
    errors = validate_all()
    if errors:
        for e in errors:
            print(e)
        return 1
    categories = []
    for cat_label, g2_file, g4_file in FILES:
        cat_num = int(cat_label.replace("cat", ""))
        categories.append(build_category(cat_num, g2_file, g4_file))
    patch_html(categories)
    for d in categories:
        print(
            f"Cat {d['cat']}: G2={d['g2_count']} G4={d['g4_count']} "
            f"chart peak G2={max(d['chart'][0])} G4={max(d['chart'][1])}"
        )
    from deal_tracker import log_deals
    from publish_docs import publish_docs

    log_deals()
    publish_docs()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
