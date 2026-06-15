## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 229 groups, price range $2,714 – $27,600 total
G4 fetched: 163 groups → 489 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   483 |       98.8% | May exist in G2, not top-100   |
| NEW        |     6 |        1.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 348 Row G Seats 5–6  avg $1,357/ea  total $2,714
Cheapest New: Sec 121 Row EE Seats 19–20  avg $21,321/ea  total $42,642

Pairs eligible for merge (NEW below G2 min $2,714): 0

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 62 groups, price range $2,300 – $17,250 total
G4 fetched: 29 groups → 87 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    87 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 604 Row F Seats 5–6  avg $1,367/ea  total $2,734
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 24 groups, price range $2,307 – $23,000 total
G4 fetched: 9 groups → 27 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |       77.8% | May exist in G2, not top-100   |
| NEW        |     6 |       22.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 629 Row B Seats 10–11  avg $1,260/ea  total $2,520
Cheapest New: Sec 628 Row L Seats 10–11  avg $1,150/ea  total $2,300

Pairs eligible for merge (NEW below G2 min $2,307): 3

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 4 groups, price range $2,760 – $28,750 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 643 Row F Seats 3–4  avg $1,538/ea  total $3,076
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            483 | DERIVE          |
| Cat 2    |       0.0% |         0 |             87 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             21 | DERIVE          |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

