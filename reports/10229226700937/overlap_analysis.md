## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 54 groups, price range $5,060 – $16,100 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    60 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 231 Row 3 Seats 19–20  avg $2,869/ea  total $5,738
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 25 groups, price range $5,416 – $43,068 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    30 |       90.9% | May exist in G2, not top-100   |
| NEW        |     3 |        9.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 348 Row 29 Seats 13–14  avg $2,818/ea  total $5,636
Cheapest New: Sec 321 Row 18 Seats 1–2  avg $2,645/ea  total $5,290

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 7 groups, price range $5,078 – $11,500 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 332 Row 22 Seats 13–14  avg $2,588/ea  total $5,176
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             60 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             30 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **PARTIAL**

