## Category 1 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 160 groups, price range $3,250 – $16,100 total
G4 fetched: 73 groups → 219 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   213 |       97.3% | May exist in G2, not top-100   |
| NEW        |     6 |        2.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 140 Row 25 Seats 9–10  avg $1,692/ea  total $3,384
Cheapest New: Sec 126 Row 14 Seats 5–6  avg $9,275/ea  total $18,550

Pairs eligible for merge (NEW below G2 min $3,250): 0

## Category 2 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 106 groups, price range $2,389 – $23,000 total
G4 fetched: 64 groups → 192 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   189 |       98.4% | May exist in G2, not top-100   |
| NEW        |     3 |        1.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 329 Row 1 Seats 14–15  avg $1,285/ea  total $2,570
Cheapest New: Sec 225 Row 6 Seats 6–7  avg $13,799/ea  total $27,598

## Category 3 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 12 groups, price range $3,220 – $7,590 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 303 Row 21 Seats 20–21  avg $1,610/ea  total $3,220
Cheapest New: Sec 303 Row 10 Seats 9–10  avg $1,150/ea  total $2,300

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
| Cat 1    |       0.0% |         6 |            213 | DERIVE          |
| Cat 2    |       0.0% |         3 |            189 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              9 | SKIP            |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

