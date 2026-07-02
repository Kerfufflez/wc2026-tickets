## Category 1 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 41 groups, price range $10,350 – $44,850 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       80.0% | May exist in G2, not top-100   |
| NEW        |     3 |       20.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 462 Row 4 Seats 1–2  avg $7,475/ea  total $14,950
Cheapest New: Sec 467 Row 1 Seats 1–2  avg $35,649/ea  total $71,298

## Category 2 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 17 groups, price range $10,695 – $69,000 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 550 Row 11 Seats 1–2  avg $7,026/ea  total $14,052
Cheapest New: Sec 535 Row 4 Seats 5–6  avg $5,268/ea  total $10,536

## Category 3 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 16 groups, price range $8,050 – $17,250 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 664 Row 2 Seats 6–7  avg $5,520/ea  total $11,040
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 4 groups, price range $10,350 – $22,857 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 619 Row 7 Seats 5–6  avg $5,253/ea  total $10,506
Cheapest New: Sec 619 Row 5 Seats 8–9  avg $4,833/ea  total $9,666

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             12 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |              9 | SKIP            |
| Cat 3    |       0.0% |         0 |             15 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

