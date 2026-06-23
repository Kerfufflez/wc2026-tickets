## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 46 groups, price range $3,422 – $16,100 total
G4 fetched: 18 groups → 54 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    54 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 218 Row 4 Seats 20–21  avg $1,955/ea  total $3,910
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 27 groups, price range $2,500 – $5,750 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |       80.0% | May exist in G2, not top-100   |
| NEW        |     6 |       20.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 408 Row 3 Seats 6–7  avg $1,380/ea  total $2,760
Cheapest New: Sec 342 Row 13 Seats 2–3  avg $2,904/ea  total $5,808

Pairs eligible for merge (NEW below G2 min $2,500): 0

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 5 groups, price range $2,893 – $2,875,000 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 454 Row 11 Seats 6–7  avg $1,725/ea  total $3,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             54 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             24 | DERIVE          |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

