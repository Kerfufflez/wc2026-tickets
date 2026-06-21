## Category 1 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 108 groups, price range $3,703 – $57,500 total
G4 fetched: 87 groups → 261 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   258 |       98.9% | May exist in G2, not top-100   |
| NEW        |     3 |        1.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 41 Seats 5–6  avg $2,218/ea  total $4,436
Cheapest New: Sec 128 Row 37 Seats 8–9  avg $412,275/ea  total $824,550

## Category 2 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 161 groups, price range $3,335 – $23,000 total
G4 fetched: 71 groups → 213 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   201 |       94.4% | May exist in G2, not top-100   |
| NEW        |    12 |        5.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 310 Row 6 Seats 17–18  avg $1,668/ea  total $3,336
Cheapest New: Sec 308 Row 23 Seats 17–18  avg $1,610/ea  total $3,220

Pairs eligible for merge (NEW below G2 min $3,335): 9

## Category 3 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 37 groups, price range $2,760 – $20,442 total
G4 fetched: 23 groups → 69 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    69 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 307 Row 16 Seats 5–6  avg $1,782/ea  total $3,564
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 5 groups, price range $3,450 – $11,500 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 346 Row 20 Seats 21–22  avg $2,012/ea  total $4,024
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            258 | INVESTIGATE     |
| Cat 2    |       0.0% |        12 |            201 | DERIVE          |
| Cat 3    |       0.0% |         0 |             69 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

