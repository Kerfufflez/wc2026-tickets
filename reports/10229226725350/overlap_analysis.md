## Category 1 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 68 groups, price range $6,281 – $26,795 total
G4 fetched: 28 groups → 84 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |       96.4% | May exist in G2, not top-100   |
| NEW        |     3 |        3.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 119 Row K Seats 1–2  avg $3,381/ea  total $6,762
Cheapest New: Sec 241 Row L Seats 5–6  avg $39,494/ea  total $78,988

## Category 2 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 53 groups, price range $5,278 – $29,543 total
G4 fetched: 34 groups → 102 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    96 |       94.1% | May exist in G2, not top-100   |
| NEW        |     6 |        5.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 311 Row LL Seats 9–10  avg $2,794/ea  total $5,588
Cheapest New: Sec 331 Row G Seats 1–2  avg $17,250/ea  total $34,500

Pairs eligible for merge (NEW below G2 min $5,278): 0

## Category 3 — Pair Derivation Analysis
Date: June 20, 2026

G2 fetched: 16 groups, price range $5,750 – $17,250 total
G4 fetched: 10 groups → 30 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    27 |       90.0% | May exist in G2, not top-100   |
| NEW        |     3 |       10.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 343 Row K Seats 3–4  avg $2,875/ea  total $5,750
Cheapest New: Sec 319 Row T Seats 10–11  avg $14,375/ea  total $28,750

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             81 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             96 | DERIVE          |
| Cat 3    |       0.0% |         3 |             27 | INVESTIGATE     |

Overall recommendation: **DERIVE**

