## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 208 groups, price range $3,864 – $204,217 total
G4 fetched: 107 groups → 321 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   321 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 232 Row 19 Seats 18–19  avg $2,288/ea  total $4,576
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 193 groups, price range $2,990 – $14,950 total
G4 fetched: 97 groups → 291 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   285 |       97.9% | May exist in G2, not top-100   |
| NEW        |     6 |        2.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 541 Row 13 Seats 21–22  avg $1,673/ea  total $3,346
Cheapest New: Sec 312 Row 9 Seats 11–12  avg $10,040/ea  total $20,080

Pairs eligible for merge (NEW below G2 min $2,990): 0

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 60 groups, price range $3,105 – $23,552 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    60 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 524 Row 13 Seats 12–13  avg $1,610/ea  total $3,220
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            321 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            285 | DERIVE          |
| Cat 3    |       0.0% |         0 |             60 | INVESTIGATE     |

Overall recommendation: **DERIVE**

