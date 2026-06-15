## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 142 groups, price range $3,450 – $69,000 total
G4 fetched: 87 groups → 261 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   261 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 109 Row 22 Seats 1–2  avg $1,840/ea  total $3,680
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 120 groups, price range $3,218 – $22,540 total
G4 fetched: 56 groups → 168 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   162 |       96.4% | May exist in G2, not top-100   |
| NEW        |     6 |        3.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 224 Row 30 Seats 17–18  avg $1,609/ea  total $3,218
Cheapest New: Sec 242 Row 29 Seats 31–32  avg $1,552/ea  total $3,104

Pairs eligible for merge (NEW below G2 min $3,218): 3

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 37 groups, price range $2,760 – $23,000 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 234 Row 26 Seats 1–2  avg $1,570/ea  total $3,140
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 4 groups, price range $3,105 – $6,898 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 219 Row 27 Seats 13–14  avg $2,524/ea  total $5,048
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            261 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |            162 | DERIVE          |
| Cat 3    |       0.0% |         0 |             45 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

