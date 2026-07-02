## Category 1 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 399 groups, price range $1,679 – $18,400 total
G4 fetched: 209 groups → 627 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   621 |       99.0% | May exist in G2, not top-100   |
| NEW        |     6 |        1.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 136 Row DD Seats 5–6  avg $840/ea  total $1,680
Cheapest New: Sec 131 Row P Seats 7–8  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $1,679): 0

## Category 2 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 137 groups, price range $1,288 – $57,500 total
G4 fetched: 59 groups → 177 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   177 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 639 Row E Seats 9–10  avg $862/ea  total $1,724
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 75 groups, price range $1,564 – $8,165 total
G4 fetched: 23 groups → 69 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    66 |       95.7% | May exist in G2, not top-100   |
| NEW        |     3 |        4.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 629 Row K Seats 17–18  avg $850/ea  total $1,700
Cheapest New: Sec 747 Row R Seats 5–6  avg $5,116/ea  total $10,232

## Category 4 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 12 groups, price range $1,598 – $4,554 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 725 Row P Seats 3–4  avg $1,035/ea  total $2,070
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            621 | DERIVE          |
| Cat 2    |       0.0% |         0 |            177 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             66 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

