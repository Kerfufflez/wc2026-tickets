## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 448 groups, price range $3,200 – $92,000 total
G4 fetched: 281 groups → 843 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   837 |       99.3% | May exist in G2, not top-100   |
| NEW        |     6 |        0.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 229 Row 6 Seats 21–22  avg $1,725/ea  total $3,450
Cheapest New: Sec 130 Row 20 Seats 21–22  avg $1,000,500/ea  total $2,001,000

Pairs eligible for merge (NEW below G2 min $3,200): 0

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 165 groups, price range $2,760 – $46,000 total
G4 fetched: 68 groups → 204 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   201 |       98.5% | May exist in G2, not top-100   |
| NEW        |     3 |        1.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 342 Row 18 Seats 7–8  avg $1,449/ea  total $2,898
Cheapest New: Sec 320 Row 20 Seats 17–18  avg $25,300/ea  total $50,600

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 55 groups, price range $2,872 – $271,400 total
G4 fetched: 21 groups → 63 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    63 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 329 Row 30 Seats 17–18  avg $1,477/ea  total $2,954
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 9 groups, price range $2,760 – $16,100 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 29 Seats 26–27  avg $5,750/ea  total $11,500
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            837 | DERIVE          |
| Cat 2    |       0.0% |         3 |            201 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             63 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

