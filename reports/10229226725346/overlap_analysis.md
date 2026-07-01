## Category 1 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 448 groups, price range $1,909 – $18,400 total
G4 fetched: 241 groups → 723 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   714 |       98.8% | May exist in G2, not top-100   |
| NEW        |     9 |        1.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 139 Row J Seats 1–2  avg $1,035/ea  total $2,070
Cheapest New: Sec 117 Row BB Seats 1–2  avg $920/ea  total $1,840

Pairs eligible for merge (NEW below G2 min $1,909): 3

## Category 2 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 125 groups, price range $1,798 – $57,500 total
G4 fetched: 62 groups → 186 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   186 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 613 Row L Seats 13–14  avg $918/ea  total $1,836
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 67 groups, price range $1,840 – $12,650 total
G4 fetched: 18 groups → 54 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    51 |       94.4% | May exist in G2, not top-100   |
| NEW        |     3 |        5.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 623 Row L Seats 1–2  avg $920/ea  total $1,840
Cheapest New: Sec 627 Row H Seats 4–5  avg $894/ea  total $1,788

## Category 4 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 6 groups, price range $1,955 – $4,554 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 743 Row Q Seats 5–6  avg $1,725/ea  total $3,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            714 | DERIVE          |
| Cat 2    |       0.0% |         0 |            186 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             51 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

