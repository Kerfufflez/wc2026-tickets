## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 41 groups, price range $3,450 – $27,600 total
G4 fetched: 29 groups → 87 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    87 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 136 Row 21 Seats 5–6  avg $1,869/ea  total $3,738
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 51 groups, price range $2,530 – $11,500 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    30 |       83.3% | May exist in G2, not top-100   |
| NEW        |     6 |       16.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 305 Row 19 Seats 21–22  avg $1,380/ea  total $2,760
Cheapest New: Sec 336 Row 15 Seats 9–10  avg $1,259/ea  total $2,518

Pairs eligible for merge (NEW below G2 min $2,530): 6

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 10 groups, price range $2,012 – $16,493 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 302 Row 25 Seats 21–22  avg $1,711/ea  total $3,422
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             87 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             30 | DERIVE          |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

