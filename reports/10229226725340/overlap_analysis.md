## Category 1 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 210 groups, price range $1,625 – $153,332 total
G4 fetched: 78 groups → 234 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   234 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 219 Row UU Seats 103–104  avg $813/ea  total $1,626
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 121 groups, price range $1,527 – $24,380 total
G4 fetched: 39 groups → 117 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   117 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 435 Row VV Seats 105–106  avg $792/ea  total $1,584
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 48 groups, price range $1,836 – $11,222 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |       86.7% | May exist in G2, not top-100   |
| NEW        |     6 |       13.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 402 Row RR Seats 4–5  avg $972/ea  total $1,944
Cheapest New: Sec 433 Row ZZ Seats 6–7  avg $774/ea  total $1,548

Pairs eligible for merge (NEW below G2 min $1,836): 6

## Category 4 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 3 groups, price range $2,530 – $6,501 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 427 Row YY Seats 2–3  avg $1,725/ea  total $3,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            234 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            117 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             39 | DERIVE          |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

