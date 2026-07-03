## Category 1 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 228 groups, price range $2,050 – $2,990,000 total
G4 fetched: 85 groups → 255 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   255 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 114 Row 20 Seats 3–4  avg $1,044/ea  total $2,088
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 188 groups, price range $1,725 – $115,000 total
G4 fetched: 69 groups → 207 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   201 |       97.1% | May exist in G2, not top-100   |
| NEW        |     6 |        2.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec NE-T-2 Row 3 Seats 35–36  avg $914/ea  total $1,828
Cheapest New: Sec 223 Row 1 Seats 6–7  avg $805/ea  total $1,610

Pairs eligible for merge (NEW below G2 min $1,725): 3

## Category 3 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 80 groups, price range $1,725 – $27,140 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    42 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 214 Row 7 Seats 5–6  avg $894/ea  total $1,788
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 11 groups, price range $2,185 – $6,268 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 207 Row 24 Seats 13–14  avg $1,149/ea  total $2,298
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            255 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            201 | DERIVE          |
| Cat 3    |       0.0% |         0 |             42 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

