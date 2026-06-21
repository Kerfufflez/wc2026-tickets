## Category 1 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 181 groups, price range $4,107 – $81,980 total
G4 fetched: 70 groups → 210 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   204 |       97.1% | May exist in G2, not top-100   |
| NEW        |     6 |        2.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 248 Row NN Seats 5–6  avg $2,158/ea  total $4,316
Cheapest New: Sec 224 Row FF Seats 5–6  avg $76,666/ea  total $153,332

Pairs eligible for merge (NEW below G2 min $4,107): 0

## Category 2 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 121 groups, price range $3,450 – $19,348 total
G4 fetched: 35 groups → 105 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   102 |       97.1% | May exist in G2, not top-100   |
| NEW        |     3 |        2.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 407 Row MM Seats 1–2  avg $1,807/ea  total $3,614
Cheapest New: Sec 440 Row PP Seats 8–9  avg $11,488/ea  total $22,976

## Category 3 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 23 groups, price range $3,866 – $24,643 total
G4 fetched: 17 groups → 51 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |       88.2% | May exist in G2, not top-100   |
| NEW        |     6 |       11.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 426 Row NN Seats 3–4  avg $2,054/ea  total $4,108
Cheapest New: Sec 454 Row NN Seats 102–103  avg $1,803/ea  total $3,606

Pairs eligible for merge (NEW below G2 min $3,866): 6

## Category 4 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 4 groups, price range $4,140 – $10,027 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 428 Row ZZ Seats 1–2  avg $2,271/ea  total $4,542
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            204 | DERIVE          |
| Cat 2    |       0.0% |         3 |            102 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             45 | DERIVE          |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

