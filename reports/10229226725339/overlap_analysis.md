## Category 1 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 188 groups, price range $3,680 – $230,000 total
G4 fetched: 67 groups → 201 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   201 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 205 Row 14 Seats 1–2  avg $1,840/ea  total $3,680
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 152 groups, price range $3,450 – $27,071 total
G4 fetched: 93 groups → 279 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   276 |       98.9% | May exist in G2, not top-100   |
| NEW        |     3 |        1.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 510 Row 5 Seats 15–16  avg $2,012/ea  total $4,024
Cheapest New: Sec 540 Row 8 Seats 4–5  avg $1,150/ea  total $2,300

## Category 3 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 46 groups, price range $3,105 – $17,595 total
G4 fetched: 16 groups → 48 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |       93.8% | May exist in G2, not top-100   |
| NEW        |     3 |        6.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 506 Row 14 Seats 13–14  avg $1,725/ea  total $3,450
Cheapest New: Sec 521 Row 11 Seats 17–18  avg $1,496/ea  total $2,992

## Category 4 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 5 groups, price range $2,760 – $6,900 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 526 Row 15 Seats 9–10  avg $2,300/ea  total $4,600
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            201 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            276 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             45 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

