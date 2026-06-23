## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 131 groups, price range $8,740 – $1,150,000 total
G4 fetched: 86 groups → 258 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   258 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 130 Row 19 Seats 1–2  avg $4,600/ea  total $9,200
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 32 groups, price range $7,820 – $46,000 total
G4 fetched: 24 groups → 72 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    66 |       91.7% | May exist in G2, not top-100   |
| NEW        |     6 |        8.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 343 Row 30 Seats 10–11  avg $3,974/ea  total $7,948
Cheapest New: Sec 312 Row 12 Seats 13–14  avg $3,781/ea  total $7,562

Pairs eligible for merge (NEW below G2 min $7,820): 3

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 23 groups, price range $7,883 – $32,200 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |       90.0% | May exist in G2, not top-100   |
| NEW        |     3 |       10.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 333 Row 19 Seats 17–18  avg $4,025/ea  total $8,050
Cheapest New: Sec 331 Row 21 Seats 17–18  avg $3,833/ea  total $7,666

## Category 4 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 2 groups, price range $9,200 – $9,200 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     9 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 356 Row 28 Seats 11–12  avg $5,232/ea  total $10,464

Pairs eligible for merge (NEW below G2 min $9,200): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            258 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             66 | DERIVE          |
| Cat 3    |       0.0% |         3 |             27 | INVESTIGATE     |
| Cat 4    |       0.0% |         9 |              0 | DERIVE          |

Overall recommendation: **DERIVE**

