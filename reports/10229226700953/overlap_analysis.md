## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 152 groups, price range $575 – $230,000 total
G4 fetched: 228 groups → 684 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   681 |       99.6% | May exist in G2, not top-100   |
| NEW        |     3 |        0.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 344 Row K Seats 6–7  avg $288/ea  total $576
Cheapest New: Sec 334 Row U Seats 15–16  avg $276/ea  total $552

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 154 groups, price range $460 – $6,900 total
G4 fetched: 118 groups → 354 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   351 |       99.2% | May exist in G2, not top-100   |
| NEW        |     3 |        0.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 352 Row P Seats 9–10  avg $230/ea  total $460
Cheapest New: Sec 324 Row G Seats 17–18  avg $198/ea  total $396

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 87 groups, price range $391 – $4,922 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 616 Row N Seats 3–4  avg $218/ea  total $436
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 11 groups, price range $471 – $16,100 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 717 Row Q Seats 14–15  avg $242/ea  total $484
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            681 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            351 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             81 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

