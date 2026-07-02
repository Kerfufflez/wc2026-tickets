## Category 1 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 229 groups, price range $1,838 – $48,624 total
G4 fetched: 81 groups → 243 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   237 |       97.5% | May exist in G2, not top-100   |
| NEW        |     6 |        2.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 129 Row 24 Seats 9–10  avg $972/ea  total $1,944
Cheapest New: Sec 108 Row 22 Seats 12–13  avg $897/ea  total $1,794

Pairs eligible for merge (NEW below G2 min $1,838): 3

## Category 2 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 139 groups, price range $1,449 – $23,000 total
G4 fetched: 45 groups → 135 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   132 |       97.8% | May exist in G2, not top-100   |
| NEW        |     3 |        2.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 305 Row 5 Seats 1–2  avg $805/ea  total $1,610
Cheapest New: Sec 301 Row 34 Seats 5–6  avg $13,800/ea  total $27,600

## Category 3 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 106 groups, price range $1,495 – $9,556 total
G4 fetched: 30 groups → 90 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    87 |       96.7% | May exist in G2, not top-100   |
| NEW        |     3 |        3.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 309 Row 18 Seats 4–5  avg $850/ea  total $1,700
Cheapest New: Sec 330 Row 38 Seats 1–2  avg $5,750/ea  total $11,500

## Category 4 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 2 groups, price range $1,955 – $2,875 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 330 Row 43 Seats 9–10  avg $1,380/ea  total $2,760
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            237 | DERIVE          |
| Cat 2    |       0.0% |         3 |            132 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             87 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

