## Category 1 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 125 groups, price range $4,600 – $20,700 total
G4 fetched: 57 groups → 171 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   168 |       98.2% | May exist in G2, not top-100   |
| NEW        |     3 |        1.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 140 Row Z Seats 1–2  avg $2,415/ea  total $4,830
Cheapest New: Sec 111 Row AA Seats 13–14  avg $11,500/ea  total $23,000

## Category 2 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 37 groups, price range $4,255 – $13,798 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |       92.9% | May exist in G2, not top-100   |
| NEW        |     3 |        7.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 632 Row T Seats 17–18  avg $2,185/ea  total $4,370
Cheapest New: Sec 518 Row J Seats 1–2  avg $2,104/ea  total $4,208

## Category 3 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 14 groups, price range $4,025 – $13,524 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 645 Row E Seats 9–10  avg $2,300/ea  total $4,600
Cheapest New: Sec 628 Row L Seats 6–7  avg $11,500/ea  total $23,000

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            168 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             39 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

