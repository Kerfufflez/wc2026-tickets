## Category 1 — Pair Derivation Analysis
Date: July 18, 2026

G2 fetched: 426 groups, price range $1,150 – $20,470 total
G4 fetched: 192 groups → 576 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   570 |       99.0% | May exist in G2, not top-100   |
| NEW        |     6 |        1.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 106 Row 32 Seats 15–16  avg $678/ea  total $1,356
Cheapest New: Sec 121 Row 7 Seats 21–22  avg $10,350/ea  total $20,700

Pairs eligible for merge (NEW below G2 min $1,150): 0

## Category 2 — Pair Derivation Analysis
Date: July 18, 2026

G2 fetched: 178 groups, price range $1,035 – $23,000 total
G4 fetched: 39 groups → 117 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   114 |       97.4% | May exist in G2, not top-100   |
| NEW        |     3 |        2.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 322 Row 18 Seats 1–2  avg $575/ea  total $1,150
Cheapest New: Sec 319 Row 18 Seats 3–4  avg $431,897/ea  total $863,794

## Category 3 — Pair Derivation Analysis
Date: July 18, 2026

G2 fetched: 78 groups, price range $1,150 – $11,500 total
G4 fetched: 17 groups → 51 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    51 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 330 Row 29 Seats 5–6  avg $600/ea  total $1,200
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 18, 2026

G2 fetched: 8 groups, price range $1,150 – $5,750 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 336 Row 28 Seats 25–26  avg $1,552/ea  total $3,104
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            570 | DERIVE          |
| Cat 2    |       0.0% |         3 |            114 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             51 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

