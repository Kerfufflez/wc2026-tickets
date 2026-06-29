## Category 1 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 221 groups, price range $6,785 – $129,030 total
G4 fetched: 78 groups → 234 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   234 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 104 Row 35 Seats 17–18  avg $3,910/ea  total $7,820
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 195 groups, price range $5,727 – $59,570 total
G4 fetched: 84 groups → 252 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   249 |       98.8% | May exist in G2, not top-100   |
| NEW        |     3 |        1.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 327 Row 15 Seats 21–22  avg $3,200/ea  total $6,400
Cheapest New: Sec 305 Row 11 Seats 4–5  avg $2,760/ea  total $5,520

## Category 3 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 11 groups, price range $4,991 – $20,700 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 316 Row 12 Seats 17–18  avg $2,990/ea  total $5,980
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            234 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            249 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

