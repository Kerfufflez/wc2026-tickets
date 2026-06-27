## Category 1 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 288 groups, price range $1,380 – $23,932 total
G4 fetched: 128 groups → 384 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   381 |       99.2% | May exist in G2, not top-100   |
| NEW        |     3 |        0.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 229 Row 30 Seats 9–10  avg $791/ea  total $1,582
Cheapest New: Sec 225 Row 14 Seats 16–17  avg $22,425/ea  total $44,850

## Category 2 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 323 groups, price range $932 – $8,740 total
G4 fetched: 151 groups → 453 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   444 |       98.0% | May exist in G2, not top-100   |
| NEW        |     9 |        2.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 542 Row 15 Seats 6–7  avg $499/ea  total $998
Cheapest New: Sec 536 Row 11 Seats 13–14  avg $4,600/ea  total $9,200

Pairs eligible for merge (NEW below G2 min $932): 0

## Category 3 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 93 groups, price range $954 – $12,167 total
G4 fetched: 33 groups → 99 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    99 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 549 Row 22 Seats 10–11  avg $545/ea  total $1,090
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |            381 | INVESTIGATE     |
| Cat 2    |       0.0% |         9 |            444 | DERIVE          |
| Cat 3    |       0.0% |         0 |             99 | INVESTIGATE     |

Overall recommendation: **DERIVE**

