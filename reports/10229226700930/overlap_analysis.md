## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 60 groups, price range $1,955 – $11,847 total
G4 fetched: 25 groups → 75 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    72 |       96.0% | May exist in G2, not top-100   |
| NEW        |     3 |        4.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 131 Row 20 Seats 11–12  avg $1,035/ea  total $2,070
Cheapest New: Sec 111 Row 32 Seats 10–11  avg $799/ea  total $1,598

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 34 groups, price range $1,316 – $6,900 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    54 |       90.0% | May exist in G2, not top-100   |
| NEW        |     6 |       10.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 225 Row 30 Seats 19–20  avg $684/ea  total $1,368
Cheapest New: Sec C18 Row 3 Seats 3–4  avg $3,594/ea  total $7,188

Pairs eligible for merge (NEW below G2 min $1,316): 0

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 20 groups, price range $1,656 – $5,750 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 228 Row 19 Seats 5–6  avg $978/ea  total $1,956
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 1 groups, price range $2,760 – $2,760 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     9 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 207 Row 25 Seats 3–4  avg $1,150/ea  total $2,300

Pairs eligible for merge (NEW below G2 min $2,760): 3

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             72 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             54 | DERIVE          |
| Cat 3    |       0.0% |         0 |             21 | INVESTIGATE     |
| Cat 4    |       0.0% |         9 |              0 | DERIVE          |

Overall recommendation: **DERIVE**

