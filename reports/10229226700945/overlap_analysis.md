## Category 1 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 32 groups, price range $2,530 – $9,200 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec C310 Row 9 Seats 7–8  avg $2,053/ea  total $4,106
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 22 groups, price range $2,070 – $5,750 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       50.0% | May exist in G2, not top-100   |
| NEW        |     6 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 412 Row 28 Seats 1–2  avg $1,150/ea  total $2,300
Cheapest New: Sec 411 Row 30 Seats 2–3  avg $978/ea  total $1,956

Pairs eligible for merge (NEW below G2 min $2,070): 3

## Category 3 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 8 groups, price range $2,288 – $3,450 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 421 Row 12 Seats 13–14  avg $1,259/ea  total $2,518
Cheapest New: Sec 433 Row 20 Seats 9–10  avg $920/ea  total $1,840

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             36 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |              6 | DERIVE          |
| Cat 3    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

