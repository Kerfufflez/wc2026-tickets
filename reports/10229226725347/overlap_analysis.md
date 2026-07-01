## Category 1 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 208 groups, price range $5,286 – $57,500 total
G4 fetched: 112 groups → 336 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   336 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 36 Seats 1–2  avg $2,656/ea  total $5,312
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 229 groups, price range $3,404 – $46,000 total
G4 fetched: 119 groups → 357 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   354 |       99.2% | May exist in G2, not top-100   |
| NEW        |     3 |        0.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 343 Row 8 Seats 11–12  avg $1,953/ea  total $3,906
Cheapest New: Sec 318 Row 26 Seats 11–12  avg $1,679/ea  total $3,358

## Category 3 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 115 groups, price range $3,680 – $46,000 total
G4 fetched: 30 groups → 90 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    90 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 305 Row 15 Seats 12–13  avg $2,300/ea  total $4,600
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 8 groups, price range $4,600 – $69,000 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 306 Row 22 Seats 17–18  avg $2,656/ea  total $5,312
Cheapest New: Sec 306 Row 23 Seats 13–14  avg $2,242/ea  total $4,484

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            336 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            354 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             90 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

