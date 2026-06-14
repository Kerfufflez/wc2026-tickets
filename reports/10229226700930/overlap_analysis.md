## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 199 groups, price range $1,146 – $11,500 total
G4 fetched: 112 groups → 336 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   333 |       99.1% | May exist in G2, not top-100   |
| NEW        |     3 |        0.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 115 Row 27 Seats 17–18  avg $661/ea  total $1,322
Cheapest New: Sec 125 Row 8 Seats 1–2  avg $6,900/ea  total $13,800

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 144 groups, price range $1,035 – $6,900 total
G4 fetched: 65 groups → 195 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   189 |       96.9% | May exist in G2, not top-100   |
| NEW        |     6 |        3.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 216 Row 2 Seats 6–7  avg $546/ea  total $1,092
Cheapest New: Sec SW-T-1 Row 2 Seats 27–28  avg $4,600/ea  total $9,200

Pairs eligible for merge (NEW below G2 min $1,035): 0

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 56 groups, price range $954 – $6,900 total
G4 fetched: 24 groups → 72 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    72 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 230 Row 18 Seats 1–2  avg $540/ea  total $1,080
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 3 groups, price range $1,035 – $2,760 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 207 Row 25 Seats 3–4  avg $1,150/ea  total $2,300
Cheapest New: Sec 239 Row 29 Seats 9–10  avg $1,725/ea  total $3,450

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            333 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            189 | DERIVE          |
| Cat 3    |       0.0% |         0 |             72 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

