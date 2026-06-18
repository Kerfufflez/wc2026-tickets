## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 16 groups, price range $3,675 – $12,190 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       80.0% | May exist in G2, not top-100   |
| NEW        |     3 |       20.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 128 Row 5 Seats 5–6  avg $2,399/ea  total $4,798
Cheapest New: Sec 117 Row 24 Seats 5–6  avg $20,568/ea  total $41,136

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 28 groups, price range $2,300 – $11,500 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 329 Row 10 Seats 7–8  avg $1,895/ea  total $3,790
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             12 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

