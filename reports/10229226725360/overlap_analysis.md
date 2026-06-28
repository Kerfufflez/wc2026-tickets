## Category 1 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 31 groups, price range $51,980 – $2,527,700 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |       85.7% | May exist in G2, not top-100   |
| NEW        |     3 |       14.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 121 Row 15 Seats 9–10  avg $27,140/ea  total $54,280
Cheapest New: Sec 103 Row 45 Seats 10–11  avg $25,300/ea  total $50,600

## Category 2 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 31 groups, price range $29,629 – $510,784 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 319 Row 18 Seats 13–14  avg $15,984/ea  total $31,968
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 17 groups, price range $36,306 – $356,500 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |       80.0% | May exist in G2, not top-100   |
| NEW        |     6 |       20.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 302 Row 26 Seats 17–18  avg $22,219/ea  total $44,438
Cheapest New: Sec 323 Row 22 Seats 18–19  avg $16,330/ea  total $32,660

Pairs eligible for merge (NEW below G2 min $36,306): 6

## Category 4 — Pair Derivation Analysis
Date: June 28, 2026

G2 fetched: 7 groups, price range $25,300 – $63,284 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 331 Row 19 Seats 17–18  avg $14,375/ea  total $28,750
Cheapest New: Sec 331 Row 22 Seats 21–22  avg $33,350/ea  total $66,700

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             18 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             24 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             24 | DERIVE          |
| Cat 4    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **DERIVE**

