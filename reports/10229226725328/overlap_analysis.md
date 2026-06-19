## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 98 groups, price range $4,255 – $52,900 total
G4 fetched: 58 groups → 174 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   174 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 205 Row 15 Seats 10–11  avg $2,300/ea  total $4,600
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 105 groups, price range $3,116 – $16,100 total
G4 fetched: 63 groups → 189 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   180 |       95.2% | May exist in G2, not top-100   |
| NEW        |     9 |        4.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 510 Row 15 Seats 3–4  avg $1,653/ea  total $3,306
Cheapest New: Sec 543 Row 12 Seats 10–11  avg $8,625/ea  total $17,250

Pairs eligible for merge (NEW below G2 min $3,116): 0

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 32 groups, price range $3,220 – $46,552 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 506 Row 18 Seats 5–6  avg $1,724/ea  total $3,448
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            174 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |            180 | DERIVE          |
| Cat 3    |       0.0% |         0 |             27 | INVESTIGATE     |

Overall recommendation: **DERIVE**

