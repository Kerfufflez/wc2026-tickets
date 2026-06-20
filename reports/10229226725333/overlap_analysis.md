## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 128 groups, price range $2,988 – $232,184 total
G4 fetched: 72 groups → 216 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   216 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 204 Row 4 Seats 13–14  avg $1,596/ea  total $3,192
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 106 groups, price range $2,139 – $13,800 total
G4 fetched: 71 groups → 213 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   210 |       98.6% | May exist in G2, not top-100   |
| NEW        |     3 |        1.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 448 Row 23 Seats 5–6  avg $1,092/ea  total $2,184
Cheapest New: Sec 409 Row 26 Seats 5–6  avg $1,004/ea  total $2,008

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 16 groups, price range $2,461 – $6,900 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |       55.6% | May exist in G2, not top-100   |
| NEW        |    12 |       44.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 422 Row 13 Seats 11–12  avg $1,265/ea  total $2,530
Cheapest New: Sec 406 Row 24 Seats 7–8  avg $1,150/ea  total $2,300

Pairs eligible for merge (NEW below G2 min $2,461): 3

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            216 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            210 | INVESTIGATE     |
| Cat 3    |       0.0% |        12 |             15 | DERIVE          |

Overall recommendation: **DERIVE**

