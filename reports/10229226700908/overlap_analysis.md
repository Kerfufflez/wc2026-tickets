## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 111 groups, price range $742 – $4,485 total
G4 fetched: 94 groups → 282 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   267 |       94.7% | May exist in G2, not top-100   |
| NEW        |    15 |        5.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 132 Row 12 Seats 20–21  avg $402/ea  total $804
Cheapest New: Sec 128 Row 16 Seats 13–14  avg $345/ea  total $690

Pairs eligible for merge (NEW below G2 min $742): 15

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 154 groups, price range $288 – $1,055,700 total
G4 fetched: 110 groups → 330 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   330 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 127 Row 33 Seats 21–22  avg $305/ea  total $610
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 129 groups, price range $455 – $3,450 total
G4 fetched: 48 groups → 144 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   141 |       97.9% | May exist in G2, not top-100   |
| NEW        |     3 |        2.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 416 Row 26 Seats 13–14  avg $231/ea  total $462
Cheapest New: Sec 422 Row 1 Seats 1–2  avg $3,450/ea  total $6,900

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 9 groups, price range $460 – $3,657 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 401 Row 26 Seats 17–18  avg $345/ea  total $690
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |        15 |            267 | DERIVE          |
| Cat 2    |       0.0% |         0 |            330 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |            141 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

