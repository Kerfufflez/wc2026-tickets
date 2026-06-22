## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 214 groups, price range $8,214 – $115,000 total
G4 fetched: 73 groups → 219 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   219 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 124 Row 31 Seats 9–10  avg $4,379/ea  total $8,758
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 119 groups, price range $7,360 – $34,500 total
G4 fetched: 55 groups → 165 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   165 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 319 Row 5 Seats 17–18  avg $3,944/ea  total $7,888
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 87 groups, price range $6,498 – $46,000 total
G4 fetched: 32 groups → 96 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    90 |       93.8% | May exist in G2, not top-100   |
| NEW        |     6 |        6.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 408 Row 14 Seats 5–6  avg $3,450/ea  total $6,900
Cheapest New: Sec 418 Row 26 Seats 10–11  avg $3,048/ea  total $6,096

Pairs eligible for merge (NEW below G2 min $6,498): 6

## Category 4 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 3 groups, price range $8,476 – $11,500 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     3 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 401 Row 18 Seats 23–24  avg $11,500/ea  total $23,000

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            219 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            165 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             90 | DERIVE          |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

