## Category 1 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 164 groups, price range $1,024 – $2,300,000 total
G4 fetched: 115 groups → 345 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   345 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 125 Row 7 Seats 19–20  avg $574/ea  total $1,148
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 93 groups, price range $816 – $1,124,700 total
G4 fetched: 43 groups → 129 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   129 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 202 Row 6 Seats 13–14  avg $470/ea  total $940
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 46 groups, price range $862 – $6,670 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |       92.3% | May exist in G2, not top-100   |
| NEW        |     3 |        7.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 333 Row 21 Seats 21–22  avg $460/ea  total $920
Cheapest New: Sec 314 Row 20 Seats 9–10  avg $430/ea  total $860

## Category 4 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 3 groups, price range $1,208 – $1,725 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 30 Seats 1–2  avg $667/ea  total $1,334
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            345 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            129 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             36 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

