## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 104 groups, price range $4,002 – $57,500 total
G4 fetched: 101 groups → 303 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   300 |       99.0% | May exist in G2, not top-100   |
| NEW        |     3 |        1.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 121 Row 29 Seats 13–14  avg $2,172/ea  total $4,344
Cheapest New: Sec 128 Row 37 Seats 8–9  avg $412,275/ea  total $824,550

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 165 groups, price range $2,932 – $23,000 total
G4 fetched: 71 groups → 213 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   213 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 318 Row 16 Seats 16–17  avg $1,500/ea  total $3,000
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 33 groups, price range $3,448 – $20,442 total
G4 fetched: 25 groups → 75 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    72 |       96.0% | May exist in G2, not top-100   |
| NEW        |     3 |        4.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 349 Row 13 Seats 13–14  avg $1,725/ea  total $3,450
Cheapest New: Sec 349 Row 18 Seats 17–18  avg $1,548/ea  total $3,096

## Category 4 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 6 groups, price range $3,149 – $11,500 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 346 Row 20 Seats 21–22  avg $2,012/ea  total $4,024
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            300 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            213 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             72 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

