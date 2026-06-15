## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 121 groups, price range $2,990 – $230,000 total
G4 fetched: 80 groups → 240 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   240 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 238 Row 2 Seats 5–6  avg $1,719/ea  total $3,438
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 145 groups, price range $1,996 – $18,998 total
G4 fetched: 121 groups → 363 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   354 |       97.5% | May exist in G2, not top-100   |
| NEW        |     9 |        2.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 544 Row 4 Seats 8–9  avg $1,149/ea  total $2,298
Cheapest New: Sec 511 Row 7 Seats 11–12  avg $11,500/ea  total $23,000

Pairs eligible for merge (NEW below G2 min $1,996): 0

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 24 groups, price range $2,070 – $11,500 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 548 Row 20 Seats 1–2  avg $1,149/ea  total $2,298
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |            240 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |            354 | DERIVE          |
| Cat 3    |       0.0% |         0 |             36 | INVESTIGATE     |

Overall recommendation: **DERIVE**

