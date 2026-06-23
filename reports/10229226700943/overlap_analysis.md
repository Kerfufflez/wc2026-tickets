## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 23 groups, price range $1,024 – $2,990 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    30 |       90.9% | May exist in G2, not top-100   |
| NEW        |     3 |        9.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 124 Row 15 Seats 19–20  avg $805/ea  total $1,610
Cheapest New: Sec 136 Row 16 Seats 11–12  avg $3,450/ea  total $6,900

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 25 groups, price range $1,380 – $4,600 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       66.7% | May exist in G2, not top-100   |
| NEW        |     6 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 124 Row 25 Seats 11–12  avg $886/ea  total $1,772
Cheapest New: Sec 124 Row 33 Seats 4–5  avg $2,645/ea  total $5,290

Pairs eligible for merge (NEW below G2 min $1,380): 0

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 24 groups, price range $1,150 – $3,565 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |       86.7% | May exist in G2, not top-100   |
| NEW        |     6 |       13.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 237 Row 11 Seats 7–8  avg $632/ea  total $1,264
Cheapest New: Sec 243 Row 18 Seats 12–13  avg $564/ea  total $1,128

Pairs eligible for merge (NEW below G2 min $1,150): 3

## Category 4 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 3 groups, price range $1,610 – $4,023 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 207 Row 28 Seats 5–6  avg $805/ea  total $1,610
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             30 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             12 | DERIVE          |
| Cat 3    |       0.0% |         6 |             39 | DERIVE          |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

