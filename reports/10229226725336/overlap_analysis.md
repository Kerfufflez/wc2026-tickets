## Category 1 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 233 groups, price range $3,770 – $83,950 total
G4 fetched: 96 groups → 288 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   282 |       97.9% | May exist in G2, not top-100   |
| NEW        |     6 |        2.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 123 Row 27 Seats 12–13  avg $1,898/ea  total $3,796
Cheapest New: Sec 124 Row 25 Seats 17–18  avg $1,725/ea  total $3,450

Pairs eligible for merge (NEW below G2 min $3,770): 6

## Category 2 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 162 groups, price range $2,266 – $34,500 total
G4 fetched: 77 groups → 231 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   231 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 201 Row 12 Seats 19–20  avg $1,725/ea  total $3,450
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 101 groups, price range $2,530 – $20,700 total
G4 fetched: 36 groups → 108 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   102 |       94.4% | May exist in G2, not top-100   |
| NEW        |     6 |        5.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 417 Row 15 Seats 13–14  avg $1,495/ea  total $2,990
Cheapest New: Sec 418 Row 21 Seats 29–30  avg $11,500/ea  total $23,000

Pairs eligible for merge (NEW below G2 min $2,530): 0

## Category 4 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 4 groups, price range $3,450 – $13,800 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 422 Row 15 Seats 12–13  avg $1,725/ea  total $3,450
Cheapest New: Sec 401 Row 18 Seats 23–24  avg $11,500/ea  total $23,000

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            282 | DERIVE          |
| Cat 2    |       0.0% |         0 |            231 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |            102 | DERIVE          |
| Cat 4    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **DERIVE**

