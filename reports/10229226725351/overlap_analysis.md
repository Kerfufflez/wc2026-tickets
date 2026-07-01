## Category 1 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 128 groups, price range $5,727 – $57,500 total
G4 fetched: 44 groups → 132 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   129 |       97.7% | May exist in G2, not top-100   |
| NEW        |     3 |        2.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 117 Row 30 Seats 16–17  avg $3,322/ea  total $6,644
Cheapest New: Sec 117 Row 16 Seats 19–20  avg $2,760/ea  total $5,520

## Category 2 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 102 groups, price range $4,370 – $57,500 total
G4 fetched: 50 groups → 150 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   144 |       96.0% | May exist in G2, not top-100   |
| NEW        |     6 |        4.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 337 Row 25 Seats 17–18  avg $2,185/ea  total $4,370
Cheapest New: Sec 310 Row 7 Seats 5–6  avg $2,012/ea  total $4,024

Pairs eligible for merge (NEW below G2 min $4,370): 3

## Category 3 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 111 groups, price range $3,876 – $46,000 total
G4 fetched: 48 groups → 144 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   144 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 319 Row 22 Seats 10–11  avg $2,070/ea  total $4,140
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 8 groups, price range $6,900 – $18,398 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       33.3% | May exist in G2, not top-100   |
| NEW        |     6 |       66.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 313 Row 33 Seats 6–7  avg $4,025/ea  total $8,050
Cheapest New: Sec 314 Row 27 Seats 1–2  avg $2,300/ea  total $4,600

Pairs eligible for merge (NEW below G2 min $6,900): 6

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            129 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            144 | DERIVE          |
| Cat 3    |       0.0% |         0 |            144 | INVESTIGATE     |
| Cat 4    |       0.0% |         6 |              3 | DERIVE          |

Overall recommendation: **DERIVE**

