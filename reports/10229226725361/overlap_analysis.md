## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 427 groups, price range $3,450 – $92,000 total
G4 fetched: 276 groups → 828 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   819 |       98.9% | May exist in G2, not top-100   |
| NEW        |     9 |        1.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 229 Row 6 Seats 21–22  avg $1,725/ea  total $3,450
Cheapest New: Sec 106 Row 29 Seats 10–11  avg $53,342/ea  total $106,684

Pairs eligible for merge (NEW below G2 min $3,450): 0

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 161 groups, price range $2,875 – $46,000 total
G4 fetched: 68 groups → 204 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   201 |       98.5% | May exist in G2, not top-100   |
| NEW        |     3 |        1.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 342 Row 18 Seats 7–8  avg $1,449/ea  total $2,898
Cheapest New: Sec 320 Row 20 Seats 17–18  avg $25,300/ea  total $50,600

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 59 groups, price range $2,873 – $271,400 total
G4 fetched: 19 groups → 57 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    57 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 304 Row 20 Seats 21–22  avg $1,610/ea  total $3,220
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 7 groups, price range $2,965 – $16,100 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 308 Row 26 Seats 1–2  avg $3,450/ea  total $6,900
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            819 | DERIVE          |
| Cat 2    |       0.0% |         3 |            201 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             57 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

