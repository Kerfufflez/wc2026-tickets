## Category 1 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 124 groups, price range $6,900 – $57,500 total
G4 fetched: 73 groups → 219 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   216 |       98.6% | May exist in G2, not top-100   |
| NEW        |     3 |        1.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 124 Row 38 Seats 4–5  avg $3,450/ea  total $6,900
Cheapest New: Sec 104 Row 43 Seats 17–18  avg $401,350/ea  total $802,700

## Category 2 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 158 groups, price range $5,290 – $43,470 total
G4 fetched: 65 groups → 195 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   195 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 313 Row 24 Seats 9–10  avg $3,151/ea  total $6,302
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 52 groups, price range $5,060 – $23,000 total
G4 fetched: 28 groups → 84 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    78 |       92.9% | May exist in G2, not top-100   |
| NEW        |     6 |        7.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 307 Row 13 Seats 6–7  avg $2,645/ea  total $5,290
Cheapest New: Sec 350 Row 14 Seats 4–5  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $5,060): 0

## Category 4 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 4 groups, price range $6,636 – $44,850 total
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
| Cat 1    |       0.0% |         3 |            216 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            195 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             78 | DERIVE          |
| Cat 4    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

