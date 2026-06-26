## Category 1 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 253 groups, price range $4,600 – $27,600 total
G4 fetched: 128 groups → 384 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   375 |       97.7% | May exist in G2, not top-100   |
| NEW        |     9 |        2.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 344 Row T Seats 1–2  avg $2,300/ea  total $4,600
Cheapest New: Sec 351 Row C Seats 9–10  avg $23,000/ea  total $46,000

Pairs eligible for merge (NEW below G2 min $4,600): 0

## Category 2 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 71 groups, price range $3,842 – $69,000 total
G4 fetched: 37 groups → 111 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   108 |       97.3% | May exist in G2, not top-100   |
| NEW        |     3 |        2.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 518 Row B Seats 7–8  avg $2,368/ea  total $4,736
Cheapest New: Sec 540 Row M Seats 16–17  avg $1,656/ea  total $3,312

## Category 3 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 25 groups, price range $3,450 – $27,600 total
G4 fetched: 14 groups → 42 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    39 |       92.9% | May exist in G2, not top-100   |
| NEW        |     3 |        7.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 641 Row K Seats 22–23  avg $2,299/ea  total $4,598
Cheapest New: Sec 625 Row E Seats 7–8  avg $14,375/ea  total $28,750

## Category 4 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 3 groups, price range $4,485 – $28,750 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     0 |        0.0% | May exist in G2, not top-100   |
| NEW        |     3 |      100.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: —
Cheapest New: Sec 750 Row P Seats 14–15  avg $1,955/ea  total $3,910

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         9 |            375 | DERIVE          |
| Cat 2    |       0.0% |         3 |            108 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             39 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              0 | SKIP            |

Overall recommendation: **DERIVE**

