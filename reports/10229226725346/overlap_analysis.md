## Category 1 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 321 groups, price range $3,105 – $27,600 total
G4 fetched: 161 groups → 483 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   471 |       97.5% | May exist in G2, not top-100   |
| NEW        |    12 |        2.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 330 Row Q Seats 7–8  avg $1,725/ea  total $3,450
Cheapest New: Sec 131 Row P Seats 7–8  avg $17,250/ea  total $34,500

Pairs eligible for merge (NEW below G2 min $3,105): 0

## Category 2 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 92 groups, price range $3,392 – $57,500 total
G4 fetched: 49 groups → 147 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   147 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 630 Row F Seats 1–2  avg $1,725/ea  total $3,450
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 41 groups, price range $2,990 – $27,600 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 642 Row E Seats 5–6  avg $1,552/ea  total $3,104
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 3 groups, price range $2,967 – $28,750 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 745 Row P Seats 14–15  avg $1,552/ea  total $3,104
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |        12 |            471 | DERIVE          |
| Cat 2    |       0.0% |         0 |            147 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             39 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

