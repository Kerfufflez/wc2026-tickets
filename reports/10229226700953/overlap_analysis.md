## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 159 groups, price range $460 – $34,500 total
G4 fetched: 243 groups → 729 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   726 |       99.6% | May exist in G2, not top-100   |
| NEW        |     3 |        0.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 334 Row U Seats 15–16  avg $276/ea  total $552
Cheapest New: Sec 126 Row Q Seats 19–20  avg $57,787/ea  total $115,574

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 155 groups, price range $414 – $6,900 total
G4 fetched: 122 groups → 366 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   363 |       99.2% | May exist in G2, not top-100   |
| NEW        |     3 |        0.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 352 Row H Seats 17–18  avg $230/ea  total $460
Cheapest New: Sec 324 Row G Seats 17–18  avg $198/ea  total $396

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 92 groups, price range $331 – $4,922 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 638 Row M Seats 3–4  avg $213/ea  total $426
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 11 groups, price range $471 – $16,100 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 717 Row Q Seats 14–15  avg $242/ea  total $484
Cheapest New: Sec 724 Row R Seats 15–16  avg $229/ea  total $458

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            726 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            363 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             81 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

