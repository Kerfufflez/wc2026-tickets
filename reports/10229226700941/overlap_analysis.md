## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 67 groups, price range $2,934 – $14,670 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 201 Row NN Seats 103–104  avg $1,995/ea  total $3,990
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 26 groups, price range $2,690 – $15,485 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 436 Row CC Seats 102–103  avg $1,467/ea  total $2,934
Cheapest New: Sec 436 Row PP Seats 2–3  avg $101,876/ea  total $203,752

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 7 groups, price range $2,364 – $5,288 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     3 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 402 Row KK Seats 7–8  avg $2,853/ea  total $5,706

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             15 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |              9 | SKIP            |
| Cat 3    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **PARTIAL**

