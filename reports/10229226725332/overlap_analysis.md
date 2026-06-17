## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 122 groups, price range $3,094 – $57,500 total
G4 fetched: 123 groups → 369 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   363 |       98.4% | May exist in G2, not top-100   |
| NEW        |     6 |        1.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 149 Row 29 Seats 25–26  avg $1,610/ea  total $3,220
Cheapest New: Sec 106 Row 46 Seats 13–14  avg $1,496/ea  total $2,992

Pairs eligible for merge (NEW below G2 min $3,094): 3

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 187 groups, price range $2,128 – $34,500 total
G4 fetched: 85 groups → 255 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   255 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 341 Row 21 Seats 21–22  avg $1,234/ea  total $2,468
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 54 groups, price range $2,300 – $20,442 total
G4 fetched: 32 groups → 96 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    93 |       96.9% | May exist in G2, not top-100   |
| NEW        |     3 |        3.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 349 Row 24 Seats 22–23  avg $1,150/ea  total $2,300
Cheapest New: Sec 348 Row 25 Seats 13–14  avg $1,149/ea  total $2,298

## Category 4 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 9 groups, price range $2,185 – $6,900 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 331 Row 24 Seats 9–10  avg $1,380/ea  total $2,760
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            363 | DERIVE          |
| Cat 2    |       0.0% |         0 |            255 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             93 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

