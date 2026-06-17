## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 134 groups, price range $2,205 – $22,678 total
G4 fetched: 75 groups → 225 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   222 |       98.7% | May exist in G2, not top-100   |
| NEW        |     3 |        1.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 243 Row 4 Seats 12–13  avg $1,380/ea  total $2,760
Cheapest New: Sec 227 Row 2 Seats 1–2  avg $17,250/ea  total $34,500

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 137 groups, price range $1,840 – $966,000 total
G4 fetched: 75 groups → 225 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   219 |       97.3% | May exist in G2, not top-100   |
| NEW        |     6 |        2.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 408 Row 24 Seats 1–2  avg $920/ea  total $1,840
Cheapest New: Sec 417 Row 10 Seats 10–11  avg $914/ea  total $1,828

Pairs eligible for merge (NEW below G2 min $1,840): 6

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 25 groups, price range $1,840 – $13,800 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 405 Row 14 Seats 13–14  avg $1,092/ea  total $2,184
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            222 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            219 | DERIVE          |
| Cat 3    |       0.0% |         0 |             33 | INVESTIGATE     |

Overall recommendation: **DERIVE**

