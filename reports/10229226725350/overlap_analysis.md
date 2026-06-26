## Category 1 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 130 groups, price range $7,843 – $80,500 total
G4 fetched: 60 groups → 180 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   177 |       98.3% | May exist in G2, not top-100   |
| NEW        |     3 |        1.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 124 Row S Seats 13–14  avg $4,485/ea  total $8,970
Cheapest New: Sec 212 Row D Seats 15–16  avg $40,566/ea  total $81,132

## Category 2 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 133 groups, price range $6,440 – $33,316 total
G4 fetched: 57 groups → 171 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   162 |       94.7% | May exist in G2, not top-100   |
| NEW        |     9 |        5.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 309 Row T Seats 5–6  avg $3,245/ea  total $6,490
Cheapest New: Sec 331 Row G Seats 1–2  avg $17,250/ea  total $34,500

Pairs eligible for merge (NEW below G2 min $6,440): 0

## Category 3 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 38 groups, price range $6,095 – $115,000 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    42 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 301 Row Q Seats 16–17  avg $3,335/ea  total $6,670
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            177 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |            162 | DERIVE          |
| Cat 3    |       0.0% |         0 |             42 | INVESTIGATE     |

Overall recommendation: **DERIVE**

