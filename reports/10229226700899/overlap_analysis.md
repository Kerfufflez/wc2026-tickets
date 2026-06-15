## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 182 groups, price range $798 – $13,788 total
G4 fetched: 118 groups → 354 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   351 |       99.2% | May exist in G2, not top-100   |
| NEW        |     3 |        0.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 133 Row 18 Seats 9–10  avg $402/ea  total $804
Cheapest New: Sec 107 Row 17 Seats 21–22  avg $396/ea  total $792

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 112 groups, price range $655 – $3,450 total
G4 fetched: 57 groups → 171 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   168 |       98.2% | May exist in G2, not top-100   |
| NEW        |     3 |        1.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 207 Row 6 Seats 13–14  avg $339/ea  total $678
Cheapest New: Sec 318 Row 20 Seats 13–14  avg $288/ea  total $576

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 65 groups, price range $575 – $13,800 total
G4 fetched: 22 groups → 66 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    66 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 332 Row 27 Seats 21–22  avg $345/ea  total $690
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 12 groups, price range $690 – $2,760 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 308 Row 23 Seats 6–7  avg $443/ea  total $886
Cheapest New: Sec 308 Row 30 Seats 5–6  avg $4,025/ea  total $8,050

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            351 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            168 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             66 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

