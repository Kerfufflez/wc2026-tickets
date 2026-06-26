## Category 1 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 148 groups, price range $4,347 – $46,000 total
G4 fetched: 124 groups → 372 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   369 |       99.2% | May exist in G2, not top-100   |
| NEW        |     3 |        0.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 149 Row 25 Seats 13–14  avg $2,185/ea  total $4,370
Cheapest New: Sec 123 Row 42 Seats 27–28  avg $2,130/ea  total $4,260

## Category 2 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 210 groups, price range $2,840 – $575,000 total
G4 fetched: 90 groups → 270 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   270 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 334 Row 21 Seats 8–9  avg $1,586/ea  total $3,172
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 62 groups, price range $2,760 – $20,442 total
G4 fetched: 38 groups → 114 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   111 |       97.4% | May exist in G2, not top-100   |
| NEW        |     3 |        2.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 307 Row 18 Seats 17–18  avg $1,495/ea  total $2,990
Cheapest New: Sec 306 Row 11 Seats 7–8  avg $1,334/ea  total $2,668

## Category 4 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 7 groups, price range $1,840 – $11,500 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 346 Row 22 Seats 6–7  avg $1,978/ea  total $3,956
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            369 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            270 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |            111 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

