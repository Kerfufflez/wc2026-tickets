## Category 1 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 193 groups, price range $4,830 – $55,131 total
G4 fetched: 76 groups → 228 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   213 |       93.4% | May exist in G2, not top-100   |
| NEW        |    15 |        6.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 253 Row MM Seats 105–106  avg $2,513/ea  total $5,026
Cheapest New: Sec 229 Row K Seats 1–2  avg $2,351/ea  total $4,702

Pairs eligible for merge (NEW below G2 min $4,830): 3

## Category 2 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 129 groups, price range $3,892 – $20,269 total
G4 fetched: 41 groups → 123 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   120 |       97.6% | May exist in G2, not top-100   |
| NEW        |     3 |        2.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 437 Row RR Seats 101–102  avg $2,027/ea  total $4,054
Cheapest New: Sec 440 Row PP Seats 8–9  avg $11,488/ea  total $22,976

## Category 3 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 33 groups, price range $4,021 – $34,500 total
G4 fetched: 18 groups → 54 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    54 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 450 Row MM Seats 3–4  avg $2,027/ea  total $4,054
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 4 groups, price range $4,140 – $9,924 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 428 Row ZZ Seats 1–2  avg $2,271/ea  total $4,542
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |        15 |            213 | DERIVE          |
| Cat 2    |       0.0% |         3 |            120 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             54 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

