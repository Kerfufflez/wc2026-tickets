## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 22 groups, price range $9,200 – $27,600 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       66.7% | May exist in G2, not top-100   |
| NEW        |     6 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 454 Row 3 Seats 5–6  avg $4,600/ea  total $9,200
Cheapest New: Sec 116 Row 22 Seats 7–8  avg $17,250/ea  total $34,500

Pairs eligible for merge (NEW below G2 min $9,200): 0

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 10 groups, price range $8,214 – $19,550 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 536 Row 3 Seats 1–2  avg $8,117/ea  total $16,234
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 8 groups, price range $8,048 – $34,500 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       80.0% | May exist in G2, not top-100   |
| NEW        |     3 |       20.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 648 Row 4 Seats 10–11  avg $4,025/ea  total $8,050
Cheapest New: Sec 620 Row 9 Seats 14–15  avg $29,003/ea  total $58,006

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |             12 | DERIVE          |
| Cat 2    |       0.0% |         0 |              3 | SKIP            |
| Cat 3    |       0.0% |         3 |             12 | INVESTIGATE     |

Overall recommendation: **DERIVE**

