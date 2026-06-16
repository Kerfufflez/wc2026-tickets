## Category 1 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 47 groups, price range $3,680 – $13,800 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    57 |       95.0% | May exist in G2, not top-100   |
| NEW        |     3 |        5.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 201 Row 11 Seats 11–12  avg $2,707/ea  total $5,414
Cheapest New: Sec 146 Row 21 Seats 7–8  avg $9,200/ea  total $18,400

## Category 2 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 58 groups, price range $2,702 – $12,270 total
G4 fetched: 23 groups → 69 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    63 |       91.3% | May exist in G2, not top-100   |
| NEW        |     6 |        8.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 409 Row 20 Seats 17–18  avg $1,380/ea  total $2,760
Cheapest New: Sec 440 Row 13 Seats 6–7  avg $1,322/ea  total $2,644

Pairs eligible for merge (NEW below G2 min $2,702): 3

## Category 3 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 11 groups, price range $2,760 – $8,050 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 433 Row 21 Seats 7–8  avg $1,380/ea  total $2,760
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             57 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             63 | DERIVE          |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

