## Category 1 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 329 groups, price range $1,530 – $153,332 total
G4 fetched: 127 groups → 381 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   378 |       99.2% | May exist in G2, not top-100   |
| NEW        |     3 |        0.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 201 Row C Seats 106–107  avg $809/ea  total $1,618
Cheapest New: Sec 254 Row CC Seats 5–6  avg $748/ea  total $1,496

## Category 2 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 177 groups, price range $1,295 – $23,770 total
G4 fetched: 63 groups → 189 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   189 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 435 Row YY Seats 6–7  avg $690/ea  total $1,380
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 69 groups, price range $1,259 – $13,800 total
G4 fetched: 22 groups → 66 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    66 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 453 Row OO Seats 104–105  avg $688/ea  total $1,376
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 5 groups, price range $1,610 – $3,793 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 427 Row YY Seats 2–3  avg $1,035/ea  total $2,070
Cheapest New: Sec 452 Row XX Seats 101–102  avg $2,427/ea  total $4,854

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            378 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            189 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             66 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

