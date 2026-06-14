## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 141 groups, price range $4,945 – $103,500 total
G4 fetched: 121 groups → 363 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   360 |       99.2% | May exist in G2, not top-100   |
| NEW        |     3 |        0.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 129 Row 15 Seats 19–20  avg $2,645/ea  total $5,290
Cheapest New: Sec 126 Row 30 Seats 9–10  avg $2,380/ea  total $4,760

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 48 groups, price range $4,600 – $1,356,391 total
G4 fetched: 40 groups → 120 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   108 |       90.0% | May exist in G2, not top-100   |
| NEW        |    12 |       10.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 351 Row 24 Seats 23–24  avg $2,300/ea  total $4,600
Cheapest New: Sec 323 Row 30 Seats 10–11  avg $2,043/ea  total $4,086

Pairs eligible for merge (NEW below G2 min $4,600): 12

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 29 groups, price range $4,485 – $17,250 total
G4 fetched: 16 groups → 48 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    48 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 306 Row 21 Seats 1–2  avg $2,294/ea  total $4,588
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 6 groups, price range $5,750 – $11,500 total
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
Cheapest New: Sec 336 Row 30 Seats 5–6  avg $7,475/ea  total $14,950

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            360 | INVESTIGATE     |
| Cat 2    |       0.0% |        12 |            108 | DERIVE          |
| Cat 3    |       0.0% |         0 |             48 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

