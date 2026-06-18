## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 114 groups, price range $2,875 – $1,426,000 total
G4 fetched: 65 groups → 195 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   192 |       98.5% | May exist in G2, not top-100   |
| NEW        |     3 |        1.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 138 Row 33 Seats 9–10  avg $1,438/ea  total $2,876
Cheapest New: Sec 126 Row 14 Seats 5–6  avg $1,419/ea  total $2,838

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 109 groups, price range $2,070 – $23,000 total
G4 fetched: 61 groups → 183 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   183 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 17 Seats 13–14  avg $1,121/ea  total $2,242
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 8 groups, price range $2,760 – $8,050 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 315 Row 18 Seats 5–6  avg $1,725/ea  total $3,450
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 1 groups, price range $6,900 – $6,900 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     3 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 323 Row 21 Seats 5–6  avg $1,898/ea  total $3,796

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            192 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            183 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              6 | SKIP            |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **PARTIAL**

