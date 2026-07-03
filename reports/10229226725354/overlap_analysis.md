## Category 1 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 170 groups, price range $9,200 – $624,012 total
G4 fetched: 58 groups → 174 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   174 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 234 Row 27 Seats 1–2  avg $4,600/ea  total $9,200
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 264 groups, price range $6,399 – $46,000 total
G4 fetched: 100 groups → 300 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   294 |       98.0% | May exist in G2, not top-100   |
| NEW        |     6 |        2.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 536 Row 13 Seats 17–18  avg $3,444/ea  total $6,888
Cheapest New: Sec 352 Row 4 Seats 13–14  avg $25,875/ea  total $51,750

Pairs eligible for merge (NEW below G2 min $6,399): 0

## Category 3 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 70 groups, price range $5,670 – $69,000 total
G4 fetched: 24 groups → 72 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    72 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 528 Row 14 Seats 11–12  avg $2,990/ea  total $5,980
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 3, 2026

G2 fetched: 3 groups, price range $9,430 – $16,100 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 526 Row 16 Seats 5–6  avg $6,900/ea  total $13,800
Cheapest New: Sec 553 Row 13 Seats 10–11  avg $9,775/ea  total $19,550

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            174 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            294 | DERIVE          |
| Cat 3    |       0.0% |         0 |             72 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

