## Category 1 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 140 groups, price range $3,450 – $16,100 total
G4 fetched: 72 groups → 216 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   207 |       95.8% | May exist in G2, not top-100   |
| NEW        |     9 |        4.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 115 Row 30 Seats 13–14  avg $1,840/ea  total $3,680
Cheapest New: Sec 124 Row 26 Seats 13–14  avg $9,200/ea  total $18,400

Pairs eligible for merge (NEW below G2 min $3,450): 0

## Category 2 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 117 groups, price range $2,782 – $23,000 total
G4 fetched: 75 groups → 225 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   225 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 307 Row 14 Seats 7–8  avg $1,610/ea  total $3,220
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 11 groups, price range $3,680 – $8,050 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 317 Row 13 Seats 5–6  avg $2,030/ea  total $4,060
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            207 | DERIVE          |
| Cat 2    |       0.0% |         0 |            225 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

