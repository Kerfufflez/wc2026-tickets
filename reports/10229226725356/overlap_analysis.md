## Category 1 — Pair Derivation Analysis
Date: July 8, 2026

G2 fetched: 281 groups, price range $4,255 – $345,000 total
G4 fetched: 131 groups → 393 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   393 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 125 Row 32 Seats 25–26  avg $2,706/ea  total $5,412
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 8, 2026

G2 fetched: 190 groups, price range $3,220 – $29,898 total
G4 fetched: 70 groups → 210 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   204 |       97.1% | May exist in G2, not top-100   |
| NEW        |     6 |        2.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 343 Row 35 Seats 16–17  avg $1,898/ea  total $3,796
Cheapest New: Sec 242 Row 8 Seats 13–14  avg $23,000/ea  total $46,000

Pairs eligible for merge (NEW below G2 min $3,220): 0

## Category 3 — Pair Derivation Analysis
Date: July 8, 2026

G2 fetched: 162 groups, price range $3,197 – $69,000 total
G4 fetched: 60 groups → 180 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   177 |       98.3% | May exist in G2, not top-100   |
| NEW        |     3 |        1.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 306 Row 19 Seats 13–14  avg $1,668/ea  total $3,336
Cheapest New: Sec 329 Row 31 Seats 17–18  avg $114,999/ea  total $229,998

## Category 4 — Pair Derivation Analysis
Date: July 8, 2026

G2 fetched: 5 groups, price range $2,988 – $20,125 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 318 Row 43 Seats 8–9  avg $4,456/ea  total $8,912
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            393 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            204 | DERIVE          |
| Cat 3    |       0.0% |         3 |            177 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

