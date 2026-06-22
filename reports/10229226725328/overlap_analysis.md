## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 208 groups, price range $4,255 – $204,217 total
G4 fetched: 102 groups → 306 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   306 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 232 Row 11 Seats 15–16  avg $2,299/ea  total $4,598
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 185 groups, price range $2,990 – $14,950 total
G4 fetched: 99 groups → 297 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   291 |       98.0% | May exist in G2, not top-100   |
| NEW        |     6 |        2.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 407 Row 2 Seats 13–14  avg $1,495/ea  total $2,990
Cheapest New: Sec 312 Row 9 Seats 11–12  avg $10,040/ea  total $20,080

Pairs eligible for merge (NEW below G2 min $2,990): 0

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 58 groups, price range $3,105 – $23,552 total
G4 fetched: 21 groups → 63 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    63 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 529 Row 11 Seats 9–10  avg $1,811/ea  total $3,622
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            306 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            291 | DERIVE          |
| Cat 3    |       0.0% |         0 |             63 | INVESTIGATE     |

Overall recommendation: **DERIVE**

