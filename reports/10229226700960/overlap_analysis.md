## Category 1 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 47 groups, price range $5,060 – $18,400 total
G4 fetched: 16 groups → 48 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    48 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec C338 Row 1 Seats 13–14  avg $3,162/ea  total $6,324
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 42 groups, price range $4,140 – $69,805 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |       87.5% | May exist in G2, not top-100   |
| NEW        |     3 |       12.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 416 Row 27 Seats 20–21  avg $2,300/ea  total $4,600
Cheapest New: Sec 408 Row 12 Seats 1–2  avg $1,995/ea  total $3,990

## Category 3 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 12 groups, price range $4,140 – $11,500 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 435 Row 21 Seats 11–12  avg $2,185/ea  total $4,370
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             48 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             21 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

