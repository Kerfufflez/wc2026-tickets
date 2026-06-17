## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 89 groups, price range $2,875 – $57,730 total
G4 fetched: 47 groups → 141 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   141 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 121 Row 37 Seats 5–6  avg $1,610/ea  total $3,220
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 77 groups, price range $2,070 – $13,800 total
G4 fetched: 53 groups → 159 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   153 |       96.2% | May exist in G2, not top-100   |
| NEW        |     6 |        3.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 309 Row 26 Seats 21–22  avg $1,150/ea  total $2,300
Cheapest New: Sec 315 Row 20 Seats 13–14  avg $987/ea  total $1,974

Pairs eligible for merge (NEW below G2 min $2,070): 3

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 41 groups, price range $2,139 – $690,000 total
G4 fetched: 37 groups → 111 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   108 |       97.3% | May exist in G2, not top-100   |
| NEW        |     3 |        2.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 316 Row 21 Seats 21–22  avg $1,133/ea  total $2,266
Cheapest New: Sec 302 Row 11 Seats 11–12  avg $1,035/ea  total $2,070

## Category 4 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 2 groups, price range $2,300 – $3,910 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 313 Row 28 Seats 15–16  avg $1,380/ea  total $2,760
Cheapest New: Sec 312 Row 29 Seats 13–14  avg $2,242/ea  total $4,484

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            141 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            153 | DERIVE          |
| Cat 3    |       0.0% |         3 |            108 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

