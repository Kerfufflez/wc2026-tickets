## Category 1 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 36 groups, price range $9,200 – $69,000 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |       87.5% | May exist in G2, not top-100   |
| NEW        |     3 |       12.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 422 Row 8 Seats 15–16  avg $5,002/ea  total $10,004
Cheapest New: Sec 467 Row 1 Seats 1–2  avg $35,649/ea  total $71,298

## Category 2 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 12 groups, price range $8,740 – $22,770 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 566 Row 7 Seats 13–14  avg $4,658/ea  total $9,316
Cheapest New: Sec PC04 Row 2 Seats 5–6  avg $11,500/ea  total $23,000

## Category 3 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 9 groups, price range $6,900 – $18,400 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     6 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 665 Row 9 Seats 17–18  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $6,900): 0

## Category 4 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 1 groups, price range $10,350 – $10,350 total
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
Cheapest New: Sec 619 Row 7 Seats 5–6  avg $4,670/ea  total $9,340

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             21 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |              6 | SKIP            |
| Cat 3    |       0.0% |         6 |              0 | DERIVE          |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

