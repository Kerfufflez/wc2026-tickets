## Category 1 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 151 groups, price range $1,782 – $18,170 total
G4 fetched: 75 groups → 225 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   225 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 149 Row 22 Seats 9–10  avg $977/ea  total $1,954
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 148 groups, price range $1,495 – $11,500 total
G4 fetched: 53 groups → 159 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   150 |       94.3% | May exist in G2, not top-100   |
| NEW        |     9 |        5.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 335 Row 26 Seats 24–25  avg $799/ea  total $1,598
Cheapest New: Sec 311 Row 8 Seats 5–6  avg $690/ea  total $1,380

Pairs eligible for merge (NEW below G2 min $1,495): 3

## Category 3 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 51 groups, price range $1,449 – $12,880 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 303 Row 25 Seats 10–11  avg $805/ea  total $1,610
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 6 groups, price range $1,725 – $11,500 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 346 Row 21 Seats 23–24  avg $1,380/ea  total $2,760
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            225 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |            150 | DERIVE          |
| Cat 3    |       0.0% |         0 |             39 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

