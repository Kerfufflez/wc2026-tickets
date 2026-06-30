## Category 1 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 325 groups, price range $2,656 – $34,500 total
G4 fetched: 120 groups → 360 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   351 |       97.5% | May exist in G2, not top-100   |
| NEW        |     9 |        2.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 253 Row O Seats 101–102  avg $1,359/ea  total $2,718
Cheapest New: Sec 201 Row NN Seats 103–104  avg $1,322/ea  total $2,644

Pairs eligible for merge (NEW below G2 min $2,656): 3

## Category 2 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 214 groups, price range $2,266 – $32,366 total
G4 fetched: 75 groups → 225 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   225 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 421 Row VV Seats 105–106  avg $1,335/ea  total $2,670
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 48 groups, price range $2,104 – $24,274 total
G4 fetched: 25 groups → 75 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    75 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 424 Row TT Seats 105–106  avg $1,416/ea  total $2,832
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 7 groups, price range $2,185 – $9,786 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 425 Row WW Seats 104–105  avg $1,699/ea  total $3,398
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            351 | DERIVE          |
| Cat 2    |       0.0% |         0 |            225 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             75 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

