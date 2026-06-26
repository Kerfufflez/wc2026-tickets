## Category 1 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 29 groups, price range $51,980 – $2,527,700 total
G4 fetched: 6 groups → 18 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |       83.3% | May exist in G2, not top-100   |
| NEW        |     3 |       16.7% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 121 Row 15 Seats 9–10  avg $27,140/ea  total $54,280
Cheapest New: Sec 103 Row 45 Seats 10–11  avg $25,300/ea  total $50,600

## Category 2 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 28 groups, price range $35,650 – $512,095 total
G4 fetched: 8 groups → 24 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    21 |       87.5% | May exist in G2, not top-100   |
| NEW        |     3 |       12.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 309 Row 24 Seats 1–2  avg $18,975/ea  total $37,950
Cheapest New: Sec 319 Row 18 Seats 13–14  avg $15,984/ea  total $31,968

## Category 3 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 17 groups, price range $36,306 – $356,500 total
G4 fetched: 11 groups → 33 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    24 |       72.7% | May exist in G2, not top-100   |
| NEW        |     9 |       27.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 302 Row 26 Seats 17–18  avg $22,219/ea  total $44,438
Cheapest New: Sec 303 Row 15 Seats 5–6  avg $15,761/ea  total $31,522

Pairs eligible for merge (NEW below G2 min $36,306): 9

## Category 4 — Pair Derivation Analysis
Date: June 26, 2026

G2 fetched: 6 groups, price range $27,600 – $63,284 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 331 Row 20 Seats 1–2  avg $17,250/ea  total $34,500
Cheapest New: Sec 331 Row 22 Seats 21–22  avg $33,350/ea  total $66,700

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         3 |             15 | INVESTIGATE     |
| Cat 2    |       0.0% |         3 |             21 | INVESTIGATE     |
| Cat 3    |       0.0% |         9 |             24 | DERIVE          |
| Cat 4    |       0.0% |         3 |              6 | SKIP            |

Overall recommendation: **DERIVE**

