## Category 1 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 34 groups, price range $4,370 – $27,600 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 430 Row 6 Seats 14–15  avg $2,358/ea  total $4,716
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 7 groups, price range $4,025 – $10,281 total
G4 fetched: 7 groups → 21 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |       71.4% | May exist in G2, not top-100   |
| NEW        |     6 |       28.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 535 Row 8 Seats 18–19  avg $2,300/ea  total $4,600
Cheapest New: Sec PC10 Row 1 Seats 6–7  avg $5,750/ea  total $11,500

Pairs eligible for merge (NEW below G2 min $4,025): 0

## Category 3 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 11 groups, price range $3,306 – $6,440 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       33.3% | May exist in G2, not top-100   |
| NEW        |     6 |       66.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 644 Row 3 Seats 1–2  avg $2,530/ea  total $5,060
Cheapest New: Sec 639 Row 7 Seats 5–6  avg $4,025/ea  total $8,050

Pairs eligible for merge (NEW below G2 min $3,306): 0

## Category 4 — Pair Derivation Analysis
Date: June 15, 2026

G2 fetched: 1 groups, price range $3,680 – $3,680 total
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
Cheapest New: Sec 618 Row 5 Seats 13–14  avg $2,300/ea  total $4,600

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             45 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             15 | DERIVE          |
| Cat 3    |       0.0% |         6 |              3 | DERIVE          |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

