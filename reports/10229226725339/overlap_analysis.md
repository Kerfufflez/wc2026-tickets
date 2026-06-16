## Category 1 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 109 groups, price range $3,174 – $230,000 total
G4 fetched: 61 groups → 183 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   183 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 240 Row 4 Seats 9–10  avg $1,725/ea  total $3,450
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 129 groups, price range $2,645 – $18,998 total
G4 fetched: 102 groups → 306 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   300 |       98.0% | May exist in G2, not top-100   |
| NEW        |     6 |        2.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 512 Row 13 Seats 3–4  avg $1,380/ea  total $2,760
Cheapest New: Sec 511 Row 7 Seats 11–12  avg $11,500/ea  total $23,000

Pairs eligible for merge (NEW below G2 min $2,645): 0

## Category 3 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 20 groups, price range $2,530 – $15,410 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 549 Row 20 Seats 1–2  avg $1,380/ea  total $2,760
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            183 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            300 | DERIVE          |
| Cat 3    |       0.0% |         0 |             27 | INVESTIGATE     |

Overall recommendation: **DERIVE**

