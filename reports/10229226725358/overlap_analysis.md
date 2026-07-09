## Category 1 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 114 groups, price range $11,040 – $90,223 total
G4 fetched: 28 groups → 84 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    75 |       89.3% | May exist in G2, not top-100   |
| NEW        |     9 |       10.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 134 Row 22 Seats 1–2  avg $6,090/ea  total $12,180
Cheapest New: Sec 117 Row 29 Seats 15–16  avg $71,875/ea  total $143,750

Pairs eligible for merge (NEW below G2 min $11,040): 0

## Category 2 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 158 groups, price range $6,670 – $115,000 total
G4 fetched: 48 groups → 144 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   144 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 315 Row 26 Seats 13–14  avg $3,450/ea  total $6,900
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 185 groups, price range $5,290 – $57,500 total
G4 fetched: 48 groups → 144 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   144 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 349 Row 23 Seats 1–2  avg $2,875/ea  total $5,750
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 9, 2026

G2 fetched: 16 groups, price range $6,210 – $80,500 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 313 Row 27 Seats 7–8  avg $6,601/ea  total $13,202
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |             75 | DERIVE          |
| Cat 2    |       0.0% |         0 |            144 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |            144 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

