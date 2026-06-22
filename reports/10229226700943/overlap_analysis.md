## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 20 groups, price range $1,380 – $2,990 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    57 |       95.0% | May exist in G2, not top-100   |
| NEW        |     3 |        5.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 110 Row 7 Seats 9–10  avg $690/ea  total $1,380
Cheapest New: Sec 136 Row 16 Seats 11–12  avg $3,450/ea  total $6,900

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 32 groups, price range $920 – $4,600 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |       92.9% | May exist in G2, not top-100   |
| NEW        |     3 |        7.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 128 Row 33 Seats 11–12  avg $604/ea  total $1,208
Cheapest New: Sec 128 Row 33 Seats 19–20  avg $2,875/ea  total $5,750

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 25 groups, price range $1,033 – $3,565 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |       91.7% | May exist in G2, not top-100   |
| NEW        |     3 |        8.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 236 Row 9 Seats 20–21  avg $575/ea  total $1,150
Cheapest New: Sec 218 Row 11 Seats 1–2  avg $2,300/ea  total $4,600

## Category 4 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 2 groups, price range $1,610 – $1,725 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 207 Row 28 Seats 5–6  avg $805/ea  total $1,610
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             57 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             39 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             33 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

