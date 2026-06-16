## Category 1 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 213 groups, price range $4,140 – $80,500 total
G4 fetched: 108 groups → 324 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   321 |       99.1% | May exist in G2, not top-100   |
| NEW        |     3 |        0.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 117 Row 22 Seats 9–10  avg $2,300/ea  total $4,600
Cheapest New: Sec 118 Row 32 Seats 17–18  avg $2,036/ea  total $4,072

## Category 2 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 208 groups, price range $2,760 – $112,700 total
G4 fetched: 113 groups → 339 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   339 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 9 Seats 13–14  avg $1,581/ea  total $3,162
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 17 groups, price range $3,450 – $11,500 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 301 Row 15 Seats 1–2  avg $1,725/ea  total $3,450
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 4 groups, price range $4,082 – $9,200 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 318 Row 15 Seats 5–6  avg $2,790/ea  total $5,580
Cheapest New: Sec 323 Row 25 Seats 1–2  avg $1,744/ea  total $3,488

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            321 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            339 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             15 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

