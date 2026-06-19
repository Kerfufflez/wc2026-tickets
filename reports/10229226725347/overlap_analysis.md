## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 112 groups, price range $5,276 – $39,100 total
G4 fetched: 78 groups → 234 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   228 |       97.4% | May exist in G2, not top-100   |
| NEW        |     6 |        2.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 123 Row 23 Seats 21–22  avg $3,220/ea  total $6,440
Cheapest New: Sec 149 Row 34 Seats 24–25  avg $34,477/ea  total $68,954

Pairs eligible for merge (NEW below G2 min $5,276): 0

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 155 groups, price range $4,025 – $43,470 total
G4 fetched: 80 groups → 240 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   240 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 333 Row 18 Seats 1–2  avg $2,064/ea  total $4,128
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 56 groups, price range $3,889 – $23,000 total
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
Date: June 19, 2026

G2 fetched: 4 groups, price range $5,750 – $44,850 total
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
| Cat 1    |       0.0% |         6 |            228 | DERIVE          |
| Cat 2    |       0.0% |         0 |            240 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             87 | DERIVE          |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

