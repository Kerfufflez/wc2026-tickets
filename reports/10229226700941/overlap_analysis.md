## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 68 groups, price range $2,626 – $37,749 total
G4 fetched: 21 groups → 63 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    60 |       95.2% | May exist in G2, not top-100   |
| NEW        |     3 |        4.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 227 Row D Seats 1–2  avg $1,608/ea  total $3,216
Cheapest New: Sec 230 Row PP Seats 102–103  avg $1,231/ea  total $2,462

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 40 groups, price range $2,298 – $15,592 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |       92.9% | May exist in G2, not top-100   |
| NEW        |     3 |        7.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 434 Row WW Seats 5–6  avg $1,321/ea  total $2,642
Cheapest New: Sec 436 Row PP Seats 2–3  avg $102,580/ea  total $205,160

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 14 groups, price range $2,298 – $6,898 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 433 Row LL Seats 107–108  avg $1,494/ea  total $2,988
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             60 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             39 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

