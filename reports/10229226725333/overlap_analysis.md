## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 142 groups, price range $3,260 – $103,500 total
G4 fetched: 86 groups → 258 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   255 |       98.8% | May exist in G2, not top-100   |
| NEW        |     3 |        1.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 226 Row 4 Seats 13–14  avg $1,725/ea  total $3,450
Cheapest New: Sec 226 Row 10 Seats 17–18  avg $114,999/ea  total $229,998

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 128 groups, price range $2,300 – $23,000 total
G4 fetched: 76 groups → 228 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   228 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 439 Row 13 Seats 15–16  avg $1,150/ea  total $2,300
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 15 groups, price range $2,530 – $6,923 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |       71.4% | May exist in G2, not top-100   |
| NEW        |     6 |       28.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 434 Row 21 Seats 7–8  avg $1,354/ea  total $2,708
Cheapest New: Sec 404 Row 19 Seats 7–8  avg $5,520/ea  total $11,040

Pairs eligible for merge (NEW below G2 min $2,530): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            255 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            228 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             15 | DERIVE          |

Overall recommendation: **DERIVE**

