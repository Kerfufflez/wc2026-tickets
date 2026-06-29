## Category 1 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 169 groups, price range $1,380 – $11,500 total
G4 fetched: 62 groups → 186 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   186 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec CL6 Row 4 Seats 5–6  avg $794/ea  total $1,588
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 117 groups, price range $1,058 – $10,384 total
G4 fetched: 56 groups → 168 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   165 |       98.2% | May exist in G2, not top-100   |
| NEW        |     3 |        1.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 340 Row 4 Seats 15–16  avg $575/ea  total $1,150
Cheapest New: Sec 314 Row 10 Seats 16–17  avg $518/ea  total $1,036

## Category 3 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 13 groups, price range $1,150 – $2,760 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 316 Row 16 Seats 13–14  avg $676/ea  total $1,352
Cheapest New: Sec 304 Row 24 Seats 10–11  avg $2,185/ea  total $4,370

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            186 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            165 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

