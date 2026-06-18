## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 113 groups, price range $5,405 – $39,100 total
G4 fetched: 88 groups → 264 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   258 |       97.7% | May exist in G2, not top-100   |
| NEW        |     6 |        2.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 104 Row 27 Seats 7–8  avg $2,818/ea  total $5,636
Cheapest New: Sec 149 Row 34 Seats 24–25  avg $34,477/ea  total $68,954

Pairs eligible for merge (NEW below G2 min $5,405): 0

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 165 groups, price range $3,864 – $43,700 total
G4 fetched: 86 groups → 258 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   258 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 310 Row 26 Seats 23–24  avg $1,937/ea  total $3,874
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 54 groups, price range $3,889 – $23,000 total
G4 fetched: 31 groups → 93 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    87 |       93.5% | May exist in G2, not top-100   |
| NEW        |     6 |        6.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 323 Row 15 Seats 5–6  avg $2,012/ea  total $4,024
Cheapest New: Sec 350 Row 14 Seats 4–5  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $3,889): 0

## Category 4 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 4 groups, price range $5,750 – $44,850 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 321 Row 20 Seats 23–24  avg $3,220/ea  total $6,440
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            258 | DERIVE          |
| Cat 2    |       0.0% |         0 |            258 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             87 | DERIVE          |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

