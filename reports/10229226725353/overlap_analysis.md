## Category 1 — Pair Derivation Analysis
Date: July 8, 2026

G2 fetched: 282 groups, price range $2,530 – $80,500 total
G4 fetched: 83 groups → 249 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   249 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 117 Row 22 Seats 1–2  avg $1,400/ea  total $2,800
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 8, 2026

G2 fetched: 233 groups, price range $2,046 – $4,140,000 total
G4 fetched: 100 groups → 300 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   300 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 305 Row 25 Seats 18–19  avg $1,024/ea  total $2,048
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 8, 2026

G2 fetched: 22 groups, price range $2,530 – $17,250 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       50.0% | May exist in G2, not top-100   |
| NEW        |     6 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 317 Row 16 Seats 9–10  avg $1,495/ea  total $2,990
Cheapest New: Sec 301 Row 11 Seats 5–6  avg $1,150/ea  total $2,300

Pairs eligible for merge (NEW below G2 min $2,530): 6

## Category 4 — Pair Derivation Analysis
Date: July 8, 2026

G2 fetched: 9 groups, price range $2,300 – $6,831 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 323 Row 25 Seats 1–2  avg $1,725/ea  total $3,450
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            249 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            300 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |              6 | DERIVE          |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

