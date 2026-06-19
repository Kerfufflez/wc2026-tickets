## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 44 groups, price range $1,449 – $6,900 total
G4 fetched: 30 groups → 90 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    90 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 131 Row 27 Seats 1–2  avg $748/ea  total $1,496
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 81 groups, price range $869 – $3,703 total
G4 fetched: 32 groups → 96 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    90 |       93.8% | May exist in G2, not top-100   |
| NEW        |     6 |        6.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 327 Row 40 Seats 15–16  avg $540/ea  total $1,080
Cheapest New: Sec 127 Row 26 Seats 26–27  avg $2,300/ea  total $4,600

Pairs eligible for merge (NEW below G2 min $869): 0

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 24 groups, price range $1,092 – $2,760 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |       77.8% | May exist in G2, not top-100   |
| NEW        |     6 |       22.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 305 Row 17 Seats 13–14  avg $575/ea  total $1,150
Cheapest New: Sec 305 Row 28 Seats 7–8  avg $1,725/ea  total $3,450

Pairs eligible for merge (NEW below G2 min $1,092): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             90 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             90 | DERIVE          |
| Cat 3    |       0.0% |         6 |             21 | DERIVE          |

Overall recommendation: **DERIVE**

