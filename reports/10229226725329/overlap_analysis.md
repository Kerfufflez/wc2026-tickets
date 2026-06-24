## Category 1 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 126 groups, price range $3,575 – $16,100 total
G4 fetched: 68 groups → 204 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   195 |       95.6% | May exist in G2, not top-100   |
| NEW        |     9 |        4.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 115 Row 30 Seats 13–14  avg $1,840/ea  total $3,680
Cheapest New: Sec 124 Row 26 Seats 13–14  avg $9,200/ea  total $18,400

Pairs eligible for merge (NEW below G2 min $3,575): 0

## Category 2 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 100 groups, price range $2,760 – $23,000 total
G4 fetched: 63 groups → 189 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   186 |       98.4% | May exist in G2, not top-100   |
| NEW        |     3 |        1.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 307 Row 14 Seats 7–8  avg $1,610/ea  total $3,220
Cheapest New: Sec 312 Row 17 Seats 5–6  avg $1,265/ea  total $2,530

## Category 3 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 10 groups, price range $3,220 – $7,590 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 317 Row 17 Seats 18–19  avg $1,840/ea  total $3,680
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            195 | DERIVE          |
| Cat 2    |       0.0% |         3 |            186 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

