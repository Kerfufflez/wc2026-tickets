## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 132 groups, price range $8,050 – $1,150,000 total
G4 fetched: 86 groups → 258 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   258 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 107 Row 13 Seats 15–16  avg $4,140/ea  total $8,280
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 36 groups, price range $7,636 – $46,000 total
G4 fetched: 23 groups → 69 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    60 |       87.0% | May exist in G2, not top-100   |
| NEW        |     9 |       13.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 343 Row 30 Seats 10–11  avg $4,016/ea  total $8,032
Cheapest New: Sec 323 Row 21 Seats 1–2  avg $3,565/ea  total $7,130

Pairs eligible for merge (NEW below G2 min $7,636): 6

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 26 groups, price range $6,900 – $32,200 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 303 Row 20 Seats 8–9  avg $3,450/ea  total $6,900
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 3 groups, price range $6,774 – $11,958 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 356 Row 28 Seats 11–12  avg $5,232/ea  total $10,464
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            258 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |             60 | DERIVE          |
| Cat 3    |       0.0% |         0 |             33 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

