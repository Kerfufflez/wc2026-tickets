## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 191 groups, price range $3,448 – $27,600 total
G4 fetched: 124 groups → 372 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   363 |       97.6% | May exist in G2, not top-100   |
| NEW        |     9 |        2.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 350 Row G Seats 17–18  avg $1,863/ea  total $3,726
Cheapest New: Sec 323 Row N Seats 9–10  avg $17,250/ea  total $34,500

Pairs eligible for merge (NEW below G2 min $3,448): 0

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 43 groups, price range $3,291 – $17,250 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    60 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 632 Row S Seats 8–9  avg $1,725/ea  total $3,450
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 21 groups, price range $3,220 – $23,000 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 644 Row E Seats 5–6  avg $2,128/ea  total $4,256
Cheapest New: Sec 625 Row E Seats 7–8  avg $14,375/ea  total $28,750

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            363 | DERIVE          |
| Cat 2    |       0.0% |         0 |             60 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **DERIVE**

