## Category 1 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 262 groups, price range $2,082 – $2,990,000 total
G4 fetched: 101 groups → 303 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   288 |       95.0% | May exist in G2, not top-100   |
| NEW        |    15 |        5.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 112 Row 17 Seats 13–14  avg $1,092/ea  total $2,184
Cheapest New: Sec 113 Row 13 Seats 5–6  avg $978/ea  total $1,956

Pairs eligible for merge (NEW below G2 min $2,082): 15

## Category 2 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 232 groups, price range $1,426 – $115,000 total
G4 fetched: 75 groups → 225 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   225 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 224 Row 21 Seats 17–18  avg $920/ea  total $1,840
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 93 groups, price range $1,610 – $27,140 total
G4 fetched: 18 groups → 54 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    54 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 211 Row 9 Seats 5–6  avg $805/ea  total $1,610
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 16 groups, price range $1,610 – $6,268 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 207 Row 29 Seats 9–10  avg $846/ea  total $1,692
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |        15 |            288 | DERIVE          |
| Cat 2    |       0.0% |         0 |            225 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             54 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

