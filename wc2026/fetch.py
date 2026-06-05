"""Fetch SeatSidekick match_seat_groups for WC2026 Semi-Final Atlanta."""

from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request

from wc2026.config import (
    API_BASE,
    API_HEADERS,
    DATA_RAW,
    FETCH_META,
    FETCH_QUERIES,
    MAX_SINGLE_LIMIT,
    PAGE_SIZE,
    PERFORMANCE_ID,
    raw_path,
)


def build_url(
    category: str, group_size: int, *, limit: int, offset: int = 0, select: str = "*"
) -> str:
    params = {
        "select": select,
        "performance_id": f"eq.{PERFORMANCE_ID}",
        "dominant_bucket": "eq.Standard",
        "dominant_category": f"eq.{category}",
        "order": "total_price.asc",
        "limit": str(limit),
        "offset": str(offset),
        "group_size": f"eq.{group_size}",
    }
    return f"{API_BASE}?{urllib.parse.urlencode(params)}"


def http_request(url: str, extra_headers: dict | None = None) -> tuple[int, dict, str]:
    headers = {**API_HEADERS, **(extra_headers or {})}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.status, dict(resp.headers), resp.read().decode("utf-8")


def parse_content_range_total(headers: dict) -> int | None:
    raw = headers.get("Content-Range") or headers.get("content-range")
    if not raw:
        return None
    m = re.search(r"/(\d+)\s*$", raw)
    return int(m.group(1)) if m else None


def get_total_count(category: str, group_size: int) -> int | None:
    url = build_url(category, group_size, limit=0, select="group_id")
    try:
        status, headers, body = http_request(
            url, {"Prefer": "count=exact", "Range-Unit": "items"}
        )
        if status not in (200, 206):
            return None
        total = parse_content_range_total(headers)
        if total is not None:
            return total
        data = json.loads(body)
        return len(data) if isinstance(data, list) else None
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError):
        return None


def fetch_page(
    category: str, group_size: int, limit: int, offset: int, max_attempts: int = 5
) -> list | None:
    url = build_url(category, group_size, limit=limit, offset=offset)
    for attempt in range(1, max_attempts + 1):
        try:
            status, _, body = http_request(url)
            if status != 200:
                print(f"  attempt {attempt}: HTTP {status}")
            else:
                data = json.loads(body)
                if isinstance(data, dict) and "code" in data:
                    print(f"  attempt {attempt}: API error {data}")
                elif isinstance(data, list):
                    return data
                else:
                    print(f"  attempt {attempt}: unexpected JSON type")
        except (urllib.error.URLError, json.JSONDecodeError, TimeoutError) as e:
            print(f"  attempt {attempt}: {e}")
        if attempt < max_attempts:
            time.sleep(3)
    return None


def fetch_all(category: str, group_size: int) -> tuple[list | None, int | None]:
    """Fetch complete inventory: high limit first, offset pages as fallback."""
    total = get_total_count(category, group_size)
    if total is not None and total <= MAX_SINGLE_LIMIT:
        batch = fetch_page(category, group_size, limit=max(total, 1), offset=0)
        if batch is not None and len(batch) >= total:
            return batch, total

    all_rows: list = []
    offset = 0
    while True:
        batch = fetch_page(category, group_size, limit=PAGE_SIZE, offset=offset)
        if batch is None:
            return (all_rows if all_rows else None), total
        all_rows.extend(batch)
        if len(batch) < PAGE_SIZE:
            break
        offset += PAGE_SIZE
        if total is not None and len(all_rows) >= total:
            break
    return all_rows, total if total is not None else len(all_rows)


def main() -> int:
    DATA_RAW.mkdir(parents=True, exist_ok=True)
    errors = []
    meta: dict[str, dict] = {}
    for filename, category, group_size in FETCH_QUERIES:
        print(f"Fetching {filename}...")
        data, expected = fetch_all(category, group_size)
        if data is None:
            errors.append(filename)
            print("  FAILED after retries")
            continue
        out = raw_path(filename)
        out.write_text(json.dumps(data, indent=2), encoding="utf-8")
        truncated = expected is not None and len(data) < expected
        meta[filename] = {
            "count": len(data),
            "total": expected,
            "truncated": truncated,
        }
        note = ""
        if truncated:
            note = f" (WARNING: expected {expected}, got {len(data)})"
        elif expected is not None and len(data) > 100:
            note = f" (full inventory; {len(data)} total)"
        print(f"  saved {len(data)} groups -> data/raw/{filename}{note}")
    FETCH_META.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    if errors:
        print(f"\nFailed files: {', '.join(errors)}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
