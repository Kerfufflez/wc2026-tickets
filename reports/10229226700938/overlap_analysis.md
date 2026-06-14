## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 46 groups, price range $1,000 – $5,750 total
G4 fetched: 45 groups → 135 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   135 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 29 Seats 5–6  avg $518/ea  total $1,036
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 98 groups, price range $814 – $3,450 total
G4 fetched: 78 groups → 234 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   225 |       96.2% | May exist in G2, not top-100   |
| NEW        |     9 |        3.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 122 Row 34 Seats 12–13  avg $430/ea  total $860
Cheapest New: Sec 122 Row 36 Seats 31–32  avg $1,854/ea  total $3,708

Pairs eligible for merge (NEW below G2 min $814): 0

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 104 groups, price range $736 – $9,200 total
G4 fetched: 41 groups → 123 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   123 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 332 Row 12 Seats 6–7  avg $371/ea  total $742
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 6 groups, price range $888 – $2,300 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       50.0% | May exist in G2, not top-100   |
| NEW        |     6 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 311 Row 30 Seats 9–10  avg $690/ea  total $1,380
Cheapest New: Sec 313 Row 31 Seats 21–22  avg $402/ea  total $804

Pairs eligible for merge (NEW below G2 min $888): 6

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            135 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |            225 | DERIVE          |
| Cat 3    |       0.0% |         0 |            123 | INVESTIGATE     |
| Cat 4    |       0.0% |         6 |              6 | DERIVE          |

Overall recommendation: **DERIVE**

