## Category 1 — Pair Derivation Analysis
Date: July 4, 2026

G2 fetched: 175 groups, price range $9,545 – $622,241 total
G4 fetched: 57 groups → 171 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   171 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 234 Row 19 Seats 13–14  avg $5,175/ea  total $10,350
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 4, 2026

G2 fetched: 265 groups, price range $6,601 – $46,000 total
G4 fetched: 112 groups → 336 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   330 |       98.2% | May exist in G2, not top-100   |
| NEW        |     6 |        1.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 536 Row 13 Seats 17–18  avg $3,444/ea  total $6,888
Cheapest New: Sec 352 Row 4 Seats 13–14  avg $25,875/ea  total $51,750

Pairs eligible for merge (NEW below G2 min $6,601): 0

## Category 3 — Pair Derivation Analysis
Date: July 4, 2026

G2 fetched: 70 groups, price range $6,900 – $46,000 total
G4 fetched: 22 groups → 66 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    57 |       86.4% | May exist in G2, not top-100   |
| NEW        |     9 |       13.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 532 Row 21 Seats 17–18  avg $3,680/ea  total $7,360
Cheapest New: Sec 528 Row 14 Seats 11–12  avg $2,990/ea  total $5,980

Pairs eligible for merge (NEW below G2 min $6,900): 3

## Category 4 — Pair Derivation Analysis
Date: July 4, 2026

G2 fetched: 4 groups, price range $7,015 – $16,100 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 526 Row 16 Seats 5–6  avg $6,900/ea  total $13,800
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            171 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            330 | DERIVE          |
| Cat 3    |       0.0% |         9 |             57 | DERIVE          |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

