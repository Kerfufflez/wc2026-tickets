## Category 1 — Pair Derivation Analysis
Date: July 13, 2026

G2 fetched: 49 groups, price range $29,596 – $200,000 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |       83.3% | May exist in G2, not top-100   |
| NEW        |     3 |       16.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 103 Row 7 Seats 5–6  avg $16,088/ea  total $32,176
Cheapest New: Sec 148 Row 32 Seats 3–4  avg $212,750/ea  total $425,500

## Category 2 — Pair Derivation Analysis
Date: July 13, 2026

G2 fetched: 72 groups, price range $18,262 – $178,314 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 334 Row 4 Seats 13–14  avg $11,690/ea  total $23,380
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 13, 2026

G2 fetched: 43 groups, price range $18,170 – $1,357,000 total
G4 fetched: 17 groups → 51 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    33 |       64.7% | May exist in G2, not top-100   |
| NEW        |    18 |       35.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 345 Row 23 Seats 25–26  avg $9,292/ea  total $18,584
Cheapest New: Sec 304 Row 23 Seats 14–15  avg $8,280/ea  total $16,560

Pairs eligible for merge (NEW below G2 min $18,170): 18

## Category 4 — Pair Derivation Analysis
Date: July 13, 2026

G2 fetched: 15 groups, price range $17,248 – $54,050 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 321 Row 23 Seats 9–10  avg $10,925/ea  total $21,850
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             15 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |             24 | INVESTIGATE     |
| Cat 3    |       0.0% |        18 |             33 | DERIVE          |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

