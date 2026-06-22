## Category 1 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 239 groups, price range $8,214 – $115,000 total
G4 fetched: 85 groups → 255 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   246 |       96.5% | May exist in G2, not top-100   |
| NEW        |     9 |        3.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 107 Row 23 Seats 13–14  avg $4,485/ea  total $8,970
Cheapest New: Sec 145 Row 30 Seats 16–17  avg $4,025/ea  total $8,050

Pairs eligible for merge (NEW below G2 min $8,214): 9

## Category 2 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 130 groups, price range $6,785 – $34,500 total
G4 fetched: 67 groups → 201 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   198 |       98.5% | May exist in G2, not top-100   |
| NEW        |     3 |        1.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 208 Row 9 Seats 11–12  avg $3,450/ea  total $6,900
Cheapest New: Sec 318 Row 1 Seats 26–27  avg $25,300/ea  total $50,600

## Category 3 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 99 groups, price range $6,440 – $34,500 total
G4 fetched: 30 groups → 90 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    87 |       96.7% | May exist in G2, not top-100   |
| NEW        |     3 |        3.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 405 Row 26 Seats 17–18  avg $3,335/ea  total $6,670
Cheapest New: Sec 418 Row 26 Seats 10–11  avg $3,048/ea  total $6,096

## Category 4 — Pair Derivation Analysis
Date: June 22, 2026

G2 fetched: 5 groups, price range $6,900 – $11,500 total
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
Cheapest New: Sec 401 Row 18 Seats 23–24  avg $11,500/ea  total $23,000

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            246 | DERIVE          |
| Cat 2    |       0.0% |         3 |            198 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             87 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

