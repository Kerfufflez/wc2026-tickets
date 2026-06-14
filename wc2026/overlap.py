"""G4 pair derivation overlap analysis -> reports/{pid}/overlap_analysis.md"""

from __future__ import annotations

from datetime import date

from wc2026.config import game_overlap, game_raw_path
from wc2026.derive import derive_pairs
from wc2026.utils import g2_key, load_json


def classify_pair(pair: dict, g2_lookup: set, g2_min: float, g2_max: float) -> str:
    key = (pair["block"], pair["row"], pair["first_seat"], pair["last_seat"])
    if key in g2_lookup:
        return "DUPLICATE"
    if g2_min <= pair["total"] <= g2_max:
        return "IN_RANGE"
    return "NEW"


def verdict(overlap_pct: float, new_count: int, in_range_count: int) -> str:
    if overlap_pct >= 80:
        return "SKIP"
    if new_count >= 5:
        return "DERIVE"
    if new_count < 5 and in_range_count >= 10:
        return "INVESTIGATE"
    return "SKIP"


def recommendation_text(v: str) -> str:
    return {
        "SKIP": "G2 API already surfaces pairs; derivation adds little.",
        "DERIVE": "Add only NEW pairs below G2 min total to G2 list.",
        "INVESTIGATE": "Many IN_RANGE pairs; consider paginated G2 fetch before adding.",
    }[v]


def cheapest_in(bucket: str, classified: list[tuple[str, dict]]) -> str | None:
    items = [p for b, p in classified if b == bucket]
    if not items:
        return None
    c = min(items, key=lambda x: x["avg"])
    return (
        f"Sec {c['block']} Row {c['row']} Seats {c['seat_str']}  "
        f"avg ${c['avg']:,}/ea  total ${c['total']:,}"
    )


def analyze_category(cat_num: int, g2: list, g4: list) -> dict:
    lookup = {g2_key(r) for r in g2}
    g2_totals = [r["total_price"] for r in g2]
    g2_min, g2_max = min(g2_totals), max(g2_totals)

    derived = derive_pairs(g4)
    classified = []
    counts = {"DUPLICATE": 0, "IN_RANGE": 0, "NEW": 0}
    for p in derived:
        b = classify_pair(p, lookup, g2_min, g2_max)
        counts[b] += 1
        classified.append((b, p))

    total = len(derived) or 1
    overlap_rate = counts["DUPLICATE"] / total * 100
    v = verdict(overlap_rate, counts["NEW"], counts["IN_RANGE"])

    new_below_min = [
        p for b, p in classified if b == "NEW" and p["total"] < g2_min
    ]

    return {
        "cat_num": cat_num,
        "g2_count": len(g2),
        "g4_count": len(g4),
        "derived_count": len(derived),
        "g2_min_total": round(g2_min),
        "g2_max_total": round(g2_max),
        "counts": counts,
        "overlap_rate": overlap_rate,
        "verdict": v,
        "classified": classified,
        "new_below_min": new_below_min,
        "g2_min": g2_min,
    }


def format_section(r: dict) -> str:
    c = r["counts"]
    total = r["derived_count"] or 1
    cat_name = f"Category {r['cat_num']}"
    lines = [
        f"## {cat_name} — Pair Derivation Analysis",
        f"Date: {date.today().strftime('%B %-d, %Y')}",
        "",
        f"G2 fetched: {r['g2_count']} groups, price range "
        f"${r['g2_min_total']:,} – ${r['g2_max_total']:,} total",
        f"G4 fetched: {r['g4_count']} groups → {r['derived_count']} derived adjacent pairs",
        "",
        "| Bucket     | Count | % of derived | Notes                          |",
        "|------------|-------|--------------|--------------------------------|",
    ]
    notes = {
        "DUPLICATE": "Already in G2 response",
        "IN_RANGE": "May exist in G2, not top-100",
        "NEW": "Genuinely new options",
    }
    for bucket in ("DUPLICATE", "IN_RANGE", "NEW"):
        n = c[bucket]
        pct = n / total * 100
        lines.append(
            f"| {bucket:<10} | {n:>5} | {pct:>10.1f}% | {notes[bucket]:<30} |"
        )
    lines.extend(
        [
            "",
            f"Overlap rate: {r['overlap_rate']:.1f}% (DUPLICATE / total)",
            f"Verdict: **{r['verdict']}** — {recommendation_text(r['verdict'])}",
            "",
        ]
    )
    for bucket in ("DUPLICATE", "IN_RANGE", "NEW"):
        line = cheapest_in(bucket, r["classified"])
        label = bucket.replace("_", " ").title()
        lines.append(f"Cheapest {label}: {line or '—'}")
    if r["verdict"] == "DERIVE":
        lines.append(
            f"\nPairs eligible for merge (NEW below G2 min ${r['g2_min_total']:,}): "
            f"{len(r['new_below_min'])}"
        )
    lines.append("")
    return "\n".join(lines)


def overall_recommendation(results: list[dict]) -> str:
    verdicts = [r["verdict"] for r in results]
    if all(v == "SKIP" for v in verdicts):
        return "SKIP"
    if any(v == "DERIVE" for v in verdicts):
        if all(v in ("SKIP", "DERIVE") for v in verdicts):
            return "PARTIAL"
        return "DERIVE"
    if any(v == "INVESTIGATE" for v in verdicts):
        return "PARTIAL"
    return "SKIP"


def main(pid: str, categories: list[tuple[int, dict[int, str]]]) -> int:
    results = []
    for cat_num, gs_files in categories:
        g2_path = game_raw_path(pid, gs_files[2])
        g4_path = game_raw_path(pid, gs_files[4])
        if not g2_path.exists() or not g4_path.exists():
            continue
        g2 = load_json(g2_path)
        g4 = load_json(g4_path)
        if not g2 or not g4:
            continue
        results.append(analyze_category(cat_num, g2, g4))

    if not results:
        print("No G2+G4 data available for overlap analysis — skipping")
        return 0

    sections = [format_section(r) for r in results]
    summary_rows = [
        "## Summary Recommendation",
        "",
        "| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |",
        "|----------|-------------|-----------|----------------|-----------------|",
    ]
    for r in results:
        c = r["counts"]
        summary_rows.append(
            f"| Cat {r['cat_num']}    | {r['overlap_rate']:>9.1f}% | "
            f"{c['NEW']:>9} | {c['IN_RANGE']:>14} | {r['verdict']:<15} |"
        )
    overall = overall_recommendation(results)
    summary_rows.extend(
        [
            "",
            f"Overall recommendation: **{overall}**",
            "",
        ]
    )

    out = game_overlap(pid)
    out.parent.mkdir(parents=True, exist_ok=True)
    body = "\n".join(sections) + "\n" + "\n".join(summary_rows) + "\n"
    out.write_text(body, encoding="utf-8")
    print(f"Wrote {out}")
    for r in results:
        print(
            f"  Cat {r['cat_num']}: overlap {r['overlap_rate']:.1f}%, "
            f"verdict {r['verdict']}, NEW below min: {len(r['new_below_min'])}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit("Use: python3 -m wc2026 overlap --game <pid>")
