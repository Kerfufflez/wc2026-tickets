## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 90 groups, price range $1,714 – $11,875 total
G4 fetched: 36 groups → 108 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   105 |       97.2% | May exist in G2, not top-100   |
| NEW        |     3 |        2.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 108 Row 19 Seats 7–8  avg $920/ea  total $1,840
Cheapest New: Sec 111 Row 32 Seats 10–11  avg $799/ea  total $1,598

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 55 groups, price range $1,319 – $4,948 total
G4 fetched: 26 groups → 78 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    75 |       96.2% | May exist in G2, not top-100   |
| NEW        |     3 |        3.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 225 Row 30 Seats 19–20  avg $684/ea  total $1,368
Cheapest New: Sec C25 Row 2 Seats 17–18  avg $5,750/ea  total $11,500

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 26 groups, price range $1,380 – $4,948 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |       92.3% | May exist in G2, not top-100   |
| NEW        |     3 |        7.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 216 Row 17 Seats 1–2  avg $776/ea  total $1,552
Cheapest New: Sec 231 Row 17 Seats 6–7  avg $661/ea  total $1,322

## Category 4 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 2 groups, price range $1,380 – $2,760 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 239 Row 30 Seats 7–8  avg $748/ea  total $1,496
Cheapest New: Sec 239 Row 29 Seats 9–10  avg $1,725/ea  total $3,450

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            105 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             75 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             36 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

