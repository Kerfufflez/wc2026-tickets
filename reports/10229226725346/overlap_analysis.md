## Category 1 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 407 groups, price range $1,955 – $21,850 total
G4 fetched: 233 groups → 699 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   693 |       99.1% | May exist in G2, not top-100   |
| NEW        |     6 |        0.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 121 Row HH Seats 7–8  avg $1,081/ea  total $2,162
Cheapest New: Sec 131 Row P Seats 7–8  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $1,955): 0

## Category 2 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 139 groups, price range $1,840 – $57,500 total
G4 fetched: 68 groups → 204 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   204 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 518 Row G Seats 1–2  avg $1,035/ea  total $2,070
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 68 groups, price range $1,610 – $12,650 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    60 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 628 Row C Seats 10–11  avg $920/ea  total $1,840
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 7 groups, price range $1,955 – $4,554 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 718 Row P Seats 1–2  avg $1,725/ea  total $3,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            693 | DERIVE          |
| Cat 2    |       0.0% |         0 |            204 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             60 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

