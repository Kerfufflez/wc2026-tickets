## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 108 groups, price range $5,744 – $39,100 total
G4 fetched: 81 groups → 243 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   234 |       96.3% | May exist in G2, not top-100   |
| NEW        |     9 |        3.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 131 Row 22 Seats 5–6  avg $3,161/ea  total $6,322
Cheapest New: Sec 106 Row 19 Seats 10–11  avg $2,790/ea  total $5,580

Pairs eligible for merge (NEW below G2 min $5,744): 3

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 154 groups, price range $4,485 – $43,470 total
G4 fetched: 75 groups → 225 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   225 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 228B Row 7 Seats 19–20  avg $2,300/ea  total $4,600
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 56 groups, price range $4,368 – $23,000 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    72 |       88.9% | May exist in G2, not top-100   |
| NEW        |     9 |       11.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 324 Row 10 Seats 3–4  avg $2,185/ea  total $4,370
Cheapest New: Sec 305 Row 19 Seats 25–26  avg $2,179/ea  total $4,358

Pairs eligible for merge (NEW below G2 min $4,368): 3

## Category 4 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 4 groups, price range $5,744 – $44,850 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 346 Row 26 Seats 8–9  avg $2,961/ea  total $5,922
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            234 | DERIVE          |
| Cat 2    |       0.0% |         0 |            225 | INVESTIGATE     |
| Cat 3    |       0.0% |         9 |             72 | DERIVE          |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

