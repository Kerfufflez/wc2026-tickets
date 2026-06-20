## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 104 groups, price range $805 – $3,910 total
G4 fetched: 67 groups → 201 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   198 |       98.5% | May exist in G2, not top-100   |
| NEW        |     3 |        1.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 127 Row T Seats 9–10  avg $472/ea  total $944
Cheapest New: Sec 240 Row D Seats 12–13  avg $2,875/ea  total $5,750

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 152 groups, price range $668 – $3,450 total
G4 fetched: 104 groups → 312 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   312 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 149 Row TT Seats 6–7  avg $356/ea  total $712
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 52 groups, price range $667 – $3,220 total
G4 fetched: 24 groups → 72 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    72 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 339 Row JJ Seats 13–14  avg $345/ea  total $690
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 3 groups, price range $690 – $2,760 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 344 Row J Seats 16–17  avg $460/ea  total $920
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            198 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            312 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             72 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

