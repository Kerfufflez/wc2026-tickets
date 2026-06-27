## Category 1 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 217 groups, price range $4,450 – $55,022 total
G4 fetched: 87 groups → 261 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   249 |       95.4% | May exist in G2, not top-100   |
| NEW        |    12 |        4.6% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 229 Row K Seats 1–2  avg $2,347/ea  total $4,694
Cheapest New: Sec 233 Row NN Seats 104–105  avg $32,366/ea  total $64,732

Pairs eligible for merge (NEW below G2 min $4,450): 0

## Category 2 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 142 groups, price range $3,266 – $20,228 total
G4 fetched: 47 groups → 141 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   138 |       97.9% | May exist in G2, not top-100   |
| NEW        |     3 |        2.1% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 437 Row RR Seats 101–102  avg $2,023/ea  total $4,046
Cheapest New: Sec 440 Row PP Seats 8–9  avg $11,488/ea  total $22,976

## Category 3 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 32 groups, price range $3,722 – $34,500 total
G4 fetched: 15 groups → 45 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    45 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 450 Row MM Seats 3–4  avg $2,023/ea  total $4,046
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: June 27, 2026

G2 fetched: 5 groups, price range $3,910 – $9,786 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 453 Row XX Seats 2–3  avg $2,023/ea  total $4,046
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |        12 |            249 | DERIVE          |
| Cat 2    |       0.0% |         3 |            138 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |             45 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

