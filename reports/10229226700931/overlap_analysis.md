## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 35 groups, price range $5,812 – $23,000 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 125 Row 21 Seats 15–16  avg $4,399/ea  total $8,798
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 11 groups, price range $5,252 – $12,095 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       66.7% | May exist in G2, not top-100   |
| NEW        |     6 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 444 Row 14 Seats 19–20  avg $3,680/ea  total $7,360
Cheapest New: Sec 453 Row 1 Seats 9–10  avg $1,839/ea  total $3,678

Pairs eligible for merge (NEW below G2 min $5,252): 3

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             33 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             12 | DERIVE          |

Overall recommendation: **DERIVE**

