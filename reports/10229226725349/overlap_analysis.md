## Category 1 — Pair Derivation Analysis
Date: July 6, 2026

G2 fetched: 48 groups, price range $2,760 – $20,930 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 120 Row 5 Seats 1–2  avg $1,438/ea  total $2,876
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 6, 2026

G2 fetched: 31 groups, price range $2,990 – $19,895 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |       75.0% | May exist in G2, not top-100   |
| NEW        |     6 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 416 Row 21 Seats 13–14  avg $1,898/ea  total $3,796
Cheapest New: Sec 438 Row 4 Seats 9–10  avg $17,250/ea  total $34,500

Pairs eligible for merge (NEW below G2 min $2,990): 0

## Category 3 — Pair Derivation Analysis
Date: July 6, 2026

G2 fetched: 6 groups, price range $2,990 – $4,600 total
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
Cheapest New: Sec 453 Row 19 Seats 1–2  avg $2,415/ea  total $4,830

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             36 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             18 | DERIVE          |
| Cat 3    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

