## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 141 groups, price range $823 – $2,474 total
G4 fetched: 83 groups → 249 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   246 |       98.8% | May exist in G2, not top-100   |
| NEW        |     3 |        1.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 221 Row LL Seats 7–8  avg $412/ea  total $824
Cheapest New: Sec 244 Row T Seats 6–7  avg $1,319/ea  total $2,638

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 188 groups, price range $635 – $8,247 total
G4 fetched: 84 groups → 252 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   252 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 227 Row B Seats 1–2  avg $345/ea  total $690
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 52 groups, price range $632 – $3,450 total
G4 fetched: 21 groups → 63 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    63 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 420 Row UU Seats 104–105  avg $402/ea  total $804
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 5 groups, price range $805 – $1,265 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 429 Row YY Seats 1–2  avg $437/ea  total $874
Cheapest New: Sec 428 Row XX Seats 2–3  avg $690/ea  total $1,380

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            246 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            252 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             63 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

