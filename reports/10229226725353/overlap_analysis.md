## Category 1 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 175 groups, price range $7,475 – $129,030 total
G4 fetched: 62 groups → 186 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   186 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 15 Seats 9–10  avg $4,025/ea  total $8,050
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 152 groups, price range $5,729 – $112,700 total
G4 fetched: 72 groups → 216 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   216 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 327 Row 15 Seats 21–22  avg $3,200/ea  total $6,400
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 2 groups, price range $8,150 – $9,200 total
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
Cheapest New: Sec 318 Row 15 Seats 5–6  avg $3,450/ea  total $6,900

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            186 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            216 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **PARTIAL**

