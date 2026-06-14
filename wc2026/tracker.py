"""Snapshot inventory and append per-refresh changelog entries."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from wc2026.config import (
    game_deal_log_json,
    game_deal_log_md,
    game_snapshots,
)
from wc2026.dates import (
    _HAS_OFFSET,
    format_est,
    iso_est,
    now_est,
    parse_captured_at,
    snapshot_id,
)

TIMESTAMPED_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{6}$")


def deal_id(row: dict[str, Any]) -> str:
    if row.get("_derived"):
        return (
            f"derived:{row['block']}:{row['row']}:"
            f"{row['first_seat']}-{row['last_seat']}"
        )
    return str(row.get("group_id", ""))


def listing_record(row: dict[str, Any], cat_num: int) -> dict[str, Any]:
    from wc2026.utils import row_to_deal
    d = row_to_deal(row, cat_num)
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


def is_timestamped_stem(stem: str) -> bool:
    return bool(TIMESTAMPED_RE.match(stem))


def is_legacy_daily_stem(stem: str) -> bool:
    return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", stem))


def build_snapshot(pid: str) -> dict[str, Any]:
    from wc2026.build import build_category, merge_derived_pairs
    from wc2026.config import game_raw_path
    from wc2026.games import game_categories, get_game
    from wc2026.utils import load_json, market_deal, row_to_deal

    match = get_game(pid)
    categories = game_categories(match)

    from wc2026.games import (
        _STAGE_MARKET_RANGE, _DEFAULT_MARKET_RANGE,
        _STAGE_BUCKETS, _DEFAULT_BUCKETS,
    )
    stage = match.get("stage", "Semi-final")
    market_range = _STAGE_MARKET_RANGE.get(stage, _DEFAULT_MARKET_RANGE)
    bucket_preset = _STAGE_BUCKETS.get(stage, _DEFAULT_BUCKETS)
    bucket_ranges = {cat_num: bucket_preset.get(cat_num, [500, 1000, 2000, 4000, 8000])
                    for cat_num, _, _ in categories}

    now = now_est()
    sid = snapshot_id(now)
    cats: dict[str, Any] = {}
    for cat_num, g2_file, g4_file in categories:
        g2_raw = load_json(game_raw_path(pid, g2_file))
        g4_raw = load_json(game_raw_path(pid, g4_file))
        g2_merged = merge_derived_pairs(g2_raw, g4_raw)
        built = build_category(cat_num, pid, g2_file, g4_file, market_range, bucket_ranges)

        listings: dict[str, dict] = {}
        for row in g2_merged + g4_raw:
            listings[deal_id(row)] = listing_record(row, cat_num)

        cats[f"cat{cat_num}"] = {
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
        "categories": cats,
    }


def load_snapshot(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_snapshot(data: dict[str, Any], path: Path) -> dict[str, Any]:
    out = dict(data)
    out["id"] = out.get("id") or path.stem
    if out.get("captured_at"):
        try:
            dt = parse_captured_at(out["captured_at"], source=path)
            if not _HAS_OFFSET.search(out["captured_at"].strip()):
                out["captured_at"] = iso_est(dt)
            out["captured_label"] = format_est(dt)
        except ValueError:
            out["captured_label"] = out.get("captured_label") or out["id"]
    elif "captured_label" not in out:
        out["captured_label"] = out["id"]
    if "date" not in out:
        out["date"] = out["id"][:10]
    return out


def _snapshot_sort_key(path: Path) -> float:
    try:
        data = load_snapshot(path)
        raw = data.get("captured_at", path.stem)
        return parse_captured_at(raw, source=path).timestamp()
    except (json.JSONDecodeError, OSError, ValueError):
        return 0.0


def top10_entered(prev_top: list, curr_top: list, cat_key: str) -> list[dict]:
    prev_keys = {_deal_key(d) for d in prev_top}
    return [
        _deal_brief(d, cat_key)
        for d in curr_top
        if _deal_key(d) not in prev_keys
    ]


def cleanup_legacy_snapshots(pid: str) -> None:
    snaps = game_snapshots(pid)
    if not snaps.exists():
        return
    ts_dates = _dates_with_timestamped(pid)
    for path in snaps.glob("*.json"):
        if is_legacy_daily_stem(path.stem) and path.stem in ts_dates:
            path.unlink()
            print(f"Removed legacy snapshot: {path.name}")


def list_snapshot_files(pid: str) -> list[Path]:
    snaps = game_snapshots(pid)
    if not snaps.exists():
        return []
    files = list(snaps.glob("*.json"))
    return sorted(files, key=_snapshot_sort_key, reverse=True)


def _dates_with_timestamped(pid: str) -> set[str]:
    dates: set[str] = set()
    snaps = game_snapshots(pid)
    if not snaps.exists():
        return dates
    for path in snaps.glob("*.json"):
        if is_timestamped_stem(path.stem):
            dates.add(path.stem[:10])
    return dates


def list_chain_snapshot_paths(pid: str) -> list[Path]:
    snaps = game_snapshots(pid)
    if not snaps.exists():
        return []
    ts_dates = _dates_with_timestamped(pid)
    selected: list[Path] = []
    for path in snaps.glob("*.json"):
        stem = path.stem
        if is_timestamped_stem(stem):
            selected.append(path)
        elif is_legacy_daily_stem(stem) and stem not in ts_dates:
            selected.append(path)
    return sorted(selected, key=_snapshot_sort_key)


def previous_snapshot(pid: str, exclude_id: str) -> tuple[dict[str, Any] | None, str | None]:
    for path in reversed(list_chain_snapshot_paths(pid)):
        if path.stem == exclude_id:
            continue
        data = normalize_snapshot(load_snapshot(path), path)
        return data, path.stem
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


def _deal_brief(
    d: dict[str, Any],
    cat: str,
    change: str | None = None,
    was_avg: int | None = None,
) -> dict:
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
    if was_avg is not None:
        out["was_avg"] = was_avg
    return out


def extract_inventory(snapshot: dict[str, Any]) -> dict[str, dict]:
    inv: dict[str, dict] = {}
    for cat_key, cat in snapshot["categories"].items():
        inv[cat_key] = {
            "g2": cat["counts"]["g2"],
            "g4": cat["counts"]["g4"],
            "cheapest_g2": cat.get("cheapest_g2"),
            "cheapest_g4": cat.get("cheapest_g4"),
        }
    return inv


def build_log_entry(
    pid: str,
    snapshot: dict[str, Any],
    prev: dict[str, Any] | None,
    prev_id: str | None,
) -> dict[str, Any]:
    from wc2026.games import _STAGE_MARKET_RANGE, _DEFAULT_MARKET_RANGE, get_game
    match = get_game(pid)
    stage = match.get("stage", "Semi-final")
    market_range = _STAGE_MARKET_RANGE.get(stage, _DEFAULT_MARKET_RANGE)

    inventory = extract_inventory(snapshot)
    categories_detail: dict[str, dict] = {}

    for cat_key in snapshot["categories"]:
        cat_num_str = cat_key.replace("cat", "")
        cat_num = int(cat_num_str)
        ccat = snapshot["categories"][cat_key]

        if prev is None or cat_key not in prev.get("categories", {}):
            inv = inventory[cat_key]
            categories_detail[cat_key] = {
                "label": f"Category {cat_num}",
                "g2_count": inv["g2"],
                "g4_count": inv["g4"],
                "g2_delta": 0,
                "g4_delta": 0,
                "cheaper": [],
                "top10_new_g2": [],
                "top10_new_g4": [],
            }
        else:
            from wc2026.utils import market_deal
            pcat = prev["categories"][cat_key]
            diff = compare_listings(pcat["listings"], ccat["listings"])
            g2_delta = ccat["counts"]["g2"] - pcat["counts"]["g2"]
            g4_delta = ccat["counts"]["g4"] - pcat["counts"]["g4"]

            drop_rows: list[tuple[int, dict]] = []
            for p, c in diff["drops"]:
                saved = p["avg"] - c["avg"]
                if saved < 1 or not market_deal(c, cat_num, market_range):
                    continue
                drop_rows.append(
                    (
                        saved,
                        _deal_brief(
                            c,
                            cat_key,
                            f"{fmt_delta(p['avg'], c['avg'])}/ea",
                            was_avg=p["avg"],
                        ),
                    )
                )
            drop_rows.sort(key=lambda x: x[0], reverse=True)

            categories_detail[cat_key] = {
                "label": f"Category {cat_num}",
                "g2_count": ccat["counts"]["g2"],
                "g4_count": ccat["counts"]["g4"],
                "g2_delta": g2_delta,
                "g4_delta": g4_delta,
                "cheaper": [d for _, d in drop_rows][:5],
                "top10_new_g2": top10_entered(
                    pcat.get("top10_g2", []), ccat.get("top10_g2", []), cat_key
                ),
                "top10_new_g4": top10_entered(
                    pcat.get("top10_g4", []), ccat.get("top10_g4", []), cat_key
                ),
            }

    return {
        "id": snapshot["id"],
        "captured_at": snapshot["captured_at"],
        "captured_label": snapshot["captured_label"],
        "prev_id": prev_id,
        "prev_label": (prev.get("captured_label") if prev else None),
        "categories": categories_detail,
        "is_baseline": prev is None,
    }


def load_deal_log_entries(pid: str) -> list[dict]:
    path = game_deal_log_json(pid)
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("entries", [])


def save_deal_log_entries(pid: str, entries: list[dict]) -> None:
    path = game_deal_log_json(pid)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"entries": entries}, indent=2) + "\n",
        encoding="utf-8",
    )


def rebuild_deal_log(pid: str) -> list[dict]:
    paths = list_chain_snapshot_paths(pid)
    chronological: list[dict] = []
    for path in paths:
        chronological.append(normalize_snapshot(load_snapshot(path), path))

    entries: list[dict] = []
    prev: dict[str, Any] | None = None
    prev_id: str | None = None
    for snap in chronological:
        entries.append(build_log_entry(pid, snap, prev, prev_id))
        prev, prev_id = snap, snap["id"]

    entries.reverse()
    save_deal_log_entries(pid, entries)
    return entries


def log_deals(pid: str) -> Path:
    cleanup_legacy_snapshots(pid)
    snapshot = build_snapshot(pid)
    sid = snapshot["id"]

    snaps_dir = game_snapshots(pid)
    snaps_dir.mkdir(parents=True, exist_ok=True)
    snap_path = snaps_dir / f"{sid}.json"
    snap_path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
    print(f"Snapshot saved: {snap_path}")

    entries = rebuild_deal_log(pid)
    latest = entries[0] if entries else None
    print(f"Deal log rebuilt: {game_deal_log_json(pid)} ({len(entries)} entries)")
    if latest:
        print(f"  Latest: {latest['captured_label']}")
        if latest.get("prev_id"):
            print(f"  Compared against: {latest['prev_id']}")
    return game_deal_log_json(pid)


def snapshot_dates_manifest(pid: str) -> list[dict]:
    from wc2026.dates import format_dropdown_label

    by_date: dict[str, dict] = {}
    for path in list_snapshot_files(pid):
        if not is_timestamped_stem(path.stem):
            continue
        try:
            data = normalize_snapshot(load_snapshot(path), path)
            day = data.get("date") or path.stem[:10]
            dt = parse_captured_at(data["captured_at"], source=path)
            ts = dt.timestamp()
            if day not in by_date or ts > by_date[day].get("_ts", 0):
                by_date[day] = {
                    "date": day,
                    "captured_at": data["captured_at"],
                    "label": format_dropdown_label(dt),
                    "_ts": ts,
                }
        except (json.JSONDecodeError, ValueError, OSError):
            continue
    items = [{k: v for k, v in d.items() if k != "_ts"} for d in by_date.values()]
    return sorted(items, key=lambda x: x["date"], reverse=True)


if __name__ == "__main__":
    raise SystemExit("Use: python3 -m wc2026 refresh --game <pid>")
