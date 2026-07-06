## Category 1 — Pair Derivation Analysis
Date: July 6, 2026

G2 fetched: 139 groups, price range $3,680 – $34,500 total
G4 fetched: 39 groups → 117 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   117 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 203 Row 15 Seats 16–17  avg $2,064/ea  total $4,128
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 6, 2026

G2 fetched: 102 groups, price range $2,760 – $27,600 total
G4 fetched: 24 groups → 72 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    66 |       91.7% | May exist in G2, not top-100   |
| NEW        |     6 |        8.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 453 Row 4 Seats 3–4  avg $1,552/ea  total $3,104
Cheapest New: Sec 438 Row 4 Seats 9–10  avg $17,250/ea  total $34,500

Pairs eligible for merge (NEW below G2 min $2,760): 0

## Category 3 — Pair Derivation Analysis
Date: July 6, 2026

G2 fetched: 9 groups, price range $2,760 – $8,050 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 403 Row 22 Seats 17–18  avg $1,552/ea  total $3,104
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            117 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             66 | DERIVE          |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

