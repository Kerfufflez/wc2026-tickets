## Category 1 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 107 groups, price range $7,705 – $45,655 total
G4 fetched: 41 groups → 123 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   123 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 104 Row 18 Seats 1–2  avg $4,140/ea  total $8,280
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 65 groups, price range $6,555 – $34,500 total
G4 fetched: 28 groups → 84 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    78 |       92.9% | May exist in G2, not top-100   |
| NEW        |     6 |        7.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 337 Row 26 Seats 4–5  avg $3,448/ea  total $6,896
Cheapest New: Sec 314 Row 26 Seats 11–12  avg $2,588/ea  total $5,176

Pairs eligible for merge (NEW below G2 min $6,555): 6

## Category 3 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 60 groups, price range $6,325 – $23,000 total
G4 fetched: 25 groups → 75 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    75 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 328 Row 14 Seats 21–22  avg $3,245/ea  total $6,490
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            123 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             78 | DERIVE          |
| Cat 3    |       0.0% |         0 |             75 | INVESTIGATE     |

Overall recommendation: **DERIVE**

