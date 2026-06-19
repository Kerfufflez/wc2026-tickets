## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 58 groups, price range $1,610 – $8,050 total
G4 fetched: 42 groups → 126 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   123 |       97.6% | May exist in G2, not top-100   |
| NEW        |     3 |        2.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 108 Row 23 Seats 14–15  avg $820/ea  total $1,640
Cheapest New: Sec 124 Row 20 Seats 14–15  avg $748/ea  total $1,496

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 46 groups, price range $1,380 – $5,750 total
G4 fetched: 19 groups → 57 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    57 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 226 Row 22 Seats 3–4  avg $690/ea  total $1,380
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 32 groups, price range $1,380 – $5,060 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |       70.0% | May exist in G2, not top-100   |
| NEW        |     9 |       30.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 416 Row 11 Seats 5–6  avg $805/ea  total $1,610
Cheapest New: Sec 407 Row 3 Seats 6–7  avg $604/ea  total $1,208

Pairs eligible for merge (NEW below G2 min $1,380): 6

## Category 4 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 2 groups, price range $1,265 – $1,495 total
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
Cheapest New: Sec 422 Row 22 Seats 18–19  avg $851/ea  total $1,702

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            123 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             57 | INVESTIGATE     |
| Cat 3    |       0.0% |         9 |             21 | DERIVE          |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

