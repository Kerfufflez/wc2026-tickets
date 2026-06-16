## Category 1 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 108 groups, price range $825 – $2,474 total
G4 fetched: 66 groups → 198 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   195 |       98.5% | May exist in G2, not top-100   |
| NEW        |     3 |        1.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 222 Row OO Seats 3–4  avg $449/ea  total $898
Cheapest New: Sec 244 Row T Seats 6–7  avg $1,319/ea  total $2,638

## Category 2 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 160 groups, price range $635 – $8,247 total
G4 fetched: 59 groups → 177 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   177 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 252 Row PP Seats 1–2  avg $414/ea  total $828
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 42 groups, price range $748 – $3,450 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 418 Row EE Seats 4–5  avg $412/ea  total $824
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 6 groups, price range $868 – $1,265 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 403 Row WW Seats 1–2  avg $529/ea  total $1,058
Cheapest New: Sec 428 Row XX Seats 2–3  avg $690/ea  total $1,380

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            195 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            177 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             45 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

