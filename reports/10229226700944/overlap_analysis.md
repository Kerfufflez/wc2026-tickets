## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 81 groups, price range $3,051 – $16,100 total
G4 fetched: 36 groups → 108 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   108 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 148 Row 37 Seats 1–2  avg $1,620/ea  total $3,240
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 73 groups, price range $2,472 – $11,500 total
G4 fetched: 23 groups → 69 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    63 |       91.3% | May exist in G2, not top-100   |
| NEW        |     6 |        8.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 227B Row 15 Seats 7–8  avg $1,449/ea  total $2,898
Cheapest New: Sec 333 Row 14 Seats 13–14  avg $7,188/ea  total $14,376

Pairs eligible for merge (NEW below G2 min $2,472): 0

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 33 groups, price range $2,415 – $6,900 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 324 Row 16 Seats 24–25  avg $1,265/ea  total $2,530
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 8 groups, price range $3,105 – $7,475 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 306 Row 21 Seats 13–14  avg $2,875/ea  total $5,750
Cheapest New: Sec 346 Row 22 Seats 14–15  avg $11,500/ea  total $23,000

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            108 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             63 | DERIVE          |
| Cat 3    |       0.0% |         0 |             21 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

