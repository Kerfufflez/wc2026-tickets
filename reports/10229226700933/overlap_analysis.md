## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 9 groups, price range $2,748 – $6,325 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       33.3% | May exist in G2, not top-100   |
| NEW        |     6 |       66.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 104 Row 24 Seats 1–2  avg $1,840/ea  total $3,680
Cheapest New: Sec 115 Row 19 Seats 5–6  avg $3,968/ea  total $7,936

Pairs eligible for merge (NEW below G2 min $2,748): 0

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 37 groups, price range $2,185 – $11,500 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |       91.7% | May exist in G2, not top-100   |
| NEW        |     3 |        8.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 328 Row 25 Seats 1–2  avg $1,150/ea  total $2,300
Cheapest New: Sec 239 Row 22 Seats 1–2  avg $1,069/ea  total $2,138

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 6 groups, price range $2,760 – $10,350 total
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
Cheapest New: Sec 317 Row 9 Seats 4–5  avg $1,254/ea  total $2,508

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |              3 | DERIVE          |
| Cat 2    |       0.0% |         3 |             33 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

