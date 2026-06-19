## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 57 groups, price range $3,197 – $21,850 total
G4 fetched: 26 groups → 78 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    78 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 128 Row 5 Seats 11–12  avg $1,804/ea  total $3,608
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 60 groups, price range $3,105 – $11,500 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 319 Row 2 Seats 1–2  avg $1,610/ea  total $3,220
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 27 groups, price range $2,760 – $8,050 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 349 Row 24 Seats 10–11  avg $1,495/ea  total $2,990
Cheapest New: Sec 304 Row 10 Seats 5–6  avg $32,775/ea  total $65,550

## Category 4 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 7 groups, price range $3,668 – $7,475 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       33.3% | May exist in G2, not top-100   |
| NEW        |     6 |       66.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 306 Row 21 Seats 13–14  avg $2,300/ea  total $4,600
Cheapest New: Sec 306 Row 25 Seats 14–15  avg $1,707/ea  total $3,414

Pairs eligible for merge (NEW below G2 min $3,668): 3

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             78 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             33 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              9 | SKIP            |
| Cat 4    |       0.0% |         6 |              3 | DERIVE          |

Overall recommendation: **DERIVE**

