## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 77 groups, price range $10,890 – $822,710 total
G4 fetched: 31 groups → 93 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    90 |       96.8% | May exist in G2, not top-100   |
| NEW        |     3 |        3.2% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 34 Seats 11–12  avg $5,683/ea  total $11,366
Cheapest New: Sec 103 Row 39 Seats 11–12  avg $5,034/ea  total $10,068

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 130 groups, price range $7,130 – $1,328,250 total
G4 fetched: 48 groups → 144 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   144 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 309 Row 14 Seats 17–18  avg $3,910/ea  total $7,820
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 119 groups, price range $6,582 – $115,000 total
G4 fetched: 47 groups → 141 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   135 |       95.7% | May exist in G2, not top-100   |
| NEW        |     6 |        4.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 322 Row 21 Seats 17–18  avg $3,335/ea  total $6,670
Cheapest New: Sec 328 Row 6 Seats 1–2  avg $3,220/ea  total $6,440

Pairs eligible for merge (NEW below G2 min $6,582): 6

## Category 4 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 8 groups, price range $6,900 – $80,500 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 309 Row 27 Seats 1–2  avg $20,125/ea  total $40,250
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             90 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |            144 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |            135 | DERIVE          |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

