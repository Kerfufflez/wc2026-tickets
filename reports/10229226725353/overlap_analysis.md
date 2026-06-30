## Category 1 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 243 groups, price range $5,980 – $575,000 total
G4 fetched: 80 groups → 240 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   237 |       98.8% | May exist in G2, not top-100   |
| NEW        |     3 |        1.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 113 Row 14 Seats 6–7  avg $3,450/ea  total $6,900
Cheapest New: Sec 139 Row 10 Seats 5–6  avg $2,875/ea  total $5,750

## Category 2 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 214 groups, price range $3,910 – $59,570 total
G4 fetched: 84 groups → 252 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   252 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 312 Row 11 Seats 16–17  avg $2,070/ea  total $4,140
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 13 groups, price range $4,140 – $11,500 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 301 Row 23 Seats 5–6  avg $4,600/ea  total $9,200
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            237 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            252 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

