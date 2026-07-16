## Category 1 — Pair Derivation Analysis
Date: July 16, 2026

G2 fetched: 488 groups, price range $1,405 – $81,202 total
G4 fetched: 286 groups → 858 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   855 |       99.7% | May exist in G2, not top-100   |
| NEW        |     3 |        0.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 154 Row 24 Seats 5–6  avg $862/ea  total $1,724
Cheapest New: Sec 121 Row 7 Seats 21–22  avg $106,375/ea  total $212,750

## Category 2 — Pair Derivation Analysis
Date: July 16, 2026

G2 fetched: 192 groups, price range $1,610 – $29,877 total
G4 fetched: 72 groups → 216 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   216 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 323 Row 25 Seats 17–18  avg $874/ea  total $1,748
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 16, 2026

G2 fetched: 105 groups, price range $1,702 – $80,500 total
G4 fetched: 32 groups → 96 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    93 |       96.9% | May exist in G2, not top-100   |
| NEW        |     3 |        3.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 304 Row 18 Seats 9–10  avg $1,000/ea  total $2,000
Cheapest New: Sec 304 Row 24 Seats 17–18  avg $812/ea  total $1,624

## Category 4 — Pair Derivation Analysis
Date: July 16, 2026

G2 fetched: 14 groups, price range $2,300 – $23,000 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 28 Seats 17–18  avg $1,322/ea  total $2,644
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            855 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            216 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             93 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

