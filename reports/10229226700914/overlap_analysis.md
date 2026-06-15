## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 162 groups, price range $981 – $30,513 total
G4 fetched: 100 groups → 300 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   300 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 232 Row 27 Seats 21–22  avg $518/ea  total $1,036
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 231 groups, price range $805 – $8,050 total
G4 fetched: 140 groups → 420 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   420 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 543 Row 16 Seats 10–11  avg $437/ea  total $874
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 41 groups, price range $803 – $8,048 total
G4 fetched: 24 groups → 72 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    72 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 552 Row 13 Seats 10–11  avg $437/ea  total $874
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 5 groups, price range $1,035 – $1,380 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 553 Row 13 Seats 10–11  avg $632/ea  total $1,264
Cheapest New: Sec 526 Row 18 Seats 5–6  avg $1,639/ea  total $3,278

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            300 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            420 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             72 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

