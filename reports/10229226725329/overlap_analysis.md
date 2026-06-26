## Category 1 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 177 groups, price range $2,760 – $13,800 total
G4 fetched: 76 groups → 228 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   216 |       94.7% | May exist in G2, not top-100   |
| NEW        |    12 |        5.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 101 Row 23 Seats 6–7  avg $1,380/ea  total $2,760
Cheapest New: Sec 140 Row 31 Seats 1–2  avg $1,357/ea  total $2,714

Pairs eligible for merge (NEW below G2 min $2,760): 3

## Category 2 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 148 groups, price range $1,955 – $23,000 total
G4 fetched: 79 groups → 237 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   234 |       98.7% | May exist in G2, not top-100   |
| NEW        |     3 |        1.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 337 Row 3 Seats 17–18  avg $1,150/ea  total $2,300
Cheapest New: Sec 225 Row 6 Seats 6–7  avg $13,799/ea  total $27,598

## Category 3 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 16 groups, price range $2,242 – $7,590 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 303 Row 21 Seats 20–21  avg $1,230/ea  total $2,460
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |        12 |            216 | DERIVE          |
| Cat 2    |       0.0% |         3 |            234 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

