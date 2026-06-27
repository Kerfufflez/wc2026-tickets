## Category 1 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 148 groups, price range $7,532 – $80,500 total
G4 fetched: 59 groups → 177 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   174 |       98.3% | May exist in G2, not top-100   |
| NEW        |     3 |        1.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 229 Row K Seats 6–7  avg $4,453/ea  total $8,906
Cheapest New: Sec 212 Row D Seats 15–16  avg $40,566/ea  total $81,132

## Category 2 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 138 groups, price range $6,428 – $33,316 total
G4 fetched: 56 groups → 168 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   159 |       94.6% | May exist in G2, not top-100   |
| NEW        |     9 |        5.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 309 Row T Seats 5–6  avg $3,245/ea  total $6,490
Cheapest New: Sec 331 Row G Seats 1–2  avg $17,250/ea  total $34,500

Pairs eligible for merge (NEW below G2 min $6,428): 0

## Category 3 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 40 groups, price range $5,060 – $115,000 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 318 Row P Seats 19–20  avg $2,840/ea  total $5,680
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            174 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |            159 | DERIVE          |
| Cat 3    |       0.0% |         0 |             45 | INVESTIGATE     |

Overall recommendation: **DERIVE**

