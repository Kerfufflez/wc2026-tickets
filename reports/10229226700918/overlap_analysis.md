## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 40 groups, price range $1,955 – $9,218 total
G4 fetched: 22 groups → 66 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    66 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 119 Row 35 Seats 9–10  avg $1,127/ea  total $2,254
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 26 groups, price range $1,838 – $6,900 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 307 Row 23 Seats 17–18  avg $1,006/ea  total $2,012
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 2 groups, price range $1,955 – $2,266 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 316 Row 19 Seats 13–14  avg $1,041/ea  total $2,082
Cheapest New: Sec 339 Row 26 Seats 5–6  avg $1,380/ea  total $2,760

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             66 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             24 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

