## Category 1 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 40 groups, price range $4,285 – $27,600 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    30 |       90.9% | May exist in G2, not top-100   |
| NEW        |     3 |        9.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 464 Row 6 Seats 6–7  avg $2,644/ea  total $5,288
Cheapest New: Sec 116 Row 22 Seats 7–8  avg $17,250/ea  total $34,500

## Category 2 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 16 groups, price range $5,035 – $16,330 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    12 |       66.7% | May exist in G2, not top-100   |
| NEW        |     6 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 565 Row 7 Seats 13–14  avg $2,875/ea  total $5,750
Cheapest New: Sec 567 Row 11 Seats 12–13  avg $2,248/ea  total $4,496

Pairs eligible for merge (NEW below G2 min $5,035): 6

## Category 3 — Pair Derivation Analysis
Date: June 16, 2026

G2 fetched: 14 groups, price range $4,301 – $13,225 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |       75.0% | May exist in G2, not top-100   |
| NEW        |     6 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 644 Row 6 Seats 9–10  avg $2,415/ea  total $4,830
Cheapest New: Sec 665 Row 9 Seats 17–18  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $4,301): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             30 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             12 | DERIVE          |
| Cat 3    |       0.0% |         6 |             18 | DERIVE          |

Overall recommendation: **DERIVE**

