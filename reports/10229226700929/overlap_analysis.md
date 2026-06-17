## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 210 groups, price range $1,378 – $41,233 total
G4 fetched: 141 groups → 423 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   420 |       99.3% | May exist in G2, not top-100   |
| NEW        |     3 |        0.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 129 Row 42 Seats 5–6  avg $713/ea  total $1,426
Cheapest New: Sec 129 Row 36 Seats 17–18  avg $667/ea  total $1,334

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 160 groups, price range $1,058 – $5,416 total
G4 fetched: 114 groups → 342 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   339 |       99.1% | May exist in G2, not top-100   |
| NEW        |     3 |        0.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 312 Row 9 Seats 11–12  avg $562/ea  total $1,124
Cheapest New: Sec 225B Row 11 Seats 15–16  avg $3,450/ea  total $6,900

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 48 groups, price range $1,136 – $7,072 total
G4 fetched: 17 groups → 51 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    51 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 325 Row 18 Seats 1–2  avg $575/ea  total $1,150
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 6 groups, price range $1,265 – $2,760 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 346 Row 23 Seats 17–18  avg $759/ea  total $1,518
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            420 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            339 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             51 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

