## Category 1 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 235 groups, price range $1,932 – $46,000 total
G4 fetched: 133 groups → 399 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   399 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 123 Row 48 Seats 1–2  avg $1,035/ea  total $2,070
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 255 groups, price range $1,610 – $11,500 total
G4 fetched: 111 groups → 333 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   324 |       97.3% | May exist in G2, not top-100   |
| NEW        |     9 |        2.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 333 Row 23 Seats 9–10  avg $862/ea  total $1,724
Cheapest New: Sec 309 Row 3 Seats 3–4  avg $6,670/ea  total $13,340

Pairs eligible for merge (NEW below G2 min $1,610): 0

## Category 3 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 81 groups, price range $1,306 – $12,880 total
G4 fetched: 34 groups → 102 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   102 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 325 Row 23 Seats 21–22  avg $889/ea  total $1,778
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 29, 2026

G2 fetched: 9 groups, price range $2,070 – $11,500 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 346 Row 20 Seats 5–6  avg $1,725/ea  total $3,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            399 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |            324 | DERIVE          |
| Cat 3    |       0.0% |         0 |            102 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

