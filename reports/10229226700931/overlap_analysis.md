## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 61 groups, price range $3,438 – $27,600 total
G4 fetched: 21 groups → 63 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    63 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec C309 Row 16 Seats 20–21  avg $2,070/ea  total $4,140
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 50 groups, price range $2,530 – $13,225 total
G4 fetched: 19 groups → 57 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    54 |       94.7% | May exist in G2, not top-100   |
| NEW        |     3 |        5.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 418 Row 2 Seats 11–12  avg $1,643/ea  total $3,286
Cheapest New: Sec 406 Row 4 Seats 11–12  avg $8,247/ea  total $16,494

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 25 groups, price range $2,760 – $103,500 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 450 Row 22 Seats 20–21  avg $1,725/ea  total $3,450
Cheapest New: Sec 422 Row 16 Seats 10–11  avg $1,062,600/ea  total $2,125,200

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             63 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             54 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

