## Category 1 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 431 groups, price range $2,300 – $27,600 total
G4 fetched: 233 groups → 699 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   690 |       98.7% | May exist in G2, not top-100   |
| NEW        |     9 |        1.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 322 Row R Seats 5–6  avg $1,265/ea  total $2,530
Cheapest New: Sec 328 Row Q Seats 3–4  avg $1,131/ea  total $2,262

Pairs eligible for merge (NEW below G2 min $2,300): 3

## Category 2 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 130 groups, price range $2,012 – $57,500 total
G4 fetched: 70 groups → 210 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   207 |       98.6% | May exist in G2, not top-100   |
| NEW        |     3 |        1.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 636 Row P Seats 15–16  avg $1,035/ea  total $2,070
Cheapest New: Sec 638 Row D Seats 18–19  avg $920/ea  total $1,840

## Category 3 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 64 groups, price range $1,702 – $27,600 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 623 Row L Seats 1–2  avg $1,092/ea  total $2,184
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 7 groups, price range $2,838 – $4,554 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 718 Row P Seats 1–2  avg $1,725/ea  total $3,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            690 | DERIVE          |
| Cat 2    |       0.0% |         3 |            207 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             45 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

