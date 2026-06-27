## Category 1 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 44 groups, price range $2,300 – $11,960 total
G4 fetched: 16 groups → 48 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    48 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 135 Row W Seats 9–10  avg $1,265/ea  total $2,530
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 13 groups, price range $2,670 – $12,478 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |       71.4% | May exist in G2, not top-100   |
| NEW        |     6 |       28.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 245 Row CC Seats 6–7  avg $1,552/ea  total $3,104
Cheapest New: Sec 247 Row W Seats 9–10  avg $1,143/ea  total $2,286

Pairs eligible for merge (NEW below G2 min $2,670): 6

## Category 3 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 14 groups, price range $2,613 – $27,600 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 237 Row J Seats 6–7  avg $1,409/ea  total $2,818
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             48 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             15 | DERIVE          |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

