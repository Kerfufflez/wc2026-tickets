## Category 1 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 260 groups, price range $2,415 – $69,000 total
G4 fetched: 106 groups → 318 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   318 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 131 Row 32 Seats 14–15  avg $1,236/ea  total $2,472
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 188 groups, price range $1,854 – $34,500 total
G4 fetched: 77 groups → 231 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   225 |       97.4% | May exist in G2, not top-100   |
| NEW        |     6 |        2.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 203 Row 28 Seats 9–10  avg $1,173/ea  total $2,346
Cheapest New: Sec C24 Row 18 Seats 1–2  avg $23,000/ea  total $46,000

Pairs eligible for merge (NEW below G2 min $1,854): 0

## Category 3 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 91 groups, price range $1,955 – $27,140 total
G4 fetched: 22 groups → 66 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    66 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 215 Row 21 Seats 11–12  avg $1,092/ea  total $2,184
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 15 groups, price range $2,070 – $11,040 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 207 Row 29 Seats 9–10  avg $2,181/ea  total $4,362
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            318 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            225 | DERIVE          |
| Cat 3    |       0.0% |         0 |             66 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

