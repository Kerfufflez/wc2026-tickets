## Category 1 — Pair Derivation Analysis
Date: July 6, 2026

G2 fetched: 75 groups, price range $3,910 – $22,540 total
G4 fetched: 23 groups → 69 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    69 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 118 Row NN Seats 5–6  avg $2,266/ea  total $4,532
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 6, 2026

G2 fetched: 79 groups, price range $3,105 – $27,140 total
G4 fetched: 29 groups → 87 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |       93.1% | May exist in G2, not top-100   |
| NEW        |     6 |        6.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 310 Row RR Seats 9–10  avg $1,983/ea  total $3,966
Cheapest New: Sec 311 Row SS Seats 2–3  avg $1,495/ea  total $2,990

Pairs eligible for merge (NEW below G2 min $3,105): 3

## Category 3 — Pair Derivation Analysis
Date: July 6, 2026

G2 fetched: 34 groups, price range $2,298 – $115,000 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 301 Row Q Seats 4–5  avg $1,725/ea  total $3,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             69 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             81 | DERIVE          |
| Cat 3    |       0.0% |         0 |             15 | INVESTIGATE     |

Overall recommendation: **DERIVE**

