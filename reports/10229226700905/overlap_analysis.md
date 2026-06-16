## Category 1 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 80 groups, price range $736 – $10,350 total
G4 fetched: 38 groups → 114 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   114 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 120 Row 32 Seats 1–2  avg $448/ea  total $896
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 76 groups, price range $665 – $3,028 total
G4 fetched: 33 groups → 99 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    96 |       97.0% | May exist in G2, not top-100   |
| NEW        |     3 |        3.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 305 Row 13 Seats 13–14  avg $356/ea  total $712
Cheapest New: Sec 226 Row 22 Seats 7–8  avg $1,725/ea  total $3,450

## Category 3 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 11 groups, price range $690 – $2,300 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 340 Row 19 Seats 6–7  avg $460/ea  total $920
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            114 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             96 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

