## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 127 groups, price range $3,335 – $75,900 total
G4 fetched: 74 groups → 222 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   219 |       98.6% | May exist in G2, not top-100   |
| NEW        |     3 |        1.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 133 Row 36 Seats 16–17  avg $1,840/ea  total $3,680
Cheapest New: Sec 122 Row 35 Seats 34–35  avg $1,627/ea  total $3,254

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 91 groups, price range $2,300 – $27,600 total
G4 fetched: 63 groups → 189 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   183 |       96.8% | May exist in G2, not top-100   |
| NEW        |     6 |        3.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 309 Row 23 Seats 9–10  avg $1,450/ea  total $2,900
Cheapest New: Sec 336 Row 26 Seats 13–14  avg $1,121/ea  total $2,242

Pairs eligible for merge (NEW below G2 min $2,300): 3

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 76 groups, price range $2,298 – $12,650 total
G4 fetched: 40 groups → 120 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   117 |       97.5% | May exist in G2, not top-100   |
| NEW        |     3 |        2.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 327 Row 10 Seats 9–10  avg $1,265/ea  total $2,530
Cheapest New: Sec 319 Row 22 Seats 10–11  avg $6,899/ea  total $13,798

## Category 4 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 7 groups, price range $2,760 – $5,750 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 311 Row 34 Seats 22–23  avg $1,552/ea  total $3,104
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            219 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            183 | DERIVE          |
| Cat 3    |       0.0% |         3 |            117 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

