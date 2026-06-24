## Category 1 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 387 groups, price range $4,483 – $403,650 total
G4 fetched: 257 groups → 771 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   765 |       99.2% | May exist in G2, not top-100   |
| NEW        |     6 |        0.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 110 Row 21 Seats 8–9  avg $2,300/ea  total $4,600
Cheapest New: Sec 130 Row 20 Seats 21–22  avg $1,000,500/ea  total $2,001,000

Pairs eligible for merge (NEW below G2 min $4,483): 0

## Category 2 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 141 groups, price range $3,887 – $46,000 total
G4 fetched: 50 groups → 150 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   147 |       98.0% | May exist in G2, not top-100   |
| NEW        |     3 |        2.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 313 Row 21 Seats 19–20  avg $2,299/ea  total $4,598
Cheapest New: Sec 320 Row 20 Seats 17–18  avg $25,300/ea  total $50,600

## Category 3 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 52 groups, price range $4,073 – $271,400 total
G4 fetched: 21 groups → 63 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    60 |       95.2% | May exist in G2, not top-100   |
| NEW        |     3 |        4.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 330 Row 18 Seats 5–6  avg $2,038/ea  total $4,076
Cheapest New: Sec 330 Row 30 Seats 17–18  avg $2,012/ea  total $4,024

## Category 4 — Pair Derivation Analysis
Date: June 24, 2026

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
| Cat 1    |       0.0% |         6 |            765 | DERIVE          |
| Cat 2    |       0.0% |         3 |            147 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             60 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

