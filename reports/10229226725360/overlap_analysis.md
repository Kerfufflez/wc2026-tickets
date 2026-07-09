## Category 1 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 34 groups, price range $33,005 – $2,326,450 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 45 Seats 10–11  avg $18,400/ea  total $36,800
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 51 groups, price range $21,192 – $178,036 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 316 Row 12 Seats 7–8  avg $14,375/ea  total $28,750
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 35 groups, price range $20,700 – $1,357,000 total
G4 fetched: 16 groups → 48 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    42 |       87.5% | May exist in G2, not top-100   |
| NEW        |     6 |       12.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 349 Row 26 Seats 4–5  avg $10,350/ea  total $20,700
Cheapest New: Sec 350 Row 25 Seats 13–14  avg $9,775/ea  total $19,550

Pairs eligible for merge (NEW below G2 min $20,700): 6

## Category 4 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 14 groups, price range $21,390 – $60,950 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |       83.3% | May exist in G2, not top-100   |
| NEW        |     3 |       16.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 346 Row 24 Seats 18–19  avg $12,018/ea  total $24,036
Cheapest New: Sec 346 Row 18 Seats 13–14  avg $10,120/ea  total $20,240

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |              9 | SKIP            |
| Cat 2    |       0.0% |         0 |             12 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             42 | DERIVE          |
| Cat 4    |       0.0% |         3 |             15 | INVESTIGATE     |

Overall recommendation: **DERIVE**

