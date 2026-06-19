## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 19 groups, price range $1,725 – $5,750 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 135 Row 13 Seats 13–14  avg $920/ea  total $1,840
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 42 groups, price range $1,324 – $1,265,000 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 341 Row 16 Seats 7–8  avg $690/ea  total $1,380
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 32 groups, price range $1,254 – $5,497 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |       86.7% | May exist in G2, not top-100   |
| NEW        |     6 |       13.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 304 Row 12 Seats 9–10  avg $632/ea  total $1,264
Cheapest New: Sec 308 Row 11 Seats 5–6  avg $604/ea  total $1,208

Pairs eligible for merge (NEW below G2 min $1,254): 6

## Category 4 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 3 groups, price range $2,300 – $2,760 total
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
Cheapest New: Sec 313 Row 29 Seats 21–22  avg $690/ea  total $1,380

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             36 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             33 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             39 | DERIVE          |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

