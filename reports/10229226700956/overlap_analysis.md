## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 32 groups, price range $2,530 – $11,500 total
G4 fetched: 18 groups → 54 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    51 |       94.4% | May exist in G2, not top-100   |
| NEW        |     3 |        5.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 131 Row 28 Seats 18–19  avg $1,265/ea  total $2,530
Cheapest New: Sec 107 Row 17 Seats 4–5  avg $1,208/ea  total $2,416

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 28 groups, price range $2,300 – $11,500 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |       91.7% | May exist in G2, not top-100   |
| NEW        |     3 |        8.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 243 Row 24 Seats 21–22  avg $1,150/ea  total $2,300
Cheapest New: Sec 227 Row 20 Seats 9–10  avg $1,121/ea  total $2,242

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 12 groups, price range $1,955 – $5,750 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 221 Row 17 Seats 21–22  avg $1,092/ea  total $2,184
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 1 groups, price range $2,415 – $2,415 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     3 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 231 Row 29 Seats 21–22  avg $1,725/ea  total $3,450

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             51 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             33 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             12 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **PARTIAL**

