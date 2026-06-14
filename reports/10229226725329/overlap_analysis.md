## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 165 groups, price range $1,921 – $57,500 total
G4 fetched: 107 groups → 321 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   321 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 19 Seats 7–8  avg $966/ea  total $1,932
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 191 groups, price range $1,402 – $23,000 total
G4 fetched: 124 groups → 372 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   369 |       99.2% | May exist in G2, not top-100   |
| NEW        |     3 |        0.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 316 Row 6 Seats 8–9  avg $748/ea  total $1,496
Cheapest New: Sec 314 Row 16 Seats 5–6  avg $690/ea  total $1,380

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 9 groups, price range $1,484 – $5,060 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |       80.0% | May exist in G2, not top-100   |
| NEW        |     6 |       20.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 324 Row 23 Seats 13–14  avg $871/ea  total $1,742
Cheapest New: Sec 316 Row 11 Seats 1–2  avg $2,875/ea  total $5,750

Pairs eligible for merge (NEW below G2 min $1,484): 0

## Category 4 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 3 groups, price range $1,610 – $6,900 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 323 Row 26 Seats 12–13  avg $891/ea  total $1,782
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            321 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            369 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             24 | DERIVE          |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

