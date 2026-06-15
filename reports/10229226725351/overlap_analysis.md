## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 119 groups, price range $3,668 – $75,900 total
G4 fetched: 69 groups → 207 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   207 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 135 Row 16 Seats 7–8  avg $2,007/ea  total $4,014
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 88 groups, price range $2,967 – $27,600 total
G4 fetched: 61 groups → 183 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   177 |       96.7% | May exist in G2, not top-100   |
| NEW        |     6 |        3.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 308 Row 24 Seats 1–2  avg $1,495/ea  total $2,990
Cheapest New: Sec 309 Row 23 Seats 9–10  avg $1,450/ea  total $2,900

Pairs eligible for merge (NEW below G2 min $2,967): 3

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 73 groups, price range $2,298 – $12,650 total
G4 fetched: 33 groups → 99 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    96 |       97.0% | May exist in G2, not top-100   |
| NEW        |     3 |        3.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 330 Row 19 Seats 1–2  avg $1,380/ea  total $2,760
Cheapest New: Sec 319 Row 22 Seats 10–11  avg $6,899/ea  total $13,798

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            207 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            177 | DERIVE          |
| Cat 3    |       0.0% |         3 |             96 | INVESTIGATE     |

Overall recommendation: **DERIVE**

