## Category 1 — Pair Derivation Analysis
Date: July 5, 2026

G2 fetched: 201 groups, price range $3,450 – $34,500 total
G4 fetched: 81 groups → 243 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   240 |       98.8% | May exist in G2, not top-100   |
| NEW        |     3 |        1.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 217 Row 14 Seats 13–14  avg $2,012/ea  total $4,024
Cheapest New: Sec 146 Row 12 Seats 1–2  avg $28,750/ea  total $57,500

## Category 2 — Pair Derivation Analysis
Date: July 5, 2026

G2 fetched: 173 groups, price range $2,288 – $27,600 total
G4 fetched: 71 groups → 213 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   207 |       97.2% | May exist in G2, not top-100   |
| NEW        |     6 |        2.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 415 Row 15 Seats 9–10  avg $1,438/ea  total $2,876
Cheapest New: Sec 438 Row 4 Seats 9–10  avg $17,250/ea  total $34,500

Pairs eligible for merge (NEW below G2 min $2,288): 0

## Category 3 — Pair Derivation Analysis
Date: July 5, 2026

G2 fetched: 26 groups, price range $2,640 – $10,925 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 432 Row 19 Seats 15–16  avg $1,320/ea  total $2,640
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            240 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            207 | DERIVE          |
| Cat 3    |       0.0% |         0 |             24 | INVESTIGATE     |

Overall recommendation: **DERIVE**

