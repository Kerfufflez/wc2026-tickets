## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 28 groups, price range $4,370 – $27,600 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 18 Seats 9–10  avg $3,162/ea  total $6,324
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 24 groups, price range $3,910 – $17,250 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 327 Row 14 Seats 5–6  avg $2,070/ea  total $4,140
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 6 groups, price range $4,600 – $16,486 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 302 Row 26 Seats 8–9  avg $2,300/ea  total $4,600
Cheapest New: Sec 304 Row 13 Seats 9–10  avg $2,932,500/ea  total $5,865,000

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             27 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             15 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

