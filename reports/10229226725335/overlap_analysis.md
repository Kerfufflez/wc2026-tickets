## Category 1 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 123 groups, price range $3,528 – $23,000 total
G4 fetched: 53 groups → 159 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   153 |       96.2% | May exist in G2, not top-100   |
| NEW        |     6 |        3.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 117 Row 39 Seats 5–6  avg $1,955/ea  total $3,910
Cheapest New: Sec 104 Row 23 Seats 12–13  avg $12,075/ea  total $24,150

Pairs eligible for merge (NEW below G2 min $3,528): 0

## Category 2 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 86 groups, price range $2,758 – $23,000 total
G4 fetched: 60 groups → 180 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   177 |       98.3% | May exist in G2, not top-100   |
| NEW        |     3 |        1.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 314 Row 8 Seats 15–16  avg $1,725/ea  total $3,450
Cheapest New: Sec 309 Row 20 Seats 17–18  avg $1,294/ea  total $2,588

## Category 3 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 60 groups, price range $2,530 – $57,500 total
G4 fetched: 51 groups → 153 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   153 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 303 Row 14 Seats 9–10  avg $1,265/ea  total $2,530
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 3 groups, price range $3,910 – $5,750 total
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
Cheapest New: Sec 311 Row 34 Seats 22–23  avg $4,025/ea  total $8,050

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            153 | DERIVE          |
| Cat 2    |       0.0% |         3 |            177 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |            153 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

