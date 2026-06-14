# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Full pipeline (fetch → overlap → build)
./refresh.sh
# or:
python3 -m wc2026 refresh

# Individual steps
python3 -m wc2026 fetch     # pull API data → data/raw/
python3 -m wc2026 overlap   # G4 pair overlap report → reports/overlap_analysis.md
python3 -m wc2026 build     # dashboard HTML + deal log + docs/
```

No install step — stdlib only (no third-party dependencies). Requires Python 3.12+ for `zoneinfo`.

Open `reports/dashboard.html` locally; `docs/index.html` is the GitHub Pages copy (auto-generated — don't edit directly).

## Architecture

### Pipeline overview

```
fetch.py → data/raw/*.json
build.py → reports/dashboard.html  (patches template inline JS in-place)
tracker.py → reports/history/snapshots/*.json + deal_log.json
render_deal_log.py → reports/history/deal-log.html
publish.py → docs/index.html + docs/archive/YYYY-MM-DD.html
```

`build.py:main()` orchestrates the last four steps in sequence.

### Data flow

**Fetch** (`fetch.py`): Queries the SeatSidekick Supabase REST API for 6 endpoints (3 ticket categories × 2 group sizes: G2 and G4). Results saved to `data/raw/cat{N}_g{2|4}.json`. API constants and all paths live in `config.py` — that's the single source of truth.

**Derive** (`derive.py`): Extracts virtual adjacent-pair G2 listings from G4 inventory. A 4-seat listing containing seats [10,11,12,13] yields pairs (10,11), (11,12), (12,13). These derived rows are merged into the G2 pool by `build.py:merge_derived_pairs()` — but only when cheaper than the cheapest native G2 listing (to surface hidden value in 4-packs).

**Build** (`build.py`): Loads raw JSON, applies market-range filtering (via `utils.CAT_MARKET_RANGE`), computes top-10 deals, metrics, chart bucket counts, and inventory by section. Then **patches the HTML template in-place using regex substitutions** — it replaces inline JS arrays like `const cat1g2 = [...]` and `makeChart(...)` calls directly inside `templates/dashboard.html`. The patched file is written to `reports/dashboard.html`.

**Track** (`tracker.py`): On each build, saves a timestamped JSON snapshot of all listings to `reports/history/snapshots/`. Rebuilds the full deal-log changelog by diffing consecutive snapshots (price drops, new listings, gone listings). Snapshot filenames are `YYYY-MM-DDTHHmmss` (ET). Legacy daily stems (`YYYY-MM-DD`) are cleaned up when timestamped files exist for the same day.

**Publish** (`publish.py`): Copies `reports/dashboard.html` → `docs/index.html`, writes a dated archive copy to `docs/archive/YYYY-MM-DD.html`, and builds the snapshot dropdown manifest at `docs/history/manifest.json`. Also copies `static/refresh.js` and the deal-log HTML into `docs/`.

### Key design decisions

- **Data embedded in HTML**: Inventory data is inlined as JS arrays inside the HTML — no API calls needed to view a snapshot. The browser-side `refresh.js` does live pulls on demand.
- **Template is the authoritative HTML source**: `templates/dashboard.html` is the edit target; `reports/dashboard.html` is always overwritten on build. Never edit `docs/` files manually.
- **Market-range filtering**: `utils.CAT_MARKET_RANGE` defines per-category `(min, max)` avg-price bounds. Listings outside this range are silently excluded from rankings and metrics (they remain in raw data).
- **All timestamps in ET**: `dates.py` is the single source of truth for timezone handling. `parse_captured_at()` includes logic to handle legacy CI snapshots that were written in UTC without an offset.

### Module summary

| Module | Role |
|---|---|
| `config.py` | All paths + API constants |
| `fetch.py` | HTTP pagination against Supabase REST |
| `derive.py` | Adjacent-pair extraction from G4 rows |
| `utils.py` | `row_to_deal()`, `market_avg()`, chart buckets, JS serialization |
| `build.py` | Category aggregation + HTML template patching |
| `tracker.py` | Snapshot persistence + deal-log diff engine |
| `render_deal_log.py` | deal_log.json → styled HTML changelog |
| `publish.py` | docs/ assembly, archive dropdown, manifest |
| `dates.py` | ET formatting + snapshot ID generation |
| `overlap.py` | Standalone G4 derivation analysis report |

### GitHub Actions

`.github/workflows/refresh.yml` runs `fetch` then `build` every 6 hours, commits changes to `docs/`, `reports/`, and `data/raw/`. It does **not** run `overlap`.
