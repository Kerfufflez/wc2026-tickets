## Category 1 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 24 groups, price range $1,725 – $8,050 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |       90.0% | May exist in G2, not top-100   |
| NEW        |     3 |       10.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 125 Row 15 Seats 21–22  avg $1,570/ea  total $3,140
Cheapest New: Sec C307 Row 5 Seats 6–7  avg $4,600/ea  total $9,200

## Category 2 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 19 groups, price range $1,895 – $4,600 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 417 Row 24 Seats 11–12  avg $1,150/ea  total $2,300
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             27 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

