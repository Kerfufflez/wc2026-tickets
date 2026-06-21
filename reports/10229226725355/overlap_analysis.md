## Category 1 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 141 groups, price range $7,666 – $1,150,000 total
G4 fetched: 85 groups → 255 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   255 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 135 Row 21 Seats 17–18  avg $4,140/ea  total $8,280
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 36 groups, price range $6,739 – $27,600 total
G4 fetched: 25 groups → 75 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    69 |       92.0% | May exist in G2, not top-100   |
| NEW        |     6 |        8.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 321 Row 24 Seats 4–5  avg $3,450/ea  total $6,900
Cheapest New: Sec 318 Row 25 Seats 13–14  avg $16,100/ea  total $32,200

Pairs eligible for merge (NEW below G2 min $6,739): 0

## Category 3 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 28 groups, price range $6,095 – $32,200 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 330 Row 30 Seats 15–16  avg $3,278/ea  total $6,556
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 21, 2026

G2 fetched: 4 groups, price range $6,774 – $11,958 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 356 Row 28 Seats 11–12  avg $5,232/ea  total $10,464
Cheapest New: Sec 328 Row 24 Seats 13–14  avg $17,250/ea  total $34,500

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            255 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             69 | DERIVE          |
| Cat 3    |       0.0% |         0 |             36 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              6 | SKIP            |

Overall recommendation: **DERIVE**

