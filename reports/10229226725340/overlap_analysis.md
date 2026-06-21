## Category 1 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 161 groups, price range $2,670 – $153,332 total
G4 fetched: 68 groups → 204 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   201 |       98.5% | May exist in G2, not top-100   |
| NEW        |     3 |        1.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 224 Row KK Seats 105–106  avg $1,380/ea  total $2,760
Cheapest New: Sec 203 Row P Seats 3–4  avg $1,322/ea  total $2,644

## Category 2 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 104 groups, price range $1,971 – $24,380 total
G4 fetched: 40 groups → 120 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   117 |       97.5% | May exist in G2, not top-100   |
| NEW        |     3 |        2.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 408 Row WW Seats 5–6  avg $1,121/ea  total $2,242
Cheapest New: Sec 420 Row WW Seats 1–2  avg $59,144/ea  total $118,288

## Category 3 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 18 groups, price range $2,464 – $8,214 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |       66.7% | May exist in G2, not top-100   |
| NEW        |     9 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 454 Row PP Seats 104–105  avg $1,396/ea  total $2,792
Cheapest New: Sec 428 Row C Seats 8–9  avg $1,232/ea  total $2,464

Pairs eligible for merge (NEW below G2 min $2,464): 9

## Category 4 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 3 groups, price range $2,136 – $3,793 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 427 Row YY Seats 2–3  avg $1,725/ea  total $3,450
Cheapest New: Sec 452 Row XX Seats 101–102  avg $2,464/ea  total $4,928

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            201 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            117 | INVESTIGATE     |
| Cat 3    |       0.0% |         9 |             18 | DERIVE          |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

