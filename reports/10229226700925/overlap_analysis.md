## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 45 groups, price range $1,204 – $13,742 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 135 Row 18 Seats 5–6  avg $805/ea  total $1,610
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 19 groups, price range $1,286 – $4,600 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |       85.7% | May exist in G2, not top-100   |
| NEW        |     3 |       14.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 316 Row 13 Seats 14–15  avg $748/ea  total $1,496
Cheapest New: Sec 317 Row 17 Seats 9–10  avg $23,000/ea  total $46,000

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 20 groups, price range $1,488 – $4,087 total
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
Cheapest New: Sec 330 Row 25 Seats 7–8  avg $2,070/ea  total $4,140

## Category 4 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 4 groups, price range $1,150 – $1,725 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 30 Seats 1–2  avg $667/ea  total $1,334
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             81 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             18 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              0 | SKIP            |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

