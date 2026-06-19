## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 98 groups, price range $3,274 – $1,426,000 total
G4 fetched: 58 groups → 174 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   171 |       98.3% | May exist in G2, not top-100   |
| NEW        |     3 |        1.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 116 Row 21 Seats 9–10  avg $1,668/ea  total $3,336
Cheapest New: Sec 124 Row 16 Seats 13–14  avg $1,610/ea  total $3,220

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 89 groups, price range $2,645 – $23,000 total
G4 fetched: 50 groups → 150 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   150 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 338 Row 5 Seats 1–2  avg $1,354/ea  total $2,708
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

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

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            171 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            150 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

