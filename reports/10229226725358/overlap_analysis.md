## Category 1 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 116 groups, price range $9,591 – $89,916 total
G4 fetched: 27 groups → 81 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    75 |       92.6% | May exist in G2, not top-100   |
| NEW        |     6 |        7.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 33 Seats 17–18  avg $6,118/ea  total $12,236
Cheapest New: Sec 121 Row 12 Seats 6–7  avg $115,000/ea  total $230,000

Pairs eligible for merge (NEW below G2 min $9,591): 0

## Category 2 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 153 groups, price range $6,900 – $115,000 total
G4 fetched: 45 groups → 135 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   135 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 315 Row 26 Seats 13–14  avg $3,565/ea  total $7,130
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 185 groups, price range $5,290 – $57,500 total
G4 fetched: 52 groups → 156 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   156 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 333 Row 23 Seats 5–6  avg $3,094/ea  total $6,188
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 10, 2026

G2 fetched: 13 groups, price range $7,537 – $80,500 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 310 Row 31 Seats 22–23  avg $7,128/ea  total $14,256
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |             75 | DERIVE          |
| Cat 2    |       0.0% |         0 |            135 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |            156 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

