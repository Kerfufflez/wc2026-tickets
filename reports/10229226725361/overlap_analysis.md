## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 399 groups, price range $4,140 – $403,650 total
G4 fetched: 264 groups → 792 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   786 |       99.2% | May exist in G2, not top-100   |
| NEW        |     6 |        0.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 130 Row 19 Seats 21–22  avg $2,277/ea  total $4,554
Cheapest New: Sec 130 Row 20 Seats 21–22  avg $1,000,500/ea  total $2,001,000

Pairs eligible for merge (NEW below G2 min $4,140): 0

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 142 groups, price range $3,887 – $46,000 total
G4 fetched: 49 groups → 147 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   144 |       98.0% | May exist in G2, not top-100   |
| NEW        |     3 |        2.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 313 Row 21 Seats 19–20  avg $2,299/ea  total $4,598
Cheapest New: Sec 320 Row 20 Seats 17–18  avg $25,300/ea  total $50,600

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 49 groups, price range $4,073 – $271,400 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    57 |       95.0% | May exist in G2, not top-100   |
| NEW        |     3 |        5.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 330 Row 18 Seats 5–6  avg $2,038/ea  total $4,076
Cheapest New: Sec 330 Row 30 Seats 17–18  avg $2,012/ea  total $4,024

## Category 4 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 4 groups, price range $3,910 – $16,100 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 328 Row 28 Seats 3–4  avg $2,853/ea  total $5,706
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            786 | DERIVE          |
| Cat 2    |       0.0% |         3 |            144 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             57 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

