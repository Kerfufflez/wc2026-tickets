## Category 1 — Pair Derivation Analysis
Date: July 11, 2026

G2 fetched: 41 groups, price range $27,600 – $200,000 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |       50.0% | May exist in G2, not top-100   |
| NEW        |     3 |       50.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 124 Row 44 Seats 10–11  avg $32,775/ea  total $65,550
Cheapest New: Sec 148 Row 32 Seats 3–4  avg $212,750/ea  total $425,500

## Category 2 — Pair Derivation Analysis
Date: July 11, 2026

G2 fetched: 58 groups, price range $15,778 – $177,935 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 335 Row 22 Seats 1–2  avg $10,925/ea  total $21,850
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 11, 2026

G2 fetched: 41 groups, price range $18,745 – $1,393,800 total
G4 fetched: 13 groups → 39 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |       84.6% | May exist in G2, not top-100   |
| NEW        |     6 |       15.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 302 Row 22 Seats 21–22  avg $10,178/ea  total $20,356
Cheapest New: Sec 307 Row 16 Seats 1–2  avg $7,820/ea  total $15,640

Pairs eligible for merge (NEW below G2 min $18,745): 6

## Category 4 — Pair Derivation Analysis
Date: July 11, 2026

G2 fetched: 13 groups, price range $14,490 – $54,050 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    18 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 331 Row 22 Seats 21–22  avg $10,061/ea  total $20,122
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |              3 | SKIP            |
| Cat 2    |       0.0% |         0 |             15 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             33 | DERIVE          |
| Cat 4    |       0.0% |         0 |             18 | INVESTIGATE     |

Overall recommendation: **DERIVE**

