## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 111 groups, price range $5,520 – $83,950 total
G4 fetched: 54 groups → 162 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   159 |       98.1% | May exist in G2, not top-100   |
| NEW        |     3 |        1.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 128 Row 24 Seats 5–6  avg $2,760/ea  total $5,520
Cheapest New: Sec 132 Row 33 Seats 18–19  avg $2,737/ea  total $5,474

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 72 groups, price range $4,198 – $34,498 total
G4 fetched: 31 groups → 93 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    90 |       96.8% | May exist in G2, not top-100   |
| NEW        |     3 |        3.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 319 Row 2 Seats 9–10  avg $2,300/ea  total $4,600
Cheapest New: Sec 314 Row 1 Seats 11–12  avg $17,249/ea  total $34,498

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 31 groups, price range $4,025 – $11,500 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |       87.5% | May exist in G2, not top-100   |
| NEW        |     3 |       12.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 405 Row 23 Seats 20–21  avg $2,185/ea  total $4,370
Cheapest New: Sec 404 Row 24 Seats 5–6  avg $2,012/ea  total $4,024

## Category 4 — Pair Derivation Analysis
Date: June 18, 2026

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
Cheapest New: Sec 401 Row 18 Seats 23–24  avg $3,450/ea  total $6,900

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            159 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             90 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             21 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **PARTIAL**

