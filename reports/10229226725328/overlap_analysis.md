## Category 1 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 254 groups, price range $3,680 – $204,217 total
G4 fetched: 131 groups → 393 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   393 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 206 Row 14 Seats 1–2  avg $2,275/ea  total $4,550
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 229 groups, price range $2,418 – $14,950 total
G4 fetched: 113 groups → 339 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   333 |       98.2% | May exist in G2, not top-100   |
| NEW        |     6 |        1.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 539 Row 18 Seats 22–23  avg $1,501/ea  total $3,002
Cheapest New: Sec 312 Row 9 Seats 11–12  avg $9,936/ea  total $19,872

Pairs eligible for merge (NEW below G2 min $2,418): 0

## Category 3 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 64 groups, price range $2,254 – $18,952 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 529 Row 22 Seats 14–15  avg $1,380/ea  total $2,760
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            393 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            333 | DERIVE          |
| Cat 3    |       0.0% |         0 |             81 | INVESTIGATE     |

Overall recommendation: **DERIVE**

