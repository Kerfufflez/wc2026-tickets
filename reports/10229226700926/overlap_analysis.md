## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 37 groups, price range $2,314 – $121,900 total
G4 fetched: 17 groups → 51 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    48 |       94.1% | May exist in G2, not top-100   |
| NEW        |     3 |        5.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 135 Row 28 Seats 12–13  avg $1,438/ea  total $2,876
Cheapest New: Sec 101 Row 25 Seats 5–6  avg $75,786/ea  total $151,572

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 19 groups, price range $2,390 – $5,980 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 226 Row 5 Seats 21–22  avg $1,495/ea  total $2,990
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 35 groups, price range $2,070 – $20,442 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       80.0% | May exist in G2, not top-100   |
| NEW        |     3 |       20.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 347 Row 9 Seats 1–2  avg $1,150/ea  total $2,300
Cheapest New: Sec 302 Row 15 Seats 4–5  avg $1,034/ea  total $2,068

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             48 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |              9 | SKIP            |
| Cat 3    |       0.0% |         3 |             12 | INVESTIGATE     |

Overall recommendation: **PARTIAL**

