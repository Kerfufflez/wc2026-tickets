"""Match list fetching and per-game configuration."""

from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timezone

from wc2026.config import API_HEADERS, MATCHES_API, MATCHES_CACHE

# Stage-based price bucket presets.
# Each entry: list of 5 breakpoints → 6 buckets (below first, between each, above last).
_STAGE_BUCKETS: dict[str, dict[int, list[int]]] = {
    "Group Stage": {
        1: [600, 900, 1300, 1800, 2500],
        2: [400, 650, 950, 1400, 2000],
        3: [200, 350, 550, 800, 1200],
        4: [150, 250, 400, 600, 900],
    },
    "Round of 32": {
        1: [800, 1200, 1800, 2500, 3500],
        2: [500, 800, 1200, 1800, 2500],
        3: [300, 500, 750, 1100, 1600],
        4: [200, 350, 550, 800, 1200],
    },
    "Round of 16": {
        1: [1000, 1500, 2200, 3200, 4500],
        2: [600, 1000, 1500, 2200, 3200],
        3: [400, 650, 1000, 1500, 2200],
        4: [300, 500, 800, 1200, 1800],
    },
    "Quarter-final": {
        1: [2000, 3000, 4500, 6500, 9000],
        2: [1000, 1600, 2500, 3800, 5500],
        3: [600, 1000, 1600, 2500, 3800],
        4: [400, 700, 1100, 1700, 2500],
    },
    "Semi-final": {
        1: [4500, 5000, 5500, 6000, 6500],
        2: [3000, 3500, 4000, 4500, 5000],
        3: [2500, 3000, 3500, 4000, 5000],
        4: [1500, 2000, 2800, 3800, 5000],
    },
    "Third Place": {
        1: [2000, 3000, 4500, 6500, 9000],
        2: [1000, 1600, 2500, 3800, 5500],
        3: [600, 1000, 1600, 2500, 3800],
        4: [400, 700, 1100, 1700, 2500],
    },
    "Final": {
        1: [6000, 8000, 11000, 15000, 20000],
        2: [3500, 5000, 7000, 10000, 14000],
        3: [2000, 3000, 4500, 6500, 9000],
        4: [1000, 1600, 2500, 3800, 5500],
    },
}

_DEFAULT_BUCKETS = _STAGE_BUCKETS["Semi-final"]

# Market range per category (lo, hi) — listings outside are excluded from rankings.
_STAGE_MARKET_RANGE: dict[str, dict[int, tuple[int, int]]] = {
    "Group Stage":    {1: (300, 8000),   2: (150, 6000),   3: (100, 4000),   4: (100, 3000)},
    "Round of 32":   {1: (400, 12000),   2: (200, 8000),   3: (150, 6000),   4: (100, 4000)},
    "Round of 16":   {1: (500, 15000),   2: (300, 10000),  3: (200, 7000),   4: (150, 5000)},
    "Quarter-final": {1: (1000, 25000),  2: (500, 15000),  3: (300, 10000),  4: (200, 7000)},
    "Semi-final":    {1: (3000, 35000),  2: (500, 25000),  3: (1500, 15000), 4: (1000, 10000)},
    "Third Place":   {1: (1000, 25000),  2: (500, 15000),  3: (300, 10000),  4: (200, 7000)},
    "Final":         {1: (3000, 60000),  2: (1500, 40000), 3: (800, 25000),  4: (500, 15000)},
}

_DEFAULT_MARKET_RANGE = _STAGE_MARKET_RANGE["Semi-final"]


def _bucket_labels(breakpoints: list[int]) -> list[str]:
    def fmt(v: int) -> str:
        if v >= 1000:
            k = v // 1000
            frac = (v % 1000) // 100
            return f"${k}.{frac}k" if frac else f"${k}k"
        return f"${v}"

    labels = [f"<{fmt(breakpoints[0])}"]
    for i in range(len(breakpoints) - 1):
        labels.append(f"{fmt(breakpoints[i])}–{fmt(breakpoints[i+1])}")
    labels.append(f"{fmt(breakpoints[-1])}+")
    return labels


def fetch_matches() -> int:
    """Fetch match list from SeatSidekick → data/matches.json. Returns game count."""
    req = urllib.request.Request(
        MATCHES_API,
        headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    matches = data.get("matches", [])
    MATCHES_CACHE.parent.mkdir(parents=True, exist_ok=True)
    MATCHES_CACHE.write_text(json.dumps({"matches": matches}, indent=2), encoding="utf-8")
    print(f"Fetched {len(matches)} matches → {MATCHES_CACHE}")
    return len(matches)


def load_matches() -> list[dict]:
    if not MATCHES_CACHE.exists():
        raise FileNotFoundError(
            f"No matches cache found at {MATCHES_CACHE}. Run: python3 -m wc2026 fetch-games"
        )
    return json.loads(MATCHES_CACHE.read_text(encoding="utf-8"))["matches"]


def get_game(pid: str | int) -> dict:
    pid_str = str(pid)
    for m in load_matches():
        if str(m["pid"]) == pid_str or m.get("eventCode") == pid_str:
            return m
    raise ValueError(f"Game not found: {pid!r}. Check data/matches.json.")


def game_categories(match: dict) -> list[tuple[int, str, str]]:
    """Return [(cat_num, g2_filename, g4_filename), ...] sorted by category number."""
    cats = match.get("cats", {})
    result = []
    for key in sorted(cats.keys()):
        n_str = key.replace("Category ", "").strip()
        if n_str.isdigit():
            n = int(n_str)
            result.append((n, f"cat{n}_g2.json", f"cat{n}_g4.json"))
    return result


def game_config_js(match: dict) -> str:
    """Return an inline <script> block setting window.__wc2026Config."""
    pid = str(match["pid"])
    stage = match.get("stage", "Semi-final")
    cats = game_categories(match)

    bucket_preset = _STAGE_BUCKETS.get(stage, _DEFAULT_BUCKETS)
    market_preset = _STAGE_MARKET_RANGE.get(stage, _DEFAULT_MARKET_RANGE)

    queries = []
    bucket_ranges: dict[int, list[int]] = {}
    bucket_labels: dict[int, list[str]] = {}
    cat_market_range: dict[int, list[int]] = {}

    for cat_num, _, _ in cats:
        queries.append({"cat": cat_num, "gs": 2, "category": f"Category {cat_num}"})
        queries.append({"cat": cat_num, "gs": 4, "category": f"Category {cat_num}"})
        bp = bucket_preset.get(cat_num, _DEFAULT_BUCKETS.get(cat_num, [500, 1000, 2000, 4000, 8000]))
        mr = market_preset.get(cat_num, (100, 50000))
        bucket_ranges[cat_num] = bp
        bucket_labels[cat_num] = _bucket_labels(bp)
        cat_market_range[cat_num] = list(mr)

    config = {
        "performanceId": pid,
        "queries": queries,
        "bucketRanges": {str(k): v for k, v in bucket_ranges.items()},
        "bucketLabels": {str(k): v for k, v in bucket_labels.items()},
        "catMarketRange": {str(k): v for k, v in cat_market_range.items()},
    }
    return f"<script>window.__wc2026Config = {json.dumps(config, separators=(',', ':'))};</script>"


def format_game_date(match: dict) -> str:
    """Format match date as 'July 15, 2026' in local time."""
    raw = match.get("date", "")
    if not raw:
        return ""
    try:
        dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        return dt.strftime("%B %-d, %Y")
    except ValueError:
        return raw[:10]
