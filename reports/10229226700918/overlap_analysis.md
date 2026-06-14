## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 70 groups, price range $1,378 – $16,100 total
G4 fetched: 55 groups → 165 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   165 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 123 Row 15 Seats 5–6  avg $824/ea  total $1,648
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 55 groups, price range $1,484 – $4,140 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    78 |       96.3% | May exist in G2, not top-100   |
| NEW        |     3 |        3.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 305 Row 14 Seats 5–6  avg $757/ea  total $1,514
Cheapest New: Sec 305 Row 13 Seats 17–18  avg $2,300/ea  total $4,600

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 9 groups, price range $1,438 – $2,956 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 338 Row 24 Seats 13–14  avg $862/ea  total $1,724
Cheapest New: Sec 326 Row 22 Seats 4–5  avg $1,725/ea  total $3,450

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            165 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             78 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

