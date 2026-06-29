## Category 1 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 371 groups, price range $2,875 – $27,600 total
G4 fetched: 204 groups → 612 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   606 |       99.0% | May exist in G2, not top-100   |
| NEW        |     6 |        1.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 138 Row AA Seats 21–22  avg $1,640/ea  total $3,280
Cheapest New: Sec 131 Row P Seats 7–8  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $2,875): 0

## Category 2 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 102 groups, price range $2,298 – $57,500 total
G4 fetched: 65 groups → 195 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   195 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 516 Row B Seats 4–5  avg $1,380/ea  total $2,760
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 47 groups, price range $2,070 – $27,600 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 642 Row E Seats 5–6  avg $1,092/ea  total $2,184
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 3 groups, price range $2,967 – $5,074 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     3 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 750 Row P Seats 14–15  avg $1,438/ea  total $2,876

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            606 | DERIVE          |
| Cat 2    |       0.0% |         0 |            195 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             36 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

