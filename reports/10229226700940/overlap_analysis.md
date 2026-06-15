## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 7 groups, price range $6,900 – $23,000 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |       83.3% | May exist in G2, not top-100   |
| NEW        |     3 |       16.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 458 Row 7 Seats 7–8  avg $3,784/ea  total $7,568
Cheapest New: Sec 338 Row D Seats 13–14  avg $20,165/ea  total $40,330

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 5 groups, price range $5,412 – $11,500 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 638 Row 2 Seats 15–16  avg $3,134/ea  total $6,268
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             15 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

