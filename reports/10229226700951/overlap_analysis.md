## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 121 groups, price range $690 – $5,750 total
G4 fetched: 136 groups → 408 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   405 |       99.3% | May exist in G2, not top-100   |
| NEW        |     3 |        0.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 126 Row R Seats 9–10  avg $374/ea  total $748
Cheapest New: Sec 140 Row F Seats 10–11  avg $4,485/ea  total $8,970

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 195 groups, price range $495 – $6,900 total
G4 fetched: 233 groups → 699 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   699 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 147 Row W Seats 1–2  avg $253/ea  total $506
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 157 groups, price range $445 – $2,300 total
G4 fetched: 79 groups → 237 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   231 |       97.5% | May exist in G2, not top-100   |
| NEW        |     6 |        2.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 324 Row Y Seats 7–8  avg $243/ea  total $486
Cheapest New: Sec 313 Row C Seats 3–4  avg $1,368/ea  total $2,736

Pairs eligible for merge (NEW below G2 min $445): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            405 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            699 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |            231 | DERIVE          |

Overall recommendation: **DERIVE**

