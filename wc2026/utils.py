"""Shared transforms, validation, and chart helpers for SeatSidekick data."""

from __future__ import annotations

import json
import math
import statistics
from pathlib import Path
from typing import Any

from wc2026.config import CATEGORIES, DATA_RAW, raw_path

BUCKET_RANGES = {
    1: [4500, 5000, 5500, 6000, 6500],
    2: [3000, 3500, 4000, 4500, 5000],
    3: [2500, 3000, 3500, 4000, 5000],
}

BUCKET_LABELS = {
    1: ["<$4.5k", "$4.5–5k", "$5–5.5k", "$5.5–6k", "$6–6.5k", "$6.5k+"],
    2: ["<$3k", "$3–3.5k", "$3.5–4k", "$4–4.5k", "$4.5–5k", "$5k+"],
    3: ["<$2.5k", "$2.5–3k", "$3–3.5k", "$3.5–4k", "$4–5k", "$5k+"],
}


def load_json(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_side(area: str) -> str:
    if "Right" in area:
        return "Right"
    if "Left" in area:
        return "Left"
    if "Opposite" in area:
        return "Opposite"
    return "Center"


def parse_stand(area: str) -> str:
    return "Opposite" if "Opposite" in area else "Main"


def format_seats(seat_numbers: str) -> str:
    seats = [s.strip() for s in seat_numbers.split(",")]
    if len(seats) <= 2:
        return "–".join(seats)
    return f"{seats[0]}–{seats[-1]}"


def row_to_deal(row: dict[str, Any]) -> dict[str, Any]:
    row_num = int(row["row"])
    return {
        "sec": str(row["block"]),
        "row": row_num,
        "seats": format_seats(row["seat_numbers"]),
        "stand": parse_stand(row["area"]),
        "side": parse_side(row["area"]),
        "total": round(row["total_price"]),
        "avg": round(row["avg_price"]),
        "gs": row["group_size"],
        "front": row_num < 20,
        "mixed": row["min_price"] != row["max_price"],
        "derived": bool(row.get("_derived")),
    }


def g2_key(row: dict[str, Any]) -> tuple:
    return (str(row["block"]), str(row["row"]), int(row["first_seat"]), int(row["last_seat"]))


def validate_all() -> list[str]:
    errors: list[str] = []
    loaded: dict[str, tuple[list, list]] = {}

    for cat, g2_file, g4_file in CATEGORIES:
        for fname in (g2_file, g4_file):
            path = raw_path(fname)
            if not path.exists():
                errors.append(f"Missing file: {fname}")
                continue
            try:
                data = load_json(path)
            except json.JSONDecodeError as e:
                errors.append(f"{fname}: invalid JSON — {e}")
                continue
            if not isinstance(data, list) or len(data) == 0:
                errors.append(f"{fname}: empty or not an array")
                continue
            for row in data:
                if row.get("avg_price") in (None, 0):
                    errors.append(
                        f"{fname}: invalid avg_price on {row.get('group_id', '?')}"
                    )
                try:
                    int(row["row"])
                except (KeyError, TypeError, ValueError):
                    errors.append(
                        f"{fname}: invalid row on {row.get('group_id', '?')}"
                    )
                if row.get("block") is None:
                    errors.append(
                        f"{fname}: missing block on {row.get('group_id', '?')}"
                    )

        g2_path, g4_path = raw_path(g2_file), raw_path(g4_file)
        if g2_path.exists() and g4_path.exists():
            g2 = load_json(g2_path)
            g4 = load_json(g4_path)
            loaded[cat] = (g2, g4)
            if len(g2) < 1:
                errors.append(f"{cat}: no G2 results")
            if len(g4) < 1:
                errors.append(f"{cat}: no G4 results")
            deals = [row_to_deal(r) for r in g2 + g4]
            if len(deals) < 3:
                errors.append(
                    f"{cat}: combined pool has {len(deals)} items, need 3 for top3"
                )

    return errors


def bucket_index(cat_num: int, avg: int) -> int:
    bounds = BUCKET_RANGES[cat_num]
    if avg < bounds[0]:
        return 0
    for i, bound in enumerate(bounds[1:], start=1):
        if avg < bound:
            return i
    return len(bounds)


def chart_buckets(cat_num: int, g2: list[dict], g4: list[dict]) -> tuple[list[int], list[int], int, int]:
    c2 = [0] * 6
    c4 = [0] * 6
    for row in g2:
        c2[bucket_index(cat_num, round(row["avg_price"]))] += 1
    for row in g4:
        c4[bucket_index(cat_num, round(row["avg_price"]))] += 1
    peak = max(c2 + c4) if (c2 or c4) else 0
    ymax = max(5, math.ceil((peak * 1.15) / 5) * 5) if peak else 5
    ystep = max(1, round(ymax / 5))
    return c2, c4, ymax, ystep


def median_rounded(values: list[float]) -> int:
    return round(statistics.median(values))


def build_inventory(g2: list[dict], g4: list[dict]) -> list[dict]:
    blocks: dict[str, dict] = {}
    for rows, cnt_key, min_key in (
        (g2, "g2c", "g2m"),
        (g4, "g4c", "g4m"),
    ):
        for row in rows:
            sec = str(row["block"])
            if sec not in blocks:
                deal = row_to_deal(row)
                blocks[sec] = {
                    "sec": sec,
                    "stand": deal["stand"],
                    "side": deal["side"],
                    "g2c": 0,
                    "g2m": None,
                    "g4c": 0,
                    "g4m": None,
                }
            b = blocks[sec]
            b[cnt_key] += 1
            avg = round(row["avg_price"])
            if b[min_key] is None or avg < b[min_key]:
                b[min_key] = avg
    return list(blocks.values())


def metrics_for(rows: list[dict], ticket_label: str) -> dict[str, str]:
    avgs = [r["avg_price"] for r in rows]
    cheapest = min(rows, key=lambda r: r["avg_price"])
    min_total_row = min(rows, key=lambda r: r["total_price"])
    n = len(rows)
    return {
        "listings": str(n),
        "cheapest_value": f"${round(cheapest['avg_price']):,}",
        "cheapest_sub": f"Section {cheapest['block']} · Row {cheapest['row']}",
        "median_value": f"${median_rounded(avgs):,}",
        "median_sub": f"Across {n} groups",
        "min_total_value": f"${round(min_total_row['total_price']):,}",
        "min_total_sub": f"Section {min_total_row['block']}, Row {min_total_row['row']}",
        "ticket_label": ticket_label,
    }


def deal_to_js(d: dict) -> str:
    parts = [
        f"sec:'{d['sec']}'",
        f"row:{d['row']}",
        f"seats:'{d['seats']}'",
        f"stand:'{d['stand']}'",
        f"side:'{d['side']}'",
        f"total:{d['total']}",
        f"avg:{d['avg']}",
        f"gs:{d['gs']}",
        f"front:{str(d['front']).lower()}",
        f"mixed:{str(d['mixed']).lower()}",
        f"derived:{str(d.get('derived', False)).lower()}",
    ]
    return "{" + ",".join(parts) + "}"


def inv_to_js(b: dict) -> str:
    g2m = "null" if b["g2m"] is None else str(b["g2m"])
    g4m = "null" if b["g4m"] is None else str(b["g4m"])
    return (
        f"{{sec:'{b['sec']}',stand:'{b['stand']}',side:'{b['side']}',"
        f"g2c:{b['g2c']},g2m:{g2m},g4c:{b['g4c']},g4m:{g4m}}}"
    )
