## Category 1 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 169 groups, price range $2,209 – $153,332 total
G4 fetched: 68 groups → 204 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   204 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 203 Row P Seats 3–4  avg $1,322/ea  total $2,644
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 103 groups, price range $2,070 – $24,380 total
G4 fetched: 40 groups → 120 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   114 |       95.0% | May exist in G2, not top-100   |
| NEW        |     6 |        5.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 421 Row PP Seats 101–102  avg $1,087/ea  total $2,174
Cheapest New: Sec 420 Row HH Seats 102–103  avg $1,027/ea  total $2,054

Pairs eligible for merge (NEW below G2 min $2,070): 3

## Category 3 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 27 groups, price range $2,136 – $8,214 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 449 Row JJ Seats 106–107  avg $1,068/ea  total $2,136
Cheapest New: —

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
| Cat 1    |       0.0% |         0 |            204 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            114 | DERIVE          |
| Cat 3    |       0.0% |         0 |             39 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

