## Category 1 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 39 groups, price range $5,060 – $15,587 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |       86.7% | May exist in G2, not top-100   |
| NEW        |     6 |       13.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 228 Row 6 Seats 21–22  avg $3,162/ea  total $6,324
Cheapest New: Sec C310 Row 6 Seats 13–14  avg $2,328/ea  total $4,656

Pairs eligible for merge (NEW below G2 min $5,060): 3

## Category 2 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 43 groups, price range $3,643 – $41,400 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 415 Row 30 Seats 5–6  avg $1,854/ea  total $3,708
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 10 groups, price range $4,255 – $11,500 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 423 Row 16 Seats 13–14  avg $2,645/ea  total $5,290
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |             39 | DERIVE          |
| Cat 2    |       0.0% |         0 |             24 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

