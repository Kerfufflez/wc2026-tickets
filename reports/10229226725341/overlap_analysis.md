## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 135 groups, price range $5,290 – $103,500 total
G4 fetched: 114 groups → 342 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   339 |       99.1% | May exist in G2, not top-100   |
| NEW        |     3 |        0.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 129 Row 15 Seats 19–20  avg $2,645/ea  total $5,290
Cheapest New: Sec 126 Row 30 Seats 9–10  avg $2,380/ea  total $4,760

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 45 groups, price range $4,600 – $23,000 total
G4 fetched: 35 groups → 105 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    93 |       88.6% | May exist in G2, not top-100   |
| NEW        |    12 |       11.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 323 Row 28 Seats 9–10  avg $2,415/ea  total $4,830
Cheapest New: Sec 323 Row 30 Seats 10–11  avg $2,043/ea  total $4,086

Pairs eligible for merge (NEW below G2 min $4,600): 12

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 27 groups, price range $4,485 – $17,250 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 306 Row 21 Seats 1–2  avg $2,294/ea  total $4,588
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            339 | INVESTIGATE     |
| Cat 2    |       0.0% |        12 |             93 | DERIVE          |
| Cat 3    |       0.0% |         0 |             45 | INVESTIGATE     |

Overall recommendation: **DERIVE**

