## Category 1 — Pair Derivation Analysis
Date: June 5, 2026

G2 fetched: 85 groups, price range $7,406 – $832,715 total
G4 fetched: 26 groups → 78 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    78 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 39 Seats 11–12  avg $5,034/ea  total $10,068
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 5, 2026

G2 fetched: 161 groups, price range $6,382 – $1,328,250 total
G4 fetched: 55 groups → 165 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   162 |       98.2% | May exist in G2, not top-100   |
| NEW        |     3 |        1.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 312 Row 14 Seats 21–22  avg $3,508/ea  total $7,016
Cheapest New: Sec 201 Row 7 Seats 1–2  avg $2,904/ea  total $5,808

## Category 3 — Pair Derivation Analysis
Date: June 5, 2026

G2 fetched: 134 groups, price range $4,807 – $87,435 total
G4 fetched: 68 groups → 204 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   204 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 328 Row 11 Seats 21–22  avg $2,415/ea  total $4,830
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             78 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            162 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |            204 | INVESTIGATE     |

Overall recommendation: **PARTIAL**

Prior per-category fetch note: Cat 1 previously showed only 2 G2 listings under a shared 100-slot query; dedicated Cat 1 G2 fetch now returns 85 groups, which may materially change overlap vs older combined-query estimates.
