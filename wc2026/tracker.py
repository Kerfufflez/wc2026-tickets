"""Snapshot inventory and append per-refresh changelog entries."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from wc2026.build import build_category, merge_derived_pairs
from wc2026.config import CATEGORIES, REPORT_DEAL_LOG_JSON, REPORT_SNAPSHOTS, raw_path
from wc2026.dates import (
    format_est,
    iso_est,
    now_est,
    parse_captured_at,
    snapshot_id,
)
from wc2026.utils import load_json, row_to_deal


def deal_id(row: dict[str, Any]) -> str:
    if row.get("_derived"):
        return (
            f"derived:{row['block']}:{row['row']}:"
            f"{row['first_seat']}-{row['last_seat']}"
        )
    return str(row.get("group_id", ""))


def listing_record(row: dict[str, Any]) -> dict[str, Any]:
    d = row_to_deal(row)
    return {
        "id": deal_id(row),
        "sec": d["sec"],
        "row": d["row"],
        "seats": d["seats"],
        "stand": d["stand"],
        "side": d["side"],
        "avg": d["avg"],
        "total": d["total"],
        "gs": d["gs"],
        "derived": d["derived"],
        "front": d["front"],
        "mixed": d["mixed"],
    }


def fmt_deal(d: dict[str, Any]) -> str:
    tag = " [from 4-pack]" if d.get("derived") else ""
    front = " [front]" if d.get("front") else ""
    return (
        f"Sec {d['sec']} Row {d['row']} Seats {d['seats']} "
        f"({d['gs']}t) — ${d['avg']:,}/ea (${d['total']:,} total){tag}{front}"
    )


def fmt_delta(old: int, new: int) -> str:
    diff = new - old
    if diff > 0:
        return f"+${diff:,}"
    if diff < 0:
        return f"−${abs(diff):,}"
    return "unchanged"


def _signed(n: int) -> str:
    if n > 0:
        return f"+{n}"
    if n < 0:
        return str(n)
    return "±0"


def build_snapshot() -> dict[str, Any]:
    now = now_est()
    sid = snapshot_id(now)
    categories: dict[str, Any] = {}
    for cat_label, g2_file, g4_file in CATEGORIES:
        cat_num = int(cat_label.replace("cat", ""))
        g2_raw = load_json(raw_path(g2_file))
        g4_raw = load_json(raw_path(g4_file))
        g2_merged = merge_derived_pairs(g2_raw, g4_raw)
        built = build_category(cat_num, g2_file, g4_file)

        listings: dict[str, dict] = {}
        for row in g2_merged + g4_raw:
            listings[deal_id(row)] = listing_record(row)

        categories[f"cat{cat_num}"] = {
            "counts": {"g2": built["g2_count"], "g4": built["g4_count"]},
            "cheapest_g2": built["g2_top"][0] if built["g2_top"] else None,
            "cheapest_g4": built["g4_top"][0] if built["g4_top"] else None,
            "top3": built["top3"],
            "top10_g2": built["g2_top"],
            "top10_g4": built["g4_top"],
            "listings": listings,
        }

    return {
        "id": sid,
        "captured_at": iso_est(now),
        "captured_label": format_est(now),
        "date": now.date().isoformat(),
        "categories": categories,
    }


def load_snapshot(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if "id" not in data:
        data["id"] = path.stem
    return data


def list_snapshot_files() -> list[Path]:
    if not REPORT_SNAPSHOTS.exists():
        return []
    files = list(REPORT_SNAPSHOTS.glob("*.json"))
    return sorted(files, key=_snapshot_sort_key, reverse=True)


def _snapshot_sort_key(path: Path) -> str:
    try:
        data = load_snapshot(path)
        return data.get("captured_at", path.stem)
    except (json.JSONDecodeError, OSError):
        return path.stem


def previous_snapshot(exclude_id: str) -> tuple[dict[str, Any] | None, str | None]:
    for path in list_snapshot_files():
        if path.stem == exclude_id:
            continue
        return load_snapshot(path), path.stem
    return None, None


def compare_listings(
    prev: dict[str, dict], curr: dict[str, dict]
) -> dict[str, list]:
    prev_ids = set(prev)
    curr_ids = set(curr)
    new_ids = curr_ids - prev_ids
    gone_ids = prev_ids - curr_ids

    price_drops = []
    price_rises = []
    for lid in prev_ids & curr_ids:
        p, c = prev[lid], curr[lid]
        if c["avg"] < p["avg"]:
            price_drops.append((p, c))
        elif c["avg"] > p["avg"]:
            price_rises.append((p, c))

    price_drops.sort(key=lambda x: x[0]["avg"] - x[1]["avg"], reverse=True)
    price_rises.sort(key=lambda x: x[1]["avg"] - x[0]["avg"], reverse=True)
    new_list = sorted((curr[i] for i in new_ids), key=lambda d: d["avg"])
    gone_list = sorted((prev[i] for i in gone_ids), key=lambda d: d["avg"])

    return {
        "new": new_list,
        "gone": gone_list,
        "drops": price_drops,
        "rises": price_rises,
    }


def _deal_key(d: dict) -> str:
    return f"{d['sec']}:{d['row']}:{d['seats']}:{d['gs']}"


def _deal_brief(d: dict[str, Any], cat: str, change: str | None = None) -> dict:
    out = {
        "cat": cat,
        "sec": d["sec"],
        "row": d["row"],
        "seats": d["seats"],
        "gs": d["gs"],
        "avg": d["avg"],
        "total": d["total"],
        "front": d.get("front", False),
        "derived": d.get("derived", False),
        "text": fmt_deal(d),
    }
    if change:
        out["change"] = change
    return out


def build_log_entry(
    snapshot: dict[str, Any],
    prev: dict[str, Any] | None,
    prev_id: str | None,
) -> dict[str, Any]:
    summary: dict[str, dict] = {}
    price_drops: list[dict] = []
    front_section: list[dict] = []
    detail_lines: list[str] = []
    preview_stats: dict[str, int] = {"price_drops": 0, "front_section": 0}

    if prev is None:
        detail_lines.append("First scan — baseline inventory saved.")
        for cat_key in ("cat1", "cat2", "cat3"):
            cat = snapshot["categories"][cat_key]
            cat_num = cat_key.replace("cat", "")
            summary[cat_key] = {
                "g2_delta": 0,
                "g4_delta": 0,
                "new_g2": 0,
                "new_g4": 0,
            }
            detail_lines.append(
                f"Cat {cat_num}: {cat['counts']['g2']} G2 / {cat['counts']['g4']} G4 listings"
            )
            if cat["cheapest_g2"]:
                detail_lines.append(f"  Cheapest G2: {fmt_deal(cat['cheapest_g2'])}")
            if cat["cheapest_g4"]:
                detail_lines.append(f"  Cheapest G4: {fmt_deal(cat['cheapest_g4'])}")
            for d in cat.get("top3", []):
                if d.get("front"):
                    front_section.append(_deal_brief(d, cat_key, "baseline"))
            preview_stats["front_section"] = len(front_section)
        detail_lines.append("")
    else:
        prev_label = prev.get("captured_label") or prev_id or "prior scan"
        detail_lines.append(f"Compared to {prev_label}")
        detail_lines.append("")

        for cat_key in ("cat1", "cat2", "cat3"):
            cat_num = cat_key.replace("cat", "")
            pcat = prev["categories"][cat_key]
            ccat = snapshot["categories"][cat_key]
            diff = compare_listings(pcat["listings"], ccat["listings"])
            g2_delta = ccat["counts"]["g2"] - pcat["counts"]["g2"]
            g4_delta = ccat["counts"]["g4"] - pcat["counts"]["g4"]
            new_g2 = len([d for d in diff["new"] if d["gs"] == 2])
            new_g4 = len([d for d in diff["new"] if d["gs"] == 4])

            summary[cat_key] = {
                "g2_delta": g2_delta,
                "g4_delta": g4_delta,
                "new_g2": new_g2,
                "new_g4": new_g4,
            }

            detail_lines.append(
                f"Cat {cat_num}: G2 {_signed(g2_delta)} ({new_g2} new) · "
                f"G4 {_signed(g4_delta)} ({new_g4} new)"
            )

            for p, c in diff["drops"]:
                if p["avg"] - c["avg"] < 1:
                    continue
                change = f"{fmt_delta(p['avg'], c['avg'])}/ea"
                drop = _deal_brief(c, cat_key, change)
                price_drops.append(drop)
                detail_lines.append(f"  Price drop: {fmt_deal(c)} — was ${p['avg']:,}/ea ({change})")

            for d in diff["new"]:
                if d.get("front"):
                    front_section.append(_deal_brief(d, cat_key, "new"))
                    detail_lines.append(f"  New front row: {fmt_deal(d)}")

            for p, c in diff["drops"]:
                if c.get("front") and c["avg"] < p["avg"]:
                    key = _deal_key(c)
                    if not any(_deal_key(x) == key for x in front_section):
                        front_section.append(_deal_brief(c, cat_key, fmt_delta(p["avg"], c["avg"]) + "/ea"))
                        detail_lines.append(
                            f"  Front row drop: {fmt_deal(c)} — was ${p['avg']:,}/ea"
                        )

            if diff["gone"]:
                detail_lines.append(f"  Removed {len(diff['gone'])} listings")
                for d in diff["gone"][:5]:
                    detail_lines.append(f"    {fmt_deal(d)}")
                if len(diff["gone"]) > 5:
                    detail_lines.append(f"    …and {len(diff['gone']) - 5} more")

            if not any([diff["new"], diff["drops"], diff["gone"], g2_delta, g4_delta]):
                detail_lines.append("  No material changes")

            detail_lines.append("")

        preview_stats["price_drops"] = len(price_drops)
        preview_stats["front_section"] = len(front_section)

    preview_lines = _build_preview_lines(summary, preview_stats)

    return {
        "id": snapshot["id"],
        "captured_at": snapshot["captured_at"],
        "captured_label": snapshot["captured_label"],
        "prev_id": prev_id,
        "summary": summary,
        "preview_lines": preview_lines,
        "preview_stats": preview_stats,
        "price_drops": price_drops,
        "front_section": front_section,
        "detail_lines": detail_lines,
        "is_baseline": prev is None,
    }


def _build_preview_lines(summary: dict, stats: dict) -> list[str]:
    cat_parts = []
    for cat_key in ("cat1", "cat2", "cat3"):
        s = summary.get(cat_key, {})
        num = cat_key.replace("cat", "")
        cat_parts.append(
            f"Cat {num} G2 {_signed(s.get('g2_delta', 0))} · G4 {_signed(s.get('g4_delta', 0))}"
        )
    stat_parts = []
    if stats.get("price_drops"):
        n = stats["price_drops"]
        stat_parts.append(f"{n} price drop{'s' if n != 1 else ''}")
    if stats.get("front_section"):
        n = stats["front_section"]
        stat_parts.append(f"{n} front-section")
    lines = [" · ".join(cat_parts)]
    if stat_parts:
        lines.append(" · ".join(stat_parts))
    elif not any(
        s.get("g2_delta") or s.get("g4_delta")
        for s in summary.values()
    ):
        lines.append("No changes vs last scan")
    return lines


def load_deal_log_entries() -> list[dict]:
    if not REPORT_DEAL_LOG_JSON.exists():
        return []
    data = json.loads(REPORT_DEAL_LOG_JSON.read_text(encoding="utf-8"))
    return data.get("entries", [])


def append_deal_log_entry(entry: dict) -> None:
    REPORT_DEAL_LOG_JSON.parent.mkdir(parents=True, exist_ok=True)
    entries = load_deal_log_entries()
    entries = [e for e in entries if e.get("id") != entry["id"]]
    entries.insert(0, entry)
    REPORT_DEAL_LOG_JSON.write_text(
        json.dumps({"entries": entries}, indent=2) + "\n",
        encoding="utf-8",
    )


def log_deals() -> Path:
    snapshot = build_snapshot()
    sid = snapshot["id"]
    prev, prev_id = previous_snapshot(exclude_id=sid)

    REPORT_SNAPSHOTS.mkdir(parents=True, exist_ok=True)
    snap_path = REPORT_SNAPSHOTS / f"{sid}.json"
    snap_path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")

    entry = build_log_entry(snapshot, prev, prev_id)
    append_deal_log_entry(entry)

    print(f"Snapshot saved: {snap_path}")
    print(f"Deal log entry: {REPORT_DEAL_LOG_JSON} ({entry['captured_label']})")
    if prev_id:
        print(f"Compared against: {prev_id}")
    else:
        print("Baseline snapshot (no prior scan to compare)")
    return REPORT_DEAL_LOG_JSON


def snapshot_dates_manifest() -> list[dict]:
    """Latest capture per calendar day for dropdown labels."""
    by_date: dict[str, dict] = {}
    for path in list_snapshot_files():
        try:
            data = load_snapshot(path)
            day = data.get("date") or path.stem[:10]
            captured = data.get("captured_at", "")
            if day not in by_date or captured > by_date[day].get("captured_at", ""):
                dt = parse_captured_at(captured) if captured else now_est()
                from wc2026.dates import format_dropdown_label

                by_date[day] = {
                    "date": day,
                    "captured_at": captured,
                    "label": format_dropdown_label(dt),
                }
        except (json.JSONDecodeError, ValueError, OSError):
            continue
    return sorted(by_date.values(), key=lambda x: x["date"], reverse=True)


def main() -> int:
    log_deals()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
