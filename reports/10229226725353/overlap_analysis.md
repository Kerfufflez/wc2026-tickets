## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 195 groups, price range $5,500 – $80,500 total
G4 fetched: 89 groups → 267 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   267 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 123 Row 38 Seats 14–15  avg $2,869/ea  total $5,738
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 165 groups, price range $4,370 – $112,700 total
G4 fetched: 79 groups → 237 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   234 |       98.7% | May exist in G2, not top-100   |
| NEW        |     3 |        1.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 335 Row 5 Seats 9–10  avg $2,299/ea  total $4,598
Cheapest New: Sec 327 Row 15 Seats 5–6  avg $2,184/ea  total $4,368

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 12 groups, price range $4,368 – $11,500 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 315 Row 25 Seats 6–7  avg $2,472/ea  total $4,944
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 4 groups, price range $4,082 – $9,200 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 318 Row 15 Seats 5–6  avg $3,852/ea  total $7,704
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            267 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            234 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

