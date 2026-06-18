## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 106 groups, price range $4,370 – $230,000 total
G4 fetched: 47 groups → 141 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   138 |       97.9% | May exist in G2, not top-100   |
| NEW        |     3 |        2.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 206 Row 14 Seats 9–10  avg $2,185/ea  total $4,370
Cheapest New: Sec 203 Row 16 Seats 17–18  avg $1,955/ea  total $3,910

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 113 groups, price range $2,990 – $23,000 total
G4 fetched: 82 groups → 246 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   240 |       97.6% | May exist in G2, not top-100   |
| NEW        |     6 |        2.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 535 Row 16 Seats 12–13  avg $1,610/ea  total $3,220
Cheapest New: Sec 456 Row 3 Seats 9–10  avg $1,480/ea  total $2,960

Pairs eligible for merge (NEW below G2 min $2,990): 3

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 16 groups, price range $3,105 – $15,410 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 549 Row 19 Seats 15–16  avg $1,714/ea  total $3,428
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            138 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            240 | DERIVE          |
| Cat 3    |       0.0% |         0 |             18 | INVESTIGATE     |

Overall recommendation: **DERIVE**

