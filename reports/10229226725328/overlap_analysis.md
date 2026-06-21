## Category 1 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 188 groups, price range $4,138 – $204,217 total
G4 fetched: 94 groups → 282 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   282 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 232 Row 11 Seats 15–16  avg $2,299/ea  total $4,598
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 174 groups, price range $2,811 – $14,950 total
G4 fetched: 91 groups → 273 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   267 |       97.8% | May exist in G2, not top-100   |
| NEW        |     6 |        2.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 541 Row 13 Seats 21–22  avg $1,673/ea  total $3,346
Cheapest New: Sec 312 Row 9 Seats 11–12  avg $10,040/ea  total $20,080

Pairs eligible for merge (NEW below G2 min $2,811): 0

## Category 3 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 52 groups, price range $3,220 – $23,552 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 529 Row 11 Seats 9–10  avg $1,811/ea  total $3,622
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            282 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            267 | DERIVE          |
| Cat 3    |       0.0% |         0 |             45 | INVESTIGATE     |

Overall recommendation: **DERIVE**

