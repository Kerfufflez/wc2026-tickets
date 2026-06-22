## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 127 groups, price range $3,946 – $23,000 total
G4 fetched: 61 groups → 183 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   177 |       96.7% | May exist in G2, not top-100   |
| NEW        |     6 |        3.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 138 Row 10 Seats 8–9  avg $1,995/ea  total $3,990
Cheapest New: Sec 124 Row 26 Seats 13–14  avg $19,550/ea  total $39,100

Pairs eligible for merge (NEW below G2 min $3,946): 0

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 103 groups, price range $2,932 – $23,000 total
G4 fetched: 53 groups → 159 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   159 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 329 Row 11 Seats 1–2  avg $1,725/ea  total $3,450
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 12 groups, price range $3,565 – $8,050 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 317 Row 13 Seats 5–6  avg $2,559/ea  total $5,118
Cheapest New: Sec 315 Row 18 Seats 5–6  avg $1,725/ea  total $3,450

## Category 4 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 2 groups, price range $4,600 – $5,808 total
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
Cheapest New: Sec 318 Row 14 Seats 1–2  avg $1,610/ea  total $3,220

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            177 | DERIVE          |
| Cat 2    |       0.0% |         0 |            159 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              3 | SKIP            |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

