## Category 1 — Pair Derivation Analysis
Date: July 4, 2026

G2 fetched: 131 groups, price range $1,610 – $13,800 total
G4 fetched: 37 groups → 111 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   111 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 116 Row Z Seats 1–2  avg $851/ea  total $1,702
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 4, 2026

G2 fetched: 32 groups, price range $1,311 – $3,565 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |       92.9% | May exist in G2, not top-100   |
| NEW        |     3 |        7.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 519 Row D Seats 12–13  avg $798/ea  total $1,596
Cheapest New: Sec 527 Row J Seats 5–6  avg $2,300/ea  total $4,600

## Category 3 — Pair Derivation Analysis
Date: July 4, 2026

G2 fetched: 26 groups, price range $1,265 – $5,750 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 602 Row N Seats 8–9  avg $804/ea  total $1,608
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            111 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             39 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

