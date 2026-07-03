## Category 1 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 315 groups, price range $1,564 – $127,650 total
G4 fetched: 146 groups → 438 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   438 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 324 Row H Seats 1–2  avg $920/ea  total $1,840
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 106 groups, price range $1,403 – $23,000 total
G4 fetched: 37 groups → 111 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   105 |       94.6% | May exist in G2, not top-100   |
| NEW        |     6 |        5.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 631 Row J Seats 11–12  avg $805/ea  total $1,610
Cheapest New: Sec 639 Row M Seats 17–18  avg $658/ea  total $1,316

Pairs eligible for merge (NEW below G2 min $1,403): 6

## Category 3 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 57 groups, price range $1,265 – $6,658 total
G4 fetched: 17 groups → 51 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |       88.2% | May exist in G2, not top-100   |
| NEW        |     6 |       11.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 748 Row Q Seats 3–4  avg $805/ea  total $1,610
Cheapest New: Sec 615 Row N Seats 9–10  avg $632/ea  total $1,264

Pairs eligible for merge (NEW below G2 min $1,265): 3

## Category 4 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 4 groups, price range $1,150 – $4,025 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 718 Row P Seats 1–2  avg $1,074/ea  total $2,148
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            438 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            105 | DERIVE          |
| Cat 3    |       0.0% |         6 |             45 | DERIVE          |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

