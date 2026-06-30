## Category 1 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 392 groups, price range $2,800 – $27,600 total
G4 fetched: 211 groups → 633 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   624 |       98.6% | May exist in G2, not top-100   |
| NEW        |     9 |        1.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 332 Row Q Seats 7–8  avg $1,466/ea  total $2,932
Cheapest New: Sec 115 Row FF Seats 12–13  avg $1,380/ea  total $2,760

Pairs eligible for merge (NEW below G2 min $2,800): 3

## Category 2 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 118 groups, price range $2,300 – $57,500 total
G4 fetched: 69 groups → 207 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   207 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 516 Row B Seats 4–5  avg $1,150/ea  total $2,300
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 53 groups, price range $2,070 – $27,600 total
G4 fetched: 17 groups → 51 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    51 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 623 Row A Seats 8–9  avg $1,058/ea  total $2,116
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 3 groups, price range $2,967 – $4,554 total
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
Cheapest New: Sec 750 Row P Seats 14–15  avg $1,127/ea  total $2,254

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            624 | DERIVE          |
| Cat 2    |       0.0% |         0 |            207 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             51 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

