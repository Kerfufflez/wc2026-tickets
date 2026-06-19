## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 110 groups, price range $5,520 – $83,950 total
G4 fetched: 50 groups → 150 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   150 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 125 Row 33 Seats 5–6  avg $2,875/ea  total $5,750
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 70 groups, price range $4,198 – $34,498 total
G4 fetched: 30 groups → 90 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    87 |       96.7% | May exist in G2, not top-100   |
| NEW        |     3 |        3.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 225 Row 6 Seats 10–11  avg $2,320/ea  total $4,640
Cheapest New: Sec 314 Row 1 Seats 11–12  avg $17,249/ea  total $34,498

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 31 groups, price range $4,140 – $11,500 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |       85.7% | May exist in G2, not top-100   |
| NEW        |     3 |       14.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 405 Row 23 Seats 20–21  avg $2,185/ea  total $4,370
Cheapest New: Sec 421 Row 20 Seats 11–12  avg $2,069/ea  total $4,138

## Category 4 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 1 groups, price range $5,750 – $5,750 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     3 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 401 Row 18 Seats 23–24  avg $11,500/ea  total $23,000

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            150 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             87 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             18 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **PARTIAL**

