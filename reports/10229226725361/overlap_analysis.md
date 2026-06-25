## Category 1 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 374 groups, price range $4,485 – $403,650 total
G4 fetched: 256 groups → 768 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   762 |       99.2% | May exist in G2, not top-100   |
| NEW        |     6 |        0.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 110 Row 21 Seats 8–9  avg $2,300/ea  total $4,600
Cheapest New: Sec 130 Row 20 Seats 21–22  avg $1,000,500/ea  total $2,001,000

Pairs eligible for merge (NEW below G2 min $4,485): 0

## Category 2 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 128 groups, price range $4,025 – $46,000 total
G4 fetched: 48 groups → 144 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   141 |       97.9% | May exist in G2, not top-100   |
| NEW        |     3 |        2.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 318 Row 22 Seats 17–18  avg $2,299/ea  total $4,598
Cheapest New: Sec 320 Row 20 Seats 17–18  avg $25,300/ea  total $50,600

## Category 3 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 52 groups, price range $4,061 – $271,400 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    57 |       95.0% | May exist in G2, not top-100   |
| NEW        |     3 |        5.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 335 Row 29 Seats 18–19  avg $2,207/ea  total $4,414
Cheapest New: Sec 330 Row 30 Seats 17–18  avg $2,012/ea  total $4,024

## Category 4 — Pair Derivation Analysis
Date: June 25, 2026

G2 fetched: 3 groups, price range $5,750 – $16,100 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 308 Row 26 Seats 1–2  avg $3,450/ea  total $6,900
Cheapest New: Sec 328 Row 28 Seats 3–4  avg $2,844/ea  total $5,688

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            762 | DERIVE          |
| Cat 2    |       0.0% |         3 |            141 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             57 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              6 | SKIP            |

Overall recommendation: **DERIVE**

