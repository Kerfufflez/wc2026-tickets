## Category 1 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 32 groups, price range $7,935 – $34,500 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 465 Row 1 Seats 18–19  avg $4,830/ea  total $9,660
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 14 groups, price range $7,360 – $20,700 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 518 Row 9 Seats 6–7  avg $3,923/ea  total $7,846
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 13 groups, price range $6,900 – $57,500 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 658 Row 1 Seats 15–16  avg $4,025/ea  total $8,050
Cheapest New: Sec 615 Row 9 Seats 4–5  avg $3,037/ea  total $6,074

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             21 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             18 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

