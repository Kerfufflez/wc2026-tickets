## Category 1 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 309 groups, price range $3,450 – $27,600 total
G4 fetched: 149 groups → 447 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   435 |       97.3% | May exist in G2, not top-100   |
| NEW        |    12 |        2.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 133 Row HH Seats 12–13  avg $2,163/ea  total $4,326
Cheapest New: Sec 131 Row P Seats 7–8  avg $17,250/ea  total $34,500

Pairs eligible for merge (NEW below G2 min $3,450): 0

## Category 2 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 88 groups, price range $3,446 – $57,500 total
G4 fetched: 47 groups → 141 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   141 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 518 Row G Seats 1–2  avg $2,185/ea  total $4,370
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 35 groups, price range $3,450 – $27,600 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |       92.9% | May exist in G2, not top-100   |
| NEW        |     3 |        7.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 722 Row Q Seats 3–4  avg $2,300/ea  total $4,600
Cheapest New: Sec 627 Row D Seats 2–3  avg $1,610/ea  total $3,220

## Category 4 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 5 groups, price range $3,220 – $28,750 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 750 Row P Seats 14–15  avg $1,725/ea  total $3,450
Cheapest New: Sec 745 Row P Seats 14–15  avg $1,552/ea  total $3,104

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |        12 |            435 | DERIVE          |
| Cat 2    |       0.0% |         0 |            141 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             39 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

