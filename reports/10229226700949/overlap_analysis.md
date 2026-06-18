## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 30 groups, price range $4,600 – $27,600 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 104 Row 34 Seats 9–10  avg $2,588/ea  total $5,176
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 29 groups, price range $3,450 – $11,500 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |       87.5% | May exist in G2, not top-100   |
| NEW        |     3 |       12.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 327 Row 14 Seats 5–6  avg $1,955/ea  total $3,910
Cheapest New: Sec 335 Row 14 Seats 13–14  avg $12,341/ea  total $24,682

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 9 groups, price range $3,450 – $16,454 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       33.3% | May exist in G2, not top-100   |
| NEW        |     6 |       66.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 302 Row 26 Seats 8–9  avg $2,300/ea  total $4,600
Cheapest New: Sec 302 Row 25 Seats 21–22  avg $1,711/ea  total $3,422

Pairs eligible for merge (NEW below G2 min $3,450): 3

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             27 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             21 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |              3 | DERIVE          |

Overall recommendation: **DERIVE**

