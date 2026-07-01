## Category 1 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 266 groups, price range $5,290 – $575,000 total
G4 fetched: 83 groups → 249 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   246 |       98.8% | May exist in G2, not top-100   |
| NEW        |     3 |        1.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 113 Row 14 Seats 6–7  avg $2,932/ea  total $5,864
Cheapest New: Sec 139 Row 10 Seats 5–6  avg $2,530/ea  total $5,060

## Category 2 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 235 groups, price range $3,450 – $59,570 total
G4 fetched: 90 groups → 270 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   270 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 327 Row 12 Seats 5–6  avg $1,955/ea  total $3,910
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 15 groups, price range $3,450 – $11,500 total
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
| Cat 2    |       0.0% |         0 |            270 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

