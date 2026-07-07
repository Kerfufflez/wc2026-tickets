## Category 1 — Pair Derivation Analysis
Date: July 7, 2026

G2 fetched: 219 groups, price range $4,998 – $68,998 total
G4 fetched: 75 groups → 225 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   219 |       97.3% | May exist in G2, not top-100   |
| NEW        |     6 |        2.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 208 Row 9 Seats 1–2  avg $2,702/ea  total $5,404
Cheapest New: Sec 202 Row 18 Seats 5–6  avg $2,041/ea  total $4,082

Pairs eligible for merge (NEW below G2 min $4,998): 3

## Category 2 — Pair Derivation Analysis
Date: July 7, 2026

G2 fetched: 298 groups, price range $2,806 – $49,094 total
G4 fetched: 137 groups → 411 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   411 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 511 Row 15 Seats 2–3  avg $1,525/ea  total $3,050
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 7, 2026

G2 fetched: 94 groups, price range $3,450 – $46,000 total
G4 fetched: 26 groups → 78 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    75 |       96.2% | May exist in G2, not top-100   |
| NEW        |     3 |        3.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 531 Row 17 Seats 1–2  avg $1,840/ea  total $3,680
Cheapest New: Sec 547 Row 11 Seats 12–13  avg $1,610/ea  total $3,220

## Category 4 — Pair Derivation Analysis
Date: July 7, 2026

G2 fetched: 6 groups, price range $6,325 – $19,550 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 553 Row 13 Seats 10–11  avg $5,750/ea  total $11,500
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            219 | DERIVE          |
| Cat 2    |       0.0% |         0 |            411 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             75 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

