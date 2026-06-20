## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 176 groups, price range $2,300 – $153,332 total
G4 fetched: 72 groups → 216 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   210 |       97.2% | May exist in G2, not top-100   |
| NEW        |     6 |        2.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 222 Row OO Seats 1–2  avg $1,231/ea  total $2,462
Cheapest New: Sec 201 Row OO Seats 1–2  avg $1,107/ea  total $2,214

Pairs eligible for merge (NEW below G2 min $2,300): 6

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 104 groups, price range $2,068 – $24,380 total
G4 fetched: 42 groups → 126 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   120 |       95.2% | May exist in G2, not top-100   |
| NEW        |     6 |        4.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 436 Row OO Seats 103–104  avg $1,035/ea  total $2,070
Cheapest New: Sec 420 Row HH Seats 102–103  avg $1,026/ea  total $2,052

Pairs eligible for merge (NEW below G2 min $2,068): 3

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 26 groups, price range $1,970 – $8,206 total
G4 fetched: 18 groups → 54 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    54 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 404 Row TT Seats 4–5  avg $985/ea  total $1,970
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 4 groups, price range $2,134 – $3,793 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 427 Row YY Seats 2–3  avg $1,725/ea  total $3,450
Cheapest New: Sec 452 Row XX Seats 101–102  avg $2,462/ea  total $4,924

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            210 | DERIVE          |
| Cat 2    |       0.0% |         6 |            120 | DERIVE          |
| Cat 3    |       0.0% |         0 |             54 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

