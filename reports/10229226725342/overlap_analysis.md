## Category 1 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 160 groups, price range $1,380 – $48,624 total
G4 fetched: 41 groups → 123 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   123 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 130 Row 12 Seats 5–6  avg $862/ea  total $1,724
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 97 groups, price range $1,297 – $23,000 total
G4 fetched: 31 groups → 93 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    87 |       93.5% | May exist in G2, not top-100   |
| NEW        |     6 |        6.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 344 Row 25 Seats 6–7  avg $690/ea  total $1,380
Cheapest New: Sec 305 Row 35 Seats 9–10  avg $575/ea  total $1,150

Pairs eligible for merge (NEW below G2 min $1,297): 3

## Category 3 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 65 groups, price range $1,380 – $9,556 total
G4 fetched: 19 groups → 57 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    54 |       94.7% | May exist in G2, not top-100   |
| NEW        |     3 |        5.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 314 Row 12 Seats 13–14  avg $690/ea  total $1,380
Cheapest New: Sec 310 Row 3 Seats 1–2  avg $676/ea  total $1,352

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            123 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             87 | DERIVE          |
| Cat 3    |       0.0% |         3 |             54 | INVESTIGATE     |

Overall recommendation: **DERIVE**

