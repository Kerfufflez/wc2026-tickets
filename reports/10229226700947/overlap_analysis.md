## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 64 groups, price range $3,887 – $2,300,000 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    78 |       96.3% | May exist in G2, not top-100   |
| NEW        |     3 |        3.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 231 Row 10 Seats 1–2  avg $2,058/ea  total $4,116
Cheapest New: Sec 210 Row 4 Seats 1–2  avg $1,898/ea  total $3,796

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 60 groups, price range $2,990 – $23,000 total
G4 fetched: 26 groups → 78 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    78 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 452 Row 7 Seats 15–16  avg $1,500/ea  total $3,000
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 29 groups, price range $3,162 – $8,050 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |       72.7% | May exist in G2, not top-100   |
| NEW        |     9 |       27.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 533 Row 13 Seats 1–2  avg $1,668/ea  total $3,336
Cheapest New: Sec 530 Row 17 Seats 13–14  avg $1,374/ea  total $2,748

Pairs eligible for merge (NEW below G2 min $3,162): 9

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             78 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             78 | INVESTIGATE     |
| Cat 3    |       0.0% |         9 |             24 | DERIVE          |

Overall recommendation: **DERIVE**

