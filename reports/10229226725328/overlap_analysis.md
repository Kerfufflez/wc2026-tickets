## Category 1 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 182 groups, price range $3,910 – $204,217 total
G4 fetched: 87 groups → 261 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   261 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 206 Row 9 Seats 3–4  avg $2,099/ea  total $4,198
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 159 groups, price range $2,811 – $11,500 total
G4 fetched: 86 groups → 258 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   240 |       93.0% | May exist in G2, not top-100   |
| NEW        |    18 |        7.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 455 Row 4 Seats 1–2  avg $1,673/ea  total $3,346
Cheapest New: Sec 425 Row 5 Seats 12–13  avg $6,325/ea  total $12,650

Pairs eligible for merge (NEW below G2 min $2,811): 0

## Category 3 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 50 groups, price range $3,220 – $23,552 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    42 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 534 Row 10 Seats 8–9  avg $1,725/ea  total $3,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            261 | INVESTIGATE     |
| Cat 2    |       0.0% |        18 |            240 | DERIVE          |
| Cat 3    |       0.0% |         0 |             42 | INVESTIGATE     |

Overall recommendation: **DERIVE**

