## Category 1 — Pair Derivation Analysis
Date: July 13, 2026

G2 fetched: 111 groups, price range $8,970 – $50,600 total
G4 fetched: 35 groups → 105 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    99 |       94.3% | May exist in G2, not top-100   |
| NEW        |     6 |        5.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 120 Row 39 Seats 8–9  avg $4,715/ea  total $9,430
Cheapest New: Sec 117 Row 16 Seats 11–12  avg $34,500/ea  total $69,000

Pairs eligible for merge (NEW below G2 min $8,970): 0

## Category 2 — Pair Derivation Analysis
Date: July 13, 2026

G2 fetched: 169 groups, price range $5,980 – $69,000 total
G4 fetched: 29 groups → 87 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    87 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 343 Row 14 Seats 12–13  avg $3,180/ea  total $6,360
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 13, 2026

G2 fetched: 155 groups, price range $5,750 – $115,000 total
G4 fetched: 52 groups → 156 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   153 |       98.1% | May exist in G2, not top-100   |
| NEW        |     3 |        1.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 319 Row 18 Seats 17–18  avg $3,036/ea  total $6,072
Cheapest New: Sec 330 Row 4 Seats 3–4  avg $2,760/ea  total $5,520

## Category 4 — Pair Derivation Analysis
Date: July 13, 2026

G2 fetched: 18 groups, price range $6,394 – $80,500 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 310 Row 31 Seats 22–23  avg $4,025/ea  total $8,050
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |             99 | DERIVE          |
| Cat 2    |       0.0% |         0 |             87 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |            153 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

