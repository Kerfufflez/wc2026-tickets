## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 112 groups, price range $3,795 – $57,500 total
G4 fetched: 105 groups → 315 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   306 |       97.1% | May exist in G2, not top-100   |
| NEW        |     9 |        2.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 149 Row 25 Seats 17–18  avg $1,955/ea  total $3,910
Cheapest New: Sec 101 Row 43 Seats 21–22  avg $1,892/ea  total $3,784

Pairs eligible for merge (NEW below G2 min $3,795): 6

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 162 groups, price range $2,758 – $23,000 total
G4 fetched: 76 groups → 228 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   228 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 318 Row 11 Seats 13–14  avg $1,380/ea  total $2,760
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 44 groups, price range $2,760 – $20,442 total
G4 fetched: 28 groups → 84 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    84 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 302 Row 18 Seats 13–14  avg $1,409/ea  total $2,818
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 7 groups, price range $2,932 – $11,500 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 346 Row 21 Seats 11–12  avg $1,485/ea  total $2,970
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            306 | DERIVE          |
| Cat 2    |       0.0% |         0 |            228 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             84 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

