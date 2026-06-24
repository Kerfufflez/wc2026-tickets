## Category 1 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 218 groups, price range $3,680 – $204,217 total
G4 fetched: 118 groups → 354 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   354 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 206 Row 14 Seats 1–2  avg $2,275/ea  total $4,550
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 232 groups, price range $2,645 – $11,500 total
G4 fetched: 118 groups → 354 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   339 |       95.8% | May exist in G2, not top-100   |
| NEW        |    15 |        4.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 537 Row 15 Seats 18–19  avg $1,357/ea  total $2,714
Cheapest New: Sec 425 Row 5 Seats 12–13  avg $6,325/ea  total $12,650

Pairs eligible for merge (NEW below G2 min $2,645): 0

## Category 3 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 66 groups, price range $2,760 – $18,952 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 529 Row 22 Seats 14–15  avg $1,380/ea  total $2,760
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            354 | INVESTIGATE     |
| Cat 2    |       0.0% |        15 |            339 | DERIVE          |
| Cat 3    |       0.0% |         0 |             81 | INVESTIGATE     |

Overall recommendation: **DERIVE**

