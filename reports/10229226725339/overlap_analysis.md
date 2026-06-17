## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 111 groups, price range $4,140 – $230,000 total
G4 fetched: 50 groups → 150 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   150 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 206 Row 14 Seats 9–10  avg $2,185/ea  total $4,370
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 115 groups, price range $2,875 – $23,000 total
G4 fetched: 85 groups → 255 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   249 |       97.6% | May exist in G2, not top-100   |
| NEW        |     6 |        2.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 456 Row 3 Seats 9–10  avg $1,480/ea  total $2,960
Cheapest New: Sec 402 Row 4 Seats 4–5  avg $1,409/ea  total $2,818

Pairs eligible for merge (NEW below G2 min $2,875): 3

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 18 groups, price range $2,760 – $15,410 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 549 Row 19 Seats 15–16  avg $1,714/ea  total $3,428
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            150 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            249 | DERIVE          |
| Cat 3    |       0.0% |         0 |             24 | INVESTIGATE     |

Overall recommendation: **DERIVE**

