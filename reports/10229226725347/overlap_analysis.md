## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 110 groups, price range $6,440 – $57,500 total
G4 fetched: 79 groups → 237 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   234 |       98.7% | May exist in G2, not top-100   |
| NEW        |     3 |        1.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 123 Row 32 Seats 1–2  avg $3,286/ea  total $6,572
Cheapest New: Sec 104 Row 43 Seats 17–18  avg $401,350/ea  total $802,700

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 148 groups, price range $5,060 – $43,470 total
G4 fetched: 69 groups → 207 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   204 |       98.6% | May exist in G2, not top-100   |
| NEW        |     3 |        1.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 334 Row 8 Seats 9–10  avg $2,530/ea  total $5,060
Cheapest New: Sec 310 Row 26 Seats 6–7  avg $2,505/ea  total $5,010

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 47 groups, price range $4,847 – $23,000 total
G4 fetched: 26 groups → 78 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    69 |       88.5% | May exist in G2, not top-100   |
| NEW        |     9 |       11.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 305 Row 22 Seats 1–2  avg $2,464/ea  total $4,928
Cheapest New: Sec 301 Row 9 Seats 5–6  avg $2,415/ea  total $4,830

Pairs eligible for merge (NEW below G2 min $4,847): 3

## Category 4 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 2 groups, price range $11,500 – $44,850 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     6 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 346 Row 26 Seats 8–9  avg $2,961/ea  total $5,922

Pairs eligible for merge (NEW below G2 min $11,500): 6

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            234 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |            204 | INVESTIGATE     |
| Cat 3    |       0.0% |         9 |             69 | DERIVE          |
| Cat 4    |       0.0% |         6 |              0 | DERIVE          |

Overall recommendation: **DERIVE**

