## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 142 groups, price range $7,666 – $1,150,000 total
G4 fetched: 93 groups → 279 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   276 |       98.9% | May exist in G2, not top-100   |
| NEW        |     3 |        1.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 107 Row 13 Seats 15–16  avg $4,140/ea  total $8,280
Cheapest New: Sec 253CC Row 1 Seats 9–10  avg $3,738/ea  total $7,476

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 40 groups, price range $6,325 – $27,600 total
G4 fetched: 24 groups → 72 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    69 |       95.8% | May exist in G2, not top-100   |
| NEW        |     3 |        4.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 321 Row 24 Seats 4–5  avg $3,450/ea  total $6,900
Cheapest New: Sec 318 Row 25 Seats 13–14  avg $16,100/ea  total $32,200

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 28 groups, price range $6,095 – $32,200 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 330 Row 30 Seats 15–16  avg $3,278/ea  total $6,556
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 5 groups, price range $6,210 – $11,958 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 356 Row 28 Seats 11–12  avg $5,232/ea  total $10,464
Cheapest New: Sec 328 Row 24 Seats 13–14  avg $17,250/ea  total $34,500

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            276 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             69 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             36 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              6 | SKIP            |

Overall recommendation: **PARTIAL**

