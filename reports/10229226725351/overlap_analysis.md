## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 104 groups, price range $4,600 – $75,900 total
G4 fetched: 49 groups → 147 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   147 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 116 Row 39 Seats 42–43  avg $2,600/ea  total $5,200
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 68 groups, price range $3,910 – $27,600 total
G4 fetched: 40 groups → 120 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   114 |       95.0% | May exist in G2, not top-100   |
| NEW        |     6 |        5.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 311 Row 12 Seats 15–16  avg $2,070/ea  total $4,140
Cheapest New: Sec 343 Row 18 Seats 12–13  avg $1,840/ea  total $3,680

Pairs eligible for merge (NEW below G2 min $3,910): 3

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 59 groups, price range $3,910 – $23,000 total
G4 fetched: 28 groups → 84 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |       96.4% | May exist in G2, not top-100   |
| NEW        |     3 |        3.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 319 Row 20 Seats 9–10  avg $1,955/ea  total $3,910
Cheapest New: Sec 306 Row 7 Seats 4–5  avg $1,898/ea  total $3,796

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            147 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            114 | DERIVE          |
| Cat 3    |       0.0% |         3 |             81 | INVESTIGATE     |

Overall recommendation: **DERIVE**

