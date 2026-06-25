## Category 1 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 169 groups, price range $2,978 – $14,950 total
G4 fetched: 78 groups → 234 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   219 |       93.6% | May exist in G2, not top-100   |
| NEW        |    15 |        6.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 116 Row 23 Seats 11–12  avg $1,668/ea  total $3,336
Cheapest New: Sec 141 Row 14 Seats 11–12  avg $1,380/ea  total $2,760

Pairs eligible for merge (NEW below G2 min $2,978): 9

## Category 2 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 144 groups, price range $2,300 – $23,000 total
G4 fetched: 73 groups → 219 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   216 |       98.6% | May exist in G2, not top-100   |
| NEW        |     3 |        1.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 223 Row 27 Seats 19–20  avg $1,380/ea  total $2,760
Cheapest New: Sec 225 Row 6 Seats 6–7  avg $13,799/ea  total $27,598

## Category 3 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 15 groups, price range $2,242 – $7,590 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 303 Row 21 Seats 20–21  avg $1,610/ea  total $3,220
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 2 groups, price range $2,875 – $8,108 total
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
| Cat 1    |       0.0% |        15 |            219 | DERIVE          |
| Cat 2    |       0.0% |         3 |            216 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

