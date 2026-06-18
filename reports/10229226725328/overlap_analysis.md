## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 100 groups, price range $4,255 – $52,900 total
G4 fetched: 61 groups → 183 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   183 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 207 Row 19 Seats 1–2  avg $2,171/ea  total $4,342
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 107 groups, price range $2,732 – $16,100 total
G4 fetched: 73 groups → 219 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   207 |       94.5% | May exist in G2, not top-100   |
| NEW        |    12 |        5.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 544 Row 18 Seats 13–14  avg $1,380/ea  total $2,760
Cheapest New: Sec 543 Row 12 Seats 10–11  avg $8,625/ea  total $17,250

Pairs eligible for merge (NEW below G2 min $2,732): 0

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 35 groups, price range $2,405 – $46,552 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    30 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 530 Row 21 Seats 1–2  avg $1,530/ea  total $3,060
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 1 groups, price range $3,448 – $3,448 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     3 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 525 Row 12 Seats 3–4  avg $1,840/ea  total $3,680

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            183 | INVESTIGATE     |
| Cat 2    |       0.0% |        12 |            207 | DERIVE          |
| Cat 3    |       0.0% |         0 |             30 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

