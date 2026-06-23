## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 176 groups, price range $4,825 – $34,500 total
G4 fetched: 70 groups → 210 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   186 |       88.6% | May exist in G2, not top-100   |
| NEW        |    24 |       11.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 253 Row MM Seats 105–106  avg $2,527/ea  total $5,054
Cheapest New: Sec 206 Row T Seats 1–2  avg $17,259/ea  total $34,518

Pairs eligible for merge (NEW below G2 min $4,825): 0

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 124 groups, price range $4,075 – $19,197 total
G4 fetched: 35 groups → 105 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   102 |       97.1% | May exist in G2, not top-100   |
| NEW        |     3 |        2.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 438 Row NN Seats 5–6  avg $2,159/ea  total $4,318
Cheapest New: Sec 440 Row PP Seats 8–9  avg $11,488/ea  total $22,976

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 25 groups, price range $4,112 – $34,500 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 425 Row D Seats 106–107  avg $2,300/ea  total $4,600
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 3 groups, price range $4,140 – $9,924 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 428 Row ZZ Seats 1–2  avg $2,271/ea  total $4,542
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |        24 |            186 | DERIVE          |
| Cat 2    |       0.0% |         3 |            102 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             33 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

