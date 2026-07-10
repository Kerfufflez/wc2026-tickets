## Category 1 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 42 groups, price range $28,405 – $211,600 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 146 Row 32 Seats 24–25  avg $16,848/ea  total $33,696
Cheapest New: Sec 148 Row 32 Seats 3–4  avg $212,750/ea  total $425,500

## Category 2 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 53 groups, price range $19,994 – $177,935 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 316 Row 12 Seats 7–8  avg $14,375/ea  total $28,750
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 44 groups, price range $18,400 – $1,393,800 total
G4 fetched: 17 groups → 51 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |       76.5% | May exist in G2, not top-100   |
| NEW        |    12 |       23.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 345 Row 23 Seats 25–26  avg $9,292/ea  total $18,584
Cheapest New: Sec 307 Row 16 Seats 1–2  avg $8,510/ea  total $17,020

Pairs eligible for merge (NEW below G2 min $18,400): 12

## Category 4 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 13 groups, price range $14,881 – $60,950 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 321 Row 23 Seats 9–10  avg $10,925/ea  total $21,850
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |              9 | SKIP            |
| Cat 2    |       0.0% |         0 |             12 | INVESTIGATE     |
| Cat 3    |       0.0% |        12 |             39 | DERIVE          |
| Cat 4    |       0.0% |         0 |             18 | INVESTIGATE     |

Overall recommendation: **DERIVE**

