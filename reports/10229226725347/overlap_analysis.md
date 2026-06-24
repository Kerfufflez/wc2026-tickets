## Category 1 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 116 groups, price range $6,898 – $57,500 total
G4 fetched: 81 groups → 243 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   237 |       97.5% | May exist in G2, not top-100   |
| NEW        |     6 |        2.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 124 Row 38 Seats 4–5  avg $3,450/ea  total $6,900
Cheapest New: Sec 104 Row 35 Seats 20–21  avg $3,416/ea  total $6,832

Pairs eligible for merge (NEW below G2 min $6,898): 3

## Category 2 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 156 groups, price range $5,244 – $43,470 total
G4 fetched: 71 groups → 213 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   210 |       98.6% | May exist in G2, not top-100   |
| NEW        |     3 |        1.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 317 Row 13 Seats 1–2  avg $2,645/ea  total $5,290
Cheapest New: Sec 334 Row 8 Seats 9–10  avg $2,530/ea  total $5,060

## Category 3 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 51 groups, price range $4,890 – $23,000 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    75 |       92.6% | May exist in G2, not top-100   |
| NEW        |     6 |        7.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 307 Row 13 Seats 6–7  avg $2,645/ea  total $5,290
Cheapest New: Sec 350 Row 14 Seats 4–5  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $4,890): 0

## Category 4 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 3 groups, price range $7,475 – $44,850 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 321 Row 19 Seats 9–10  avg $4,025/ea  total $8,050
Cheapest New: Sec 346 Row 26 Seats 8–9  avg $2,961/ea  total $5,922

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            237 | DERIVE          |
| Cat 2    |       0.0% |         3 |            210 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             75 | DERIVE          |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

