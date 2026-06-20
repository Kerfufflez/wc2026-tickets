## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 151 groups, price range $4,600 – $204,217 total
G4 fetched: 82 groups → 246 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   243 |       98.8% | May exist in G2, not top-100   |
| NEW        |     3 |        1.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 210 Row 16 Seats 23–24  avg $2,339/ea  total $4,678
Cheapest New: Sec 232 Row 11 Seats 15–16  avg $2,299/ea  total $4,598

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 141 groups, price range $2,940 – $11,500 total
G4 fetched: 87 groups → 261 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   246 |       94.3% | May exist in G2, not top-100   |
| NEW        |    15 |        5.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 539 Row 9 Seats 13–14  avg $1,495/ea  total $2,990
Cheapest New: Sec 315 Row 7 Seats 1–2  avg $6,900/ea  total $13,800

Pairs eligible for merge (NEW below G2 min $2,940): 0

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 51 groups, price range $2,760 – $46,552 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    42 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 534 Row 10 Seats 8–9  avg $1,725/ea  total $3,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            243 | INVESTIGATE     |
| Cat 2    |       0.0% |        15 |            246 | DERIVE          |
| Cat 3    |       0.0% |         0 |             42 | INVESTIGATE     |

Overall recommendation: **DERIVE**

