## Category 1 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 266 groups, price range $5,175 – $575,000 total
G4 fetched: 83 groups → 249 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   246 |       98.8% | May exist in G2, not top-100   |
| NEW        |     3 |        1.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 138 Row 30 Seats 9–10  avg $2,760/ea  total $5,520
Cheapest New: Sec 102 Row 19 Seats 13–14  avg $2,461/ea  total $4,922

## Category 2 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 239 groups, price range $3,657 – $59,570 total
G4 fetched: 94 groups → 282 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   279 |       98.9% | May exist in G2, not top-100   |
| NEW        |     3 |        1.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 327 Row 12 Seats 5–6  avg $1,955/ea  total $3,910
Cheapest New: Sec 312 Row 11 Seats 16–17  avg $1,438/ea  total $2,876

## Category 3 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 16 groups, price range $3,450 – $11,500 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 301 Row 23 Seats 5–6  avg $4,600/ea  total $9,200
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            246 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            279 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

