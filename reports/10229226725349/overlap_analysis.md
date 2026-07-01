## Category 1 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 199 groups, price range $5,060 – $34,500 total
G4 fetched: 100 groups → 300 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   294 |       98.0% | May exist in G2, not top-100   |
| NEW        |     6 |        2.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 227 Row 13 Seats 19–20  avg $2,530/ea  total $5,060
Cheapest New: Sec 220 Row 8 Seats 10–11  avg $22,999/ea  total $45,998

Pairs eligible for merge (NEW below G2 min $5,060): 0

## Category 2 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 179 groups, price range $3,680 – $57,498 total
G4 fetched: 77 groups → 231 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   231 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 415 Row 30 Seats 17–18  avg $2,070/ea  total $4,140
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 22 groups, price range $4,059 – $11,038 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 433 Row 22 Seats 1–2  avg $2,990/ea  total $5,980
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            294 | DERIVE          |
| Cat 2    |       0.0% |         0 |            231 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

