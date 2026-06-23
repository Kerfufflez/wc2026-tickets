## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 232 groups, price range $4,198 – $204,217 total
G4 fetched: 120 groups → 360 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   360 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 205 Row 17 Seats 7–8  avg $2,220/ea  total $4,440
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 211 groups, price range $2,162 – $14,950 total
G4 fetched: 104 groups → 312 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   306 |       98.1% | May exist in G2, not top-100   |
| NEW        |     6 |        1.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 536 Row 8 Seats 10–11  avg $1,380/ea  total $2,760
Cheapest New: Sec 312 Row 9 Seats 11–12  avg $10,040/ea  total $20,080

Pairs eligible for merge (NEW below G2 min $2,162): 0

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 66 groups, price range $2,870 – $23,552 total
G4 fetched: 23 groups → 69 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    69 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 524 Row 13 Seats 12–13  avg $1,610/ea  total $3,220
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            360 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            306 | DERIVE          |
| Cat 3    |       0.0% |         0 |             69 | INVESTIGATE     |

Overall recommendation: **DERIVE**

