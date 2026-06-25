## Category 1 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 34 groups, price range $3,907 – $18,400 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |       90.0% | May exist in G2, not top-100   |
| NEW        |     3 |       10.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 140 Row 35 Seats 13–14  avg $2,818/ea  total $5,636
Cheapest New: Sec 102 Row 17 Seats 11–12  avg $11,500/ea  total $23,000

## Category 2 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 13 groups, price range $3,567 – $6,888 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |       75.0% | May exist in G2, not top-100   |
| NEW        |     6 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 314 Row 1 Seats 1–2  avg $2,068/ea  total $4,136
Cheapest New: Sec 311 Row 2 Seats 15–16  avg $3,738/ea  total $7,476

Pairs eligible for merge (NEW below G2 min $3,567): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             27 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             18 | DERIVE          |

Overall recommendation: **DERIVE**

