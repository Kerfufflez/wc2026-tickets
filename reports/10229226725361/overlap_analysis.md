## Category 1 — Pair Derivation Analysis
Date: July 15, 2026

G2 fetched: 528 groups, price range $3,220 – $81,202 total
G4 fetched: 320 groups → 960 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   954 |       99.4% | May exist in G2, not top-100   |
| NEW        |     6 |        0.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 154 Row 24 Seats 5–6  avg $1,725/ea  total $3,450
Cheapest New: Sec 230 Row 3 Seats 19–20  avg $43,700/ea  total $87,400

Pairs eligible for merge (NEW below G2 min $3,220): 0

## Category 2 — Pair Derivation Analysis
Date: July 15, 2026

G2 fetched: 223 groups, price range $2,760 – $229,999 total
G4 fetched: 74 groups → 222 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   222 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 323 Row 25 Seats 17–18  avg $1,552/ea  total $3,104
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 15, 2026

G2 fetched: 89 groups, price range $2,528 – $80,500 total
G4 fetched: 24 groups → 72 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    72 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 330 Row 18 Seats 13–14  avg $1,725/ea  total $3,450
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 15, 2026

G2 fetched: 10 groups, price range $3,450 – $23,000 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 28 Seats 25–26  avg $1,955/ea  total $3,910
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            954 | DERIVE          |
| Cat 2    |       0.0% |         0 |            222 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             72 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

