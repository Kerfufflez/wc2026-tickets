## Category 1 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 152 groups, price range $9,200 – $92,000 total
G4 fetched: 97 groups → 291 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   288 |       99.0% | May exist in G2, not top-100   |
| NEW        |     3 |        1.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 134 Row 29 Seats 18–19  avg $4,916/ea  total $9,832
Cheapest New: Sec 239CC Row 1 Seats 13–14  avg $4,428/ea  total $8,856

## Category 2 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 53 groups, price range $7,958 – $57,500 total
G4 fetched: 25 groups → 75 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    72 |       96.0% | May exist in G2, not top-100   |
| NEW        |     3 |        4.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 344 Row 27 Seats 10–11  avg $4,255/ea  total $8,510
Cheapest New: Sec 343 Row 30 Seats 10–11  avg $3,919/ea  total $7,838

## Category 3 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 35 groups, price range $6,849 – $32,200 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 333 Row 30 Seats 14–15  avg $4,025/ea  total $8,050
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 6 groups, price range $9,200 – $14,626 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 356 Row 28 Seats 11–12  avg $5,232/ea  total $10,464
Cheapest New: Sec 328 Row 24 Seats 13–14  avg $17,250/ea  total $34,500

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            288 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             72 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             24 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

