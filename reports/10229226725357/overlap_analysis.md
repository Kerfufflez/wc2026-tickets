## Category 1 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 104 groups, price range $10,005 – $230,000 total
G4 fetched: 32 groups → 96 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    93 |       96.9% | May exist in G2, not top-100   |
| NEW        |     3 |        3.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 244 Row 9 Seats 21–22  avg $5,290/ea  total $10,580
Cheapest New: Sec 125 Row 19 Seats 20–21  avg $460,000/ea  total $920,000

## Category 2 — Pair Derivation Analysis
Date: June 19, 2026

G2 fetched: 6 groups, price range $10,000 – $19,998 total
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
Cheapest New: Sec 343 Row 2 Seats 26–27  avg $11,270/ea  total $22,540

Pairs eligible for merge (NEW below G2 min $10,000): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             93 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |              0 | DERIVE          |

Overall recommendation: **DERIVE**

