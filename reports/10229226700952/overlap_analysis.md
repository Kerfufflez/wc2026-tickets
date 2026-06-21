## Category 1 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 79 groups, price range $1,375 – $16,429 total
G4 fetched: 28 groups → 84 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |       96.4% | May exist in G2, not top-100   |
| NEW        |     3 |        3.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 215 Row DD Seats 101–102  avg $739/ea  total $1,478
Cheapest New: Sec 221 Row EE Seats 104–105  avg $575/ea  total $1,150

## Category 2 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 46 groups, price range $1,314 – $12,322 total
G4 fetched: 19 groups → 57 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    51 |       89.5% | May exist in G2, not top-100   |
| NEW        |     6 |       10.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 254 Row LL Seats 103–104  avg $658/ea  total $1,316
Cheapest New: Sec 443 Row WW Seats 102–103  avg $657/ea  total $1,314

Pairs eligible for merge (NEW below G2 min $1,314): 6

## Category 3 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 33 groups, price range $1,257 – $7,886 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 402 Row JJ Seats 105–106  avg $711/ea  total $1,422
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             81 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             51 | DERIVE          |
| Cat 3    |       0.0% |         0 |             12 | INVESTIGATE     |

Overall recommendation: **DERIVE**

