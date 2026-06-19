## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 38 groups, price range $5,290 – $34,500 total
G4 fetched: 18 groups → 54 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    51 |       94.4% | May exist in G2, not top-100   |
| NEW        |     3 |        5.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 346 Row R Seats 4–5  avg $2,875/ea  total $5,750
Cheapest New: Sec 116 Row J Seats 5–6  avg $2,530/ea  total $5,060

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 17 groups, price range $3,392 – $11,498 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 517 Row H Seats 13–14  avg $1,725/ea  total $3,450
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 6 groups, price range $4,600 – $18,135 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 625 Row F Seats 13–14  avg $2,588/ea  total $5,176
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             51 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |              6 | SKIP            |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

