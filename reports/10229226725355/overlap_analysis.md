## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 181 groups, price range $5,520 – $63,710 total
G4 fetched: 112 groups → 336 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   333 |       99.1% | May exist in G2, not top-100   |
| NEW        |     3 |        0.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 252 Row 6 Seats 18–19  avg $2,760/ea  total $5,520
Cheapest New: Sec 102 Row 10 Seats 15–16  avg $40,250/ea  total $80,500

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 53 groups, price range $4,888 – $27,600 total
G4 fetched: 34 groups → 102 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    93 |       91.2% | May exist in G2, not top-100   |
| NEW        |     9 |        8.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 342 Row 25 Seats 11–12  avg $2,542/ea  total $5,084
Cheapest New: Sec 323 Row 30 Seats 14–15  avg $2,415/ea  total $4,830

Pairs eligible for merge (NEW below G2 min $4,888): 3

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 33 groups, price range $4,255 – $23,000 total
G4 fetched: 22 groups → 66 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    63 |       95.5% | May exist in G2, not top-100   |
| NEW        |     3 |        4.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 306 Row 29 Seats 21–22  avg $2,214/ea  total $4,428
Cheapest New: Sec 307 Row 30 Seats 14–15  avg $13,556/ea  total $27,112

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 5 groups, price range $4,600 – $9,200 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       50.0% | May exist in G2, not top-100   |
| NEW        |     6 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 28 Seats 17–18  avg $2,990/ea  total $5,980
Cheapest New: Sec 356 Row 28 Seats 11–12  avg $5,232/ea  total $10,464

Pairs eligible for merge (NEW below G2 min $4,600): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            333 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |             93 | DERIVE          |
| Cat 3    |       0.0% |         3 |             63 | INVESTIGATE     |
| Cat 4    |       0.0% |         6 |              6 | DERIVE          |

Overall recommendation: **DERIVE**

