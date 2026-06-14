## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 21 groups, price range $5,290 – $11,500 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |       85.7% | May exist in G2, not top-100   |
| NEW        |     3 |       14.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 124 Row X Seats 2–3  avg $2,875/ea  total $5,750
Cheapest New: Sec 118 Row II Seats 17–18  avg $2,530/ea  total $5,060

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 13 groups, price range $4,140 – $11,500 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       50.0% | May exist in G2, not top-100   |
| NEW        |    12 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 340 Row B Seats 1–2  avg $2,472/ea  total $4,944
Cheapest New: Sec 305 Row Z Seats 10–11  avg $1,955/ea  total $3,910

Pairs eligible for merge (NEW below G2 min $4,140): 6

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 13 groups, price range $4,025 – $18,400 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 328 Row U Seats 33–34  avg $2,299/ea  total $4,598
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             18 | INVESTIGATE     |
| Cat 2    |       0.0% |        12 |             12 | DERIVE          |
| Cat 3    |       0.0% |         0 |             12 | INVESTIGATE     |

Overall recommendation: **DERIVE**

