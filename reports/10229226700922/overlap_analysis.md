## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 117 groups, price range $920 – $11,500 total
G4 fetched: 64 groups → 192 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   192 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 115 Row 20 Seats 5–6  avg $575/ea  total $1,150
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 81 groups, price range $918 – $2,530 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    75 |       92.6% | May exist in G2, not top-100   |
| NEW        |     6 |        7.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 321 Row 8 Seats 1–2  avg $518/ea  total $1,036
Cheapest New: Sec 205 Row 6 Seats 17–18  avg $1,610/ea  total $3,220

Pairs eligible for merge (NEW below G2 min $918): 0

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 35 groups, price range $690 – $655,500 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 305 Row 6 Seats 5–6  avg $518/ea  total $1,036
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            192 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             75 | DERIVE          |
| Cat 3    |       0.0% |         0 |             27 | INVESTIGATE     |

Overall recommendation: **DERIVE**

