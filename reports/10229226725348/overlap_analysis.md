## Category 1 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 42 groups, price range $8,402 – $44,850 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |       87.5% | May exist in G2, not top-100   |
| NEW        |     3 |       12.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 314 Row 9 Seats 1–2  avg $4,600/ea  total $9,200
Cheapest New: Sec 467 Row 1 Seats 1–2  avg $35,649/ea  total $71,298

## Category 2 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 16 groups, price range $9,770 – $23,000 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 504 Row 9 Seats 10–11  avg $5,520/ea  total $11,040
Cheapest New: Sec 549 Row 4 Seats 11–12  avg $3,985/ea  total $7,970

## Category 3 — Pair Derivation Analysis
Date: July 1, 2026

G2 fetched: 10 groups, price range $7,360 – $13,800 total
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
Cheapest New: Sec 620 Row 9 Seats 14–15  avg $8,303/ea  total $16,606

Pairs eligible for merge (NEW below G2 min $7,360): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             21 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |              3 | SKIP            |
| Cat 3    |       0.0% |         6 |              0 | DERIVE          |

Overall recommendation: **DERIVE**

