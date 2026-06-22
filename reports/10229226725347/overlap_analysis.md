## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 104 groups, price range $6,440 – $39,100 total
G4 fetched: 75 groups → 225 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   222 |       98.7% | May exist in G2, not top-100   |
| NEW        |     3 |        1.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 129 Row 23 Seats 10–11  avg $3,220/ea  total $6,440
Cheapest New: Sec 104 Row 43 Seats 17–18  avg $401,350/ea  total $802,700

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 143 groups, price range $4,600 – $43,470 total
G4 fetched: 75 groups → 225 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   225 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 318 Row 24 Seats 25–26  avg $2,300/ea  total $4,600
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 46 groups, price range $4,600 – $23,000 total
G4 fetched: 26 groups → 78 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    72 |       92.3% | May exist in G2, not top-100   |
| NEW        |     6 |        7.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 307 Row 25 Seats 27–28  avg $2,300/ea  total $4,600
Cheapest New: Sec 350 Row 14 Seats 4–5  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $4,600): 0

## Category 4 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 2 groups, price range $11,500 – $44,850 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     6 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 346 Row 26 Seats 8–9  avg $2,961/ea  total $5,922

Pairs eligible for merge (NEW below G2 min $11,500): 6

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            222 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            225 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             72 | DERIVE          |
| Cat 4    |       0.0% |         6 |              0 | DERIVE          |

Overall recommendation: **DERIVE**

