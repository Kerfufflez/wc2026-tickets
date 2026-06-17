## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 127 groups, price range $920 – $11,500 total
G4 fetched: 88 groups → 264 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   264 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 106 Row 19 Seats 7–8  avg $500/ea  total $1,000
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 127 groups, price range $794 – $2,760 total
G4 fetched: 66 groups → 198 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   192 |       97.0% | May exist in G2, not top-100   |
| NEW        |     6 |        3.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 304 Row 37 Seats 13–14  avg $402/ea  total $804
Cheapest New: Sec 205 Row 6 Seats 17–18  avg $1,610/ea  total $3,220

Pairs eligible for merge (NEW below G2 min $794): 0

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 38 groups, price range $506 – $2,298 total
G4 fetched: 19 groups → 57 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    57 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 331 Row 17 Seats 17–18  avg $397/ea  total $794
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            264 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            192 | DERIVE          |
| Cat 3    |       0.0% |         0 |             57 | INVESTIGATE     |

Overall recommendation: **DERIVE**

