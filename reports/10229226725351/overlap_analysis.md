## Category 1 — Pair Derivation Analysis
Date: July 7, 2026

G2 fetched: 40 groups, price range $1,840 – $13,766 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 134 Row 28 Seats 22–23  avg $1,092/ea  total $2,184
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: July 7, 2026

G2 fetched: 31 groups, price range $1,618 – $5,520 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |       75.0% | May exist in G2, not top-100   |
| NEW        |     6 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 342 Row 8 Seats 3–4  avg $1,024/ea  total $2,048
Cheapest New: Sec 103 Row 55 Seats 1–2  avg $2,875/ea  total $5,750

Pairs eligible for merge (NEW below G2 min $1,618): 0

## Category 3 — Pair Derivation Analysis
Date: July 7, 2026

G2 fetched: 16 groups, price range $2,298 – $10,350 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 345 Row 26 Seats 17–18  avg $1,898/ea  total $3,796
Cheapest New: Sec 328 Row 12 Seats 17–18  avg $759/ea  total $1,518

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             36 | INVESTIGATE     |
| Cat 2    |       0.0% |         6 |             18 | DERIVE          |
| Cat 3    |       0.0% |         3 |              3 | SKIP            |

Overall recommendation: **DERIVE**

