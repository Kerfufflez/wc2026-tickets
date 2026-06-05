"""G4 adjacent-pair derivation for G2 merge and overlap analysis."""

from __future__ import annotations


def derive_pairs(g4_rows: list[dict]) -> list[dict]:
    pairs = []
    for row in g4_rows:
        seats = [int(s.strip()) for s in row["seat_numbers"].split(",")]
        if len(seats) < 2:
            continue
        avg = round(row["avg_price"])
        block, r = str(row["block"]), str(row["row"])
        for i in range(len(seats) - 1):
            pairs.append(
                {
                    "block": block,
                    "row": r,
                    "first_seat": seats[i],
                    "last_seat": seats[i + 1],
                    "avg": avg,
                    "total": avg * 2,
                    "seat_str": f"{seats[i]}–{seats[i + 1]}",
                    "parent": row,
                }
            )
    return pairs
