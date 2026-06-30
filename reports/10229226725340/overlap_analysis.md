## Category 1 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 398 groups, price range $952 – $24,274 total
G4 fetched: 154 groups → 462 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   462 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 224 Row GG Seats 103–104  avg $564/ea  total $1,128
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 232 groups, price range $866 – $23,564 total
G4 fetched: 88 groups → 264 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   258 |       97.7% | May exist in G2, not top-100   |
| NEW        |     6 |        2.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 447 Row GG Seats 2–3  avg $443/ea  total $886
Cheapest New: Sec 409 Row PP Seats 103–104  avg $392/ea  total $784

Pairs eligible for merge (NEW below G2 min $866): 6

## Category 3 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 93 groups, price range $816 – $11,155 total
G4 fetched: 44 groups → 132 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   132 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 425 Row UU Seats 107–108  avg $433/ea  total $866
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 10 groups, price range $809 – $2,070 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 427 Row YY Seats 2–3  avg $748/ea  total $1,496
Cheapest New: Sec 452 Row XX Seats 101–102  avg $1,133/ea  total $2,266

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            462 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            258 | DERIVE          |
| Cat 3    |       0.0% |         0 |            132 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

