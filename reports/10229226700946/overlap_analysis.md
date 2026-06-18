## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 51 groups, price range $1,353 – $27,060 total
G4 fetched: 30 groups → 90 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    90 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 132 Row 28 Seats 19–20  avg $748/ea  total $1,496
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 77 groups, price range $869 – $3,703 total
G4 fetched: 37 groups → 111 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   105 |       94.6% | May exist in G2, not top-100   |
| NEW        |     6 |        5.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 346 Row 36 Seats 19–20  avg $575/ea  total $1,150
Cheapest New: Sec 127 Row 31 Seats 21–22  avg $2,300/ea  total $4,600

Pairs eligible for merge (NEW below G2 min $869): 0

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 28 groups, price range $978 – $2,576 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |       90.0% | May exist in G2, not top-100   |
| NEW        |     3 |       10.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 317 Row 15 Seats 11–12  avg $575/ea  total $1,150
Cheapest New: Sec 340 Row 17 Seats 16–17  avg $3,297/ea  total $6,594

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             90 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            105 | DERIVE          |
| Cat 3    |       0.0% |         3 |             27 | INVESTIGATE     |

Overall recommendation: **DERIVE**

