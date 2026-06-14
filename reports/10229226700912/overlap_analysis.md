## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 51 groups, price range $1,840 – $11,040 total
G4 fetched: 18 groups → 54 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    51 |       94.4% | May exist in G2, not top-100   |
| NEW        |     3 |        5.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec RN61 Row 3 Seats 12–13  avg $1,103/ea  total $2,206
Cheapest New: Sec 430 Row 2 Seats 18–19  avg $5,749/ea  total $11,498

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 12 groups, price range $1,817 – $4,828 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 518 Row 9 Seats 18–19  avg $1,010/ea  total $2,020
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 12 groups, price range $1,840 – $3,450 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 668 Row 4 Seats 16–17  avg $1,144/ea  total $2,288
Cheapest New: Sec 668 Row 3 Seats 5–6  avg $3,450/ea  total $6,900

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             51 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             24 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

