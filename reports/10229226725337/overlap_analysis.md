## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 111 groups, price range $2,760 – $18,400 total
G4 fetched: 51 groups → 153 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   150 |       98.0% | May exist in G2, not top-100   |
| NEW        |     3 |        2.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 118 Row NN Seats 9–10  avg $1,495/ea  total $2,990
Cheapest New: Sec 109 Row D Seats 17–18  avg $11,500/ea  total $23,000

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 83 groups, price range $2,185 – $115,000 total
G4 fetched: 52 groups → 156 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   156 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 306 Row U Seats 4–5  avg $1,204/ea  total $2,408
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 16 groups, price range $2,300 – $5,750 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |       75.0% | May exist in G2, not top-100   |
| NEW        |     9 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 304 Row CC Seats 23–24  avg $1,353/ea  total $2,706
Cheapest New: Sec 328 Row BB Seats 36–37  avg $1,121/ea  total $2,242

Pairs eligible for merge (NEW below G2 min $2,300): 3

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            150 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            156 | INVESTIGATE     |
| Cat 3    |       0.0% |         9 |             27 | DERIVE          |

Overall recommendation: **DERIVE**

