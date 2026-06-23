## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 247 groups, price range $3,795 – $204,217 total
G4 fetched: 124 groups → 372 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   372 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 205 Row 17 Seats 7–8  avg $2,220/ea  total $4,440
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 217 groups, price range $2,760 – $14,950 total
G4 fetched: 105 groups → 315 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   309 |       98.1% | May exist in G2, not top-100   |
| NEW        |     6 |        1.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 542 Row 10 Seats 13–14  avg $1,466/ea  total $2,932
Cheapest New: Sec 312 Row 9 Seats 11–12  avg $9,936/ea  total $19,872

Pairs eligible for merge (NEW below G2 min $2,760): 0

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 65 groups, price range $2,506 – $23,552 total
G4 fetched: 23 groups → 69 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    69 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 532 Row 20 Seats 15–16  avg $1,656/ea  total $3,312
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            372 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            309 | DERIVE          |
| Cat 3    |       0.0% |         0 |             69 | INVESTIGATE     |

Overall recommendation: **DERIVE**

