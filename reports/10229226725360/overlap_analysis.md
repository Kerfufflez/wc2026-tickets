## Category 1 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 28 groups, price range $46,000 – $2,527,700 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 45 Seats 10–11  avg $25,300/ea  total $50,600
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 29 groups, price range $34,500 – $514,303 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 309 Row 24 Seats 1–2  avg $18,975/ea  total $37,950
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 16 groups, price range $36,306 – $230,000 total
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
Cheapest New: Sec 302 Row 22 Seats 5–6  avg $15,812/ea  total $31,624

Pairs eligible for merge (NEW below G2 min $36,306): 6

## Category 4 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 7 groups, price range $27,588 – $63,284 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 331 Row 20 Seats 1–2  avg $17,250/ea  total $34,500
Cheapest New: Sec 331 Row 22 Seats 21–22  avg $33,350/ea  total $66,700

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             15 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             21 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             24 | DERIVE          |
| Cat 4    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **DERIVE**

