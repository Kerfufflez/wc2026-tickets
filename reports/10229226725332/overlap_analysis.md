## Category 1 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 140 groups, price range $2,645 – $57,500 total
G4 fetched: 159 groups → 477 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   477 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 124 Row 36 Seats 8–9  avg $1,393/ea  total $2,786
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 214 groups, price range $2,022 – $34,500 total
G4 fetched: 109 groups → 327 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   318 |       97.2% | May exist in G2, not top-100   |
| NEW        |     9 |        2.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 309 Row 7 Seats 19–20  avg $1,092/ea  total $2,184
Cheapest New: Sec 344 Row 20 Seats 1–2  avg $862/ea  total $1,724

Pairs eligible for merge (NEW below G2 min $2,022): 9

## Category 3 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 61 groups, price range $1,840 – $20,442 total
G4 fetched: 33 groups → 99 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    99 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 323 Row 19 Seats 25–26  avg $989/ea  total $1,978
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 10 groups, price range $2,185 – $6,900 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 331 Row 24 Seats 9–10  avg $1,150/ea  total $2,300
Cheapest New: Sec 331 Row 25 Seats 15–16  avg $978/ea  total $1,956

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            477 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |            318 | DERIVE          |
| Cat 3    |       0.0% |         0 |             99 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              6 | SKIP            |

Overall recommendation: **DERIVE**

