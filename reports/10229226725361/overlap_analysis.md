## Category 1 — Pair Derivation Analysis
Date: July 17, 2026

G2 fetched: 554 groups, price range $1,552 – $45,770 total
G4 fetched: 294 groups → 882 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   876 |       99.3% | May exist in G2, not top-100   |
| NEW        |     6 |        0.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 224 Row 7 Seats 11–12  avg $862/ea  total $1,724
Cheapest New: Sec 121 Row 7 Seats 21–22  avg $25,875/ea  total $51,750

Pairs eligible for merge (NEW below G2 min $1,552): 0

## Category 2 — Pair Derivation Analysis
Date: July 17, 2026

G2 fetched: 240 groups, price range $1,150 – $23,000 total
G4 fetched: 70 groups → 210 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   207 |       98.6% | May exist in G2, not top-100   |
| NEW        |     3 |        1.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 350 Row 19 Seats 11–12  avg $690/ea  total $1,380
Cheapest New: Sec 319 Row 18 Seats 3–4  avg $432,069/ea  total $864,138

## Category 3 — Pair Derivation Analysis
Date: July 17, 2026

G2 fetched: 94 groups, price range $1,462 – $80,500 total
G4 fetched: 29 groups → 87 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    87 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 307 Row 28 Seats 5–6  avg $731/ea  total $1,462
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 17, 2026

G2 fetched: 15 groups, price range $1,265 – $23,000 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 28 Seats 17–18  avg $1,725/ea  total $3,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            876 | DERIVE          |
| Cat 2    |       0.0% |         3 |            207 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             87 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

