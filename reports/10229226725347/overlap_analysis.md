## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 110 groups, price range $5,405 – $39,100 total
G4 fetched: 79 groups → 237 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   231 |       97.5% | May exist in G2, not top-100   |
| NEW        |     6 |        2.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 129 Row 23 Seats 10–11  avg $3,220/ea  total $6,440
Cheapest New: Sec 149 Row 34 Seats 24–25  avg $34,477/ea  total $68,954

Pairs eligible for merge (NEW below G2 min $5,405): 0

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 157 groups, price range $4,025 – $43,470 total
G4 fetched: 78 groups → 234 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   234 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 317 Row 9 Seats 5–6  avg $2,242/ea  total $4,484
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 56 groups, price range $3,889 – $23,000 total
G4 fetched: 29 groups → 87 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |       93.1% | May exist in G2, not top-100   |
| NEW        |     6 |        6.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 305 Row 19 Seats 25–26  avg $2,179/ea  total $4,358
Cheapest New: Sec 350 Row 14 Seats 4–5  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $3,889): 0

## Category 4 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 4 groups, price range $5,744 – $44,850 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 346 Row 26 Seats 8–9  avg $2,961/ea  total $5,922
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            231 | DERIVE          |
| Cat 2    |       0.0% |         0 |            234 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             81 | DERIVE          |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

