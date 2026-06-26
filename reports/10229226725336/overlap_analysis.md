## Category 1 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 304 groups, price range $5,750 – $115,000 total
G4 fetched: 109 groups → 327 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   327 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 130 Row 17 Seats 27–28  avg $3,220/ea  total $6,440
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 209 groups, price range $4,600 – $46,000 total
G4 fetched: 97 groups → 291 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   288 |       99.0% | May exist in G2, not top-100   |
| NEW        |     3 |        1.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 208 Row 18 Seats 1–2  avg $2,588/ea  total $5,176
Cheapest New: Sec 318 Row 1 Seats 26–27  avg $25,300/ea  total $50,600

## Category 3 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 140 groups, price range $4,082 – $32,200 total
G4 fetched: 57 groups → 171 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   168 |       98.2% | May exist in G2, not top-100   |
| NEW        |     3 |        1.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 402 Row 10 Seats 9–10  avg $2,300/ea  total $4,600
Cheapest New: Sec 403 Row 21 Seats 15–16  avg $2,012/ea  total $4,024

## Category 4 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 8 groups, price range $5,946 – $11,500 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 422 Row 16 Seats 2–3  avg $3,450/ea  total $6,900
Cheapest New: Sec 401 Row 18 Seats 23–24  avg $11,500/ea  total $23,000

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            327 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            288 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |            168 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **PARTIAL**

