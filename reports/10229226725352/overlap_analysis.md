## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 179 groups, price range $4,107 – $34,500 total
G4 fetched: 71 groups → 213 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   189 |       88.7% | May exist in G2, not top-100   |
| NEW        |    24 |       11.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 248 Row NN Seats 5–6  avg $2,158/ea  total $4,316
Cheapest New: Sec 206 Row T Seats 1–2  avg $17,396/ea  total $34,792

Pairs eligible for merge (NEW below G2 min $4,107): 0

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 125 groups, price range $3,614 – $19,348 total
G4 fetched: 32 groups → 96 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    93 |       96.9% | May exist in G2, not top-100   |
| NEW        |     3 |        3.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 420 Row UU Seats 104–105  avg $2,054/ea  total $4,108
Cheapest New: Sec 440 Row PP Seats 8–9  avg $11,488/ea  total $22,976

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 23 groups, price range $4,107 – $34,500 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 426 Row BB Seats 105–106  avg $2,218/ea  total $4,436
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 4 groups, price range $4,140 – $10,027 total
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
| Cat 1    |       0.0% |        24 |            189 | DERIVE          |
| Cat 2    |       0.0% |         3 |             93 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             39 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

