## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 112 groups, price range $605 – $3,335 total
G4 fetched: 121 groups → 363 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   363 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 120 Row 36 Seats 17–18  avg $330/ea  total $660
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 207 groups, price range $513 – $5,520 total
G4 fetched: 184 groups → 552 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   549 |       99.5% | May exist in G2, not top-100   |
| NEW        |     3 |        0.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 208 Row 23 Seats 18–19  avg $276/ea  total $552
Cheapest New: Sec 129 Row 23 Seats 14–15  avg $190/ea  total $380

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 191 groups, price range $448 – $15,160 total
G4 fetched: 89 groups → 267 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   261 |       97.8% | May exist in G2, not top-100   |
| NEW        |     6 |        2.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 406 Row 28 Seats 6–7  avg $229/ea  total $458
Cheapest New: Sec 416 Row 20 Seats 21–22  avg $224/ea  total $448

Pairs eligible for merge (NEW below G2 min $448): 3

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 4 groups, price range $490 – $1,725 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 422 Row 21 Seats 5–6  avg $380/ea  total $760
Cheapest New: Sec 401 Row 23 Seats 24–25  avg $1,150/ea  total $2,300

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            363 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            549 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |            261 | DERIVE          |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

