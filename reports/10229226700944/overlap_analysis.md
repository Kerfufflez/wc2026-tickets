## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 55 groups, price range $3,614 – $21,850 total
G4 fetched: 19 groups → 57 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    57 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 131 Row 16 Seats 9–10  avg $2,299/ea  total $4,598
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 57 groups, price range $2,990 – $11,500 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 335 Row 17 Seats 24–25  avg $1,719/ea  total $3,438
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 24 groups, price range $2,990 – $8,050 total
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
Date: June 20, 2026

G2 fetched: 7 groups, price range $3,450 – $7,475 total
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
Cheapest New: Sec 306 Row 25 Seats 14–15  avg $1,709/ea  total $3,418

Pairs eligible for merge (NEW below G2 min $3,450): 3

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             57 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             21 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              9 | SKIP            |
| Cat 4    |       0.0% |         6 |              3 | DERIVE          |

Overall recommendation: **DERIVE**

