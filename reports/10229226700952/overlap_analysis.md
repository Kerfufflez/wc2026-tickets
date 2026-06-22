## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 71 groups, price range $1,479 – $16,429 total
G4 fetched: 22 groups → 66 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    66 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 221 Row UU Seats 110–111  avg $780/ea  total $1,560
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 42 groups, price range $1,378 – $12,322 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |       85.7% | May exist in G2, not top-100   |
| NEW        |     6 |       14.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 440 Row ZZ Seats 106–107  avg $742/ea  total $1,484
Cheapest New: Sec 416 Row OO Seats 4–5  avg $657/ea  total $1,314

Pairs eligible for merge (NEW below G2 min $1,378): 6

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 31 groups, price range $1,314 – $7,886 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 418 Row PP Seats 107–108  avg $727/ea  total $1,454
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             66 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             36 | DERIVE          |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

