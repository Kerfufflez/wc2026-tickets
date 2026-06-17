## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 96 groups, price range $794 – $10,350 total
G4 fetched: 129 groups → 387 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   381 |       98.4% | May exist in G2, not top-100   |
| NEW        |     6 |        1.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 111 Row 12 Seats 13–14  avg $400/ea  total $800
Cheapest New: Sec 111 Row 15 Seats 25–26  avg $343/ea  total $686

Pairs eligible for merge (NEW below G2 min $794): 6

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 155 groups, price range $656 – $4,600 total
G4 fetched: 99 groups → 297 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   291 |       98.0% | May exist in G2, not top-100   |
| NEW        |     6 |        2.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec NE-T-2 Row 2 Seats 25–26  avg $345/ea  total $690
Cheapest New: Sec C26 Row 1 Seats 17–18  avg $2,414/ea  total $4,828

Pairs eligible for merge (NEW below G2 min $656): 0

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 39 groups, price range $632 – $3,565 total
G4 fetched: 25 groups → 75 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    72 |       96.0% | May exist in G2, not top-100   |
| NEW        |     3 |        4.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 215 Row 19 Seats 18–19  avg $322/ea  total $644
Cheapest New: Sec 218 Row 11 Seats 1–2  avg $2,300/ea  total $4,600

## Category 4 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 7 groups, price range $632 – $1,228 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 239 Row 27 Seats 17–18  avg $401/ea  total $802
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            381 | DERIVE          |
| Cat 2    |       0.0% |         6 |            291 | DERIVE          |
| Cat 3    |       0.0% |         3 |             72 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

