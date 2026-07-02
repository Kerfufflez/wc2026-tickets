## Category 1 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 159 groups, price range $9,725 – $624,012 total
G4 fetched: 57 groups → 171 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   171 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 201 Row 15 Seats 18–19  avg $5,175/ea  total $10,350
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 244 groups, price range $5,996 – $46,000 total
G4 fetched: 92 groups → 276 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   270 |       97.8% | May exist in G2, not top-100   |
| NEW        |     6 |        2.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 536 Row 11 Seats 1–2  avg $3,004/ea  total $6,008
Cheapest New: Sec 352 Row 4 Seats 13–14  avg $25,875/ea  total $51,750

Pairs eligible for merge (NEW below G2 min $5,996): 0

## Category 3 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 64 groups, price range $5,980 – $69,000 total
G4 fetched: 22 groups → 66 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    66 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 528 Row 14 Seats 11–12  avg $3,278/ea  total $6,556
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 2, 2026

G2 fetched: 2 groups, price range $14,950 – $16,100 total
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
Cheapest New: Sec 504 Row 21 Seats 1–2  avg $16,445/ea  total $32,890

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            171 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            270 | DERIVE          |
| Cat 3    |       0.0% |         0 |             66 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

