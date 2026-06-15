## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 108 groups, price range $742 – $3,968 total
G4 fetched: 91 groups → 273 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   258 |       94.5% | May exist in G2, not top-100   |
| NEW        |    15 |        5.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 130 Row 5 Seats 27–28  avg $391/ea  total $782
Cheapest New: Sec 124 Row 10 Seats 8–9  avg $330/ea  total $660

Pairs eligible for merge (NEW below G2 min $742): 15

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 143 groups, price range $575 – $1,055,700 total
G4 fetched: 89 groups → 267 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   267 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 127 Row 31 Seats 13–14  avg $316/ea  total $632
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 104 groups, price range $407 – $2,300 total
G4 fetched: 34 groups → 102 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    99 |       97.1% | May exist in G2, not top-100   |
| NEW        |     3 |        2.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 416 Row 26 Seats 13–14  avg $231/ea  total $462
Cheapest New: Sec 422 Row 1 Seats 1–2  avg $3,450/ea  total $6,900

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 6 groups, price range $575 – $920 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 401 Row 26 Seats 17–18  avg $345/ea  total $690
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |        15 |            258 | DERIVE          |
| Cat 2    |       0.0% |         0 |            267 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             99 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

