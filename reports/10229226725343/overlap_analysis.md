## Category 1 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 318 groups, price range $1,840 – $22,678 total
G4 fetched: 216 groups → 648 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   645 |       99.5% | May exist in G2, not top-100   |
| NEW        |     3 |        0.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 215 Row 7 Seats 9–10  avg $989/ea  total $1,978
Cheapest New: Sec 220 Row 10 Seats 7–8  avg $114,999/ea  total $229,998

## Category 2 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 239 groups, price range $1,426 – $23,000 total
G4 fetched: 159 groups → 477 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   468 |       98.1% | May exist in G2, not top-100   |
| NEW        |     9 |        1.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 437 Row 13 Seats 9–10  avg $730/ea  total $1,460
Cheapest New: Sec 408 Row 23 Seats 19–20  avg $678/ea  total $1,356

Pairs eligible for merge (NEW below G2 min $1,426): 9

## Category 3 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 55 groups, price range $1,610 – $13,800 total
G4 fetched: 21 groups → 63 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    60 |       95.2% | May exist in G2, not top-100   |
| NEW        |     3 |        4.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 421 Row 24 Seats 1–2  avg $805/ea  total $1,610
Cheapest New: Sec 449 Row 26 Seats 5–6  avg $728/ea  total $1,456

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            645 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |            468 | DERIVE          |
| Cat 3    |       0.0% |         3 |             60 | INVESTIGATE     |

Overall recommendation: **DERIVE**

