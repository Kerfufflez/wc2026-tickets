## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 132 groups, price range $3,586 – $18,285 total
G4 fetched: 63 groups → 189 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   177 |       93.7% | May exist in G2, not top-100   |
| NEW        |    12 |        6.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 137 Row 24 Seats 8–9  avg $1,892/ea  total $3,784
Cheapest New: Sec 119 Row 27 Seats 13–14  avg $1,725/ea  total $3,450

Pairs eligible for merge (NEW below G2 min $3,586): 3

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 114 groups, price range $2,841 – $23,000 total
G4 fetched: 69 groups → 207 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   207 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 307 Row 14 Seats 7–8  avg $1,610/ea  total $3,220
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 14 groups, price range $2,576 – $8,050 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 315 Row 18 Seats 5–6  avg $1,725/ea  total $3,450
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 2 groups, price range $2,990 – $5,808 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 318 Row 14 Seats 1–2  avg $1,610/ea  total $3,220
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |        12 |            177 | DERIVE          |
| Cat 2    |       0.0% |         0 |            207 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              6 | SKIP            |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

