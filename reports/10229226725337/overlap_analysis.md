## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 112 groups, price range $2,760 – $18,400 total
G4 fetched: 41 groups → 123 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   120 |       97.6% | May exist in G2, not top-100   |
| NEW        |     3 |        2.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 146 Row E Seats 9–10  avg $1,438/ea  total $2,876
Cheapest New: Sec 109 Row D Seats 17–18  avg $11,500/ea  total $23,000

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 75 groups, price range $2,185 – $115,000 total
G4 fetched: 48 groups → 144 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   144 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 339 Row R Seats 9–10  avg $1,150/ea  total $2,300
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 14 groups, price range $2,300 – $6,900 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |       80.0% | May exist in G2, not top-100   |
| NEW        |     6 |       20.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 329 Row Z Seats 3–4  avg $1,150/ea  total $2,300
Cheapest New: Sec 304 Row U Seats 23–24  avg $3,696/ea  total $7,392

Pairs eligible for merge (NEW below G2 min $2,300): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            120 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            144 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             24 | DERIVE          |

Overall recommendation: **DERIVE**

