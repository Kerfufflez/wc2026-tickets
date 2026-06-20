## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 157 groups, price range $4,439 – $204,217 total
G4 fetched: 80 groups → 240 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   240 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 232 Row 11 Seats 15–16  avg $2,299/ea  total $4,598
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 149 groups, price range $2,945 – $11,500 total
G4 fetched: 86 groups → 258 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   240 |       93.0% | May exist in G2, not top-100   |
| NEW        |    18 |        7.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 539 Row 9 Seats 13–14  avg $1,495/ea  total $2,990
Cheapest New: Sec 425 Row 5 Seats 12–13  avg $6,325/ea  total $12,650

Pairs eligible for merge (NEW below G2 min $2,945): 0

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 53 groups, price range $3,278 – $46,552 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 534 Row 10 Seats 8–9  avg $1,725/ea  total $3,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            240 | INVESTIGATE     |
| Cat 2    |       0.0% |        18 |            240 | DERIVE          |
| Cat 3    |       0.0% |         0 |             39 | INVESTIGATE     |

Overall recommendation: **DERIVE**

