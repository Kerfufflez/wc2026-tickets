"""Snapshot best deals and compare day-over-day price movements."""

from __future__ import annotations

import json
import re
from datetime import date, datetime
from pathlib import Path
from typing import Any

from wc2026.build import build_category, merge_derived_pairs
from wc2026.config import CATEGORIES, REPORT_DEAL_LOG, REPORT_SNAPSHOTS, raw_path
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
    return (
        f"Sec {d['sec']} Row {d['row']} Seats {d['seats']} "
        f"({d['gs']}t) — ${d['avg']:,}/ea (${d['total']:,} total){tag}"
    )


def fmt_delta(old: int, new: int) -> str:
    diff = new - old
    if diff > 0:
        return f"+${diff:,}"
    if diff < 0:
        return f"−${abs(diff):,}"
    return "unchanged"


def build_snapshot() -> dict[str, Any]:
    today = date.today().isoformat()
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
        "captured_at": datetime.now().isoformat(timespec="seconds"),
        "date": today,
        "categories": categories,
    }


def load_snapshot(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def previous_snapshot(exclude_date: str) -> tuple[dict[str, Any] | None, str | None]:
    if not REPORT_SNAPSHOTS.exists():
        return None, None
    files = sorted(REPORT_SNAPSHOTS.glob("*.json"), reverse=True)
    for f in files:
        if f.stem != exclude_date:
            return load_snapshot(f), f.stem
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

    price_drops.sort(key=lambda x: x[1]["avg"] - x[0]["avg"])
    price_rises.sort(key=lambda x: x[1]["avg"] - x[0]["avg"], reverse=True)
    new_list = sorted((curr[i] for i in new_ids), key=lambda d: d["avg"])
    gone_list = sorted((prev[i] for i in gone_ids), key=lambda d: d["avg"])

    return {
        "new": new_list,
        "gone": gone_list,
        "drops": price_drops,
        "rises": price_rises,
    }


def top10_changes(prev_top: list, curr_top: list) -> dict[str, list]:
    prev_ids = {d.get("id") or _deal_key(d) for d in prev_top}
    entered = []
    for d in curr_top:
        key = d.get("id") or _deal_key(d)
        if key not in prev_ids:
            entered.append(d)
    return {"entered_top10": entered}


def _deal_key(d: dict) -> str:
    return f"{d['sec']}:{d['row']}:{d['seats']}:{d['gs']}"


def format_run_report(
    snapshot: dict[str, Any],
    prev: dict[str, Any] | None,
    prev_date: str | None,
) -> str:
    lines = [
        f"## {snapshot['date']}",
        f"*Captured {snapshot['captured_at']}*",
        "",
    ]
    if prev is None:
        lines.extend(
            [
                "First snapshot — baseline saved. Re-run tomorrow to see day-over-day changes.",
                "",
            ]
        )
        for cat_key in ("cat1", "cat2", "cat3"):
            cat = snapshot["categories"][cat_key]
            lines.append(f"### {cat_key.upper()} — baseline")
            lines.append(
                f"- Inventory: {cat['counts']['g2']} G2 / {cat['counts']['g4']} G4"
            )
            if cat["cheapest_g2"]:
                lines.append(f"- Cheapest G2: {fmt_deal(cat['cheapest_g2'])}")
            if cat["cheapest_g4"]:
                lines.append(f"- Cheapest G4: {fmt_deal(cat['cheapest_g4'])}")
            lines.append("- Top 3:")
            for i, d in enumerate(cat["top3"], 1):
                lines.append(f"  {i}. {fmt_deal(d)}")
            lines.append("")
        return "\n".join(lines)

    lines.append(f"Compared to **{prev_date}**")
    lines.append("")

    for cat_key in ("cat1", "cat2", "cat3"):
        pcat = prev["categories"][cat_key]
        ccat = snapshot["categories"][cat_key]
        diff = compare_listings(pcat["listings"], ccat["listings"])
        g2_delta = ccat["counts"]["g2"] - pcat["counts"]["g2"]
        g4_delta = ccat["counts"]["g4"] - pcat["counts"]["g4"]

        lines.append(f"### {cat_key.upper()}")
        lines.append(
            f"- Inventory: {ccat['counts']['g2']} G2 ({_signed(g2_delta)}), "
            f"{ccat['counts']['g4']} G4 ({_signed(g4_delta)})"
        )

        for label, key in (("G2", "cheapest_g2"), ("G4", "cheapest_g4")):
            old, new = pcat.get(key), ccat.get(key)
            if old and new:
                if _deal_key(old) != _deal_key(new):
                    lines.append(
                        f"- Cheapest {label} changed: {fmt_deal(old)} → **{fmt_deal(new)}**"
                    )
                elif new["avg"] != old["avg"]:
                    lines.append(
                        f"- Cheapest {label} price: ${old['avg']:,} → **${new['avg']:,}** "
                        f"({fmt_delta(old['avg'], new['avg'])}/ea)"
                    )

        if diff["new"]:
            lines.append(f"- **New listings** ({len(diff['new'])} total, cheapest first):")
            for d in diff["new"][:10]:
                lines.append(f"  - {fmt_deal(d)}")
            if len(diff["new"]) > 10:
                lines.append(f"  - …and {len(diff['new']) - 10} more")

        for pool, label in (("top10_g2", "G2 top 10"), ("top10_g4", "G4 top 10")):
            entered = top10_changes(pcat[pool], ccat[pool])["entered_top10"]
            if entered:
                lines.append(f"- **Entered {label}:**")
                for d in entered:
                    lines.append(f"  - {fmt_deal(d)}")

        notable_drops = [(p, c) for p, c in diff["drops"] if p["avg"] - c["avg"] >= 50]
        if notable_drops:
            lines.append(f"- **Price drops** (≥$50/ea):")
            for p, c in notable_drops[:8]:
                lines.append(
                    f"  - {fmt_deal(c)} — was ${p['avg']:,}/ea ({fmt_delta(p['avg'], c['avg'])}/ea)"
                )

        notable_rises = [(p, c) for p, c in diff["rises"] if c["avg"] - p["avg"] >= 50]
        if notable_rises:
            lines.append(f"- **Price rises** (≥$50/ea):")
            for p, c in notable_rises[:5]:
                lines.append(
                    f"  - {fmt_deal(c)} — was ${p['avg']:,}/ea ({fmt_delta(p['avg'], c['avg'])}/ea)"
                )

        if diff["gone"]:
            lines.append(f"- **Removed** ({len(diff['gone'])} listings no longer available):")
            for d in diff["gone"][:5]:
                lines.append(f"  - {fmt_deal(d)}")
            if len(diff["gone"]) > 5:
                lines.append(f"  - …and {len(diff['gone']) - 5} more")

        if not any(
            [
                diff["new"],
                diff["drops"],
                diff["rises"],
                diff["gone"],
                g2_delta,
                g4_delta,
            ]
        ):
            lines.append("- No material changes vs prior snapshot.")

        lines.append("")

    return "\n".join(lines)


def _signed(n: int) -> str:
    if n > 0:
        return f"+{n}"
    if n < 0:
        return str(n)
    return "±0"


def update_deal_log(report: str, run_date: str) -> None:
    REPORT_DEAL_LOG.parent.mkdir(parents=True, exist_ok=True)
    REPORT_SNAPSHOTS.mkdir(parents=True, exist_ok=True)

    header = "# Deal movement log\n\nTrack price changes between manual dashboard refreshes.\n\n"
    if REPORT_DEAL_LOG.exists():
        body = REPORT_DEAL_LOG.read_text(encoding="utf-8")
        if not body.startswith("# Deal movement log"):
            body = header + body
        pattern = rf"## {re.escape(run_date)}\b[\s\S]*?(?=\n## |\Z)"
        if re.search(pattern, body):
            body = re.sub(pattern, report.strip() + "\n\n", body, count=1)
        else:
            body = body.rstrip() + "\n\n" + report.strip() + "\n"
    else:
        body = header + report.strip() + "\n"

    REPORT_DEAL_LOG.write_text(body, encoding="utf-8")


def log_deals() -> Path:
    snapshot = build_snapshot()
    run_date = snapshot["date"]
    prev, prev_date = previous_snapshot(exclude_date=run_date)

    REPORT_SNAPSHOTS.mkdir(parents=True, exist_ok=True)
    snap_path = REPORT_SNAPSHOTS / f"{run_date}.json"
    snap_path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")

    report = format_run_report(snapshot, prev, prev_date)
    update_deal_log(report, run_date)

    print(f"Snapshot saved: {snap_path}")
    print(f"Deal log updated: {REPORT_DEAL_LOG}")
    if prev_date:
        print(f"Compared against: {prev_date}")
    else:
        print("Baseline snapshot (no prior run to compare)")
    return REPORT_DEAL_LOG


def main() -> int:
    log_deals()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
