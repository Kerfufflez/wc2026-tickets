## Category 1 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 124 groups, price range $1,162 – $232,184 total
G4 fetched: 69 groups → 207 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   207 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 204 Row 11 Seats 3–4  avg $1,622/ea  total $3,244
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 105 groups, price range $2,288 – $13,800 total
G4 fetched: 67 groups → 201 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   195 |       97.0% | May exist in G2, not top-100   |
| NEW        |     6 |        3.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 417 Row 24 Seats 11–12  avg $1,150/ea  total $2,300
Cheapest New: Sec 409 Row 26 Seats 5–6  avg $1,004/ea  total $2,008

Pairs eligible for merge (NEW below G2 min $2,288): 6

## Category 3 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 14 groups, price range $2,300 – $6,900 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |       70.0% | May exist in G2, not top-100   |
| NEW        |     9 |       30.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 406 Row 24 Seats 7–8  avg $1,150/ea  total $2,300
Cheapest New: Sec 402 Row 9 Seats 11–12  avg $4,600/ea  total $9,200

Pairs eligible for merge (NEW below G2 min $2,300): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            207 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            195 | DERIVE          |
| Cat 3    |       0.0% |         9 |             21 | DERIVE          |

Overall recommendation: **DERIVE**

