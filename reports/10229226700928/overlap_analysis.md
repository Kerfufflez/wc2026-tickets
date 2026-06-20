## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 36 groups, price range $1,149 – $2,462 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |       88.9% | May exist in G2, not top-100   |
| NEW        |     3 |       11.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 209 Row GG Seats 8–9  avg $598/ea  total $1,196
Cheapest New: Sec 219 Row VV Seats 1–2  avg $568/ea  total $1,136

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 60 groups, price range $977 – $8,206 total
G4 fetched: 16 groups → 48 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    48 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 233 Row NN Seats 108–109  avg $533/ea  total $1,066
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 20 groups, price range $920 – $3,576 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 420 Row ZZ Seats 1–2  avg $657/ea  total $1,314
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             24 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             48 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

