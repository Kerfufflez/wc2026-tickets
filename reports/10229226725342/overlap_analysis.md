## Category 1 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 272 groups, price range $2,300 – $48,548 total
G4 fetched: 136 groups → 408 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   405 |       99.3% | May exist in G2, not top-100   |
| NEW        |     3 |        0.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 125 Row 14 Seats 5–6  avg $1,150/ea  total $2,300
Cheapest New: Sec 125 Row 37 Seats 17–18  avg $115,000/ea  total $230,000

## Category 2 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 181 groups, price range $2,036 – $23,000 total
G4 fetched: 67 groups → 201 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   201 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 304 Row 36 Seats 3–4  avg $1,127/ea  total $2,254
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 30, 2026

G2 fetched: 113 groups, price range $1,780 – $10,350 total
G4 fetched: 41 groups → 123 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   117 |       95.1% | May exist in G2, not top-100   |
| NEW        |     6 |        4.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 309 Row 22 Seats 1–2  avg $1,092/ea  total $2,184
Cheapest New: Sec 330 Row 38 Seats 1–2  avg $5,750/ea  total $11,500

Pairs eligible for merge (NEW below G2 min $1,780): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            405 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            201 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |            117 | DERIVE          |

Overall recommendation: **DERIVE**

