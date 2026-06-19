## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 37 groups, price range $6,900 – $23,000 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 121 Row 21 Seats 17–18  avg $3,738/ea  total $7,476
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 7 groups, price range $5,658 – $9,430 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |       87.5% | May exist in G2, not top-100   |
| NEW        |     3 |       12.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 404 Row 4 Seats 1–2  avg $2,898/ea  total $5,796
Cheapest New: Sec 433 Row 2 Seats 5–6  avg $6,135/ea  total $12,270

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 2 groups, price range $6,900 – $103,500 total
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
Cheapest New: Sec 422 Row 16 Seats 10–11  avg $1,062,600/ea  total $2,125,200

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             24 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             21 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **PARTIAL**

