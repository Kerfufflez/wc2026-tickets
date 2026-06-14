## Category 1 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 41 groups, price range $1,081 – $5,750 total
G4 fetched: 41 groups → 123 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   120 |       97.6% | May exist in G2, not top-100   |
| NEW        |     3 |        2.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 116 Row 26 Seats 1–2  avg $551/ea  total $1,102
Cheapest New: Sec 103 Row 29 Seats 5–6  avg $518/ea  total $1,036

## Category 2 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 95 groups, price range $840 – $3,450 total
G4 fetched: 74 groups → 222 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   213 |       95.9% | May exist in G2, not top-100   |
| NEW        |     9 |        4.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 122 Row 34 Seats 12–13  avg $430/ea  total $860
Cheapest New: Sec 122 Row 36 Seats 31–32  avg $1,854/ea  total $3,708

Pairs eligible for merge (NEW below G2 min $840): 0

## Category 3 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 104 groups, price range $775 – $9,200 total
G4 fetched: 40 groups → 120 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   120 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 329 Row 14 Seats 13–14  avg $402/ea  total $804
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 14, 2026

G2 fetched: 6 groups, price range $888 – $2,300 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       50.0% | May exist in G2, not top-100   |
| NEW        |     6 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 311 Row 30 Seats 9–10  avg $690/ea  total $1,380
Cheapest New: Sec 313 Row 31 Seats 21–22  avg $402/ea  total $804

Pairs eligible for merge (NEW below G2 min $888): 6

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            120 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |            213 | DERIVE          |
| Cat 3    |       0.0% |         0 |            120 | INVESTIGATE     |
| Cat 4    |       0.0% |         6 |              6 | DERIVE          |

Overall recommendation: **DERIVE**

