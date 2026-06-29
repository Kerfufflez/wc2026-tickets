## Category 1 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 211 groups, price range $1,378 – $18,377 total
G4 fetched: 91 groups → 273 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   264 |       96.7% | May exist in G2, not top-100   |
| NEW        |     9 |        3.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 225 Row 9 Seats 6–7  avg $690/ea  total $1,380
Cheapest New: Sec C307 Row 5 Seats 6–7  avg $632/ea  total $1,264

Pairs eligible for merge (NEW below G2 min $1,378): 6

## Category 2 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 189 groups, price range $1,104 – $9,775 total
G4 fetched: 86 groups → 258 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   255 |       98.8% | May exist in G2, not top-100   |
| NEW        |     3 |        1.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 410 Row 15 Seats 5–6  avg $575/ea  total $1,150
Cheapest New: Sec 444 Row 16 Seats 15–16  avg $546/ea  total $1,092

## Category 3 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 28 groups, price range $1,035 – $5,060 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 452 Row 21 Seats 13–14  avg $736/ea  total $1,472
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 2 groups, price range $2,070 – $2,128 total
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
Cheapest New: Sec 401 Row 20 Seats 7–8  avg $744/ea  total $1,488

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            264 | DERIVE          |
| Cat 2    |       0.0% |         3 |            255 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             15 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

