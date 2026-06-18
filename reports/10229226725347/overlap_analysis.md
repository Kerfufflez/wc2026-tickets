## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 116 groups, price range $5,060 – $39,100 total
G4 fetched: 85 groups → 255 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   249 |       97.6% | May exist in G2, not top-100   |
| NEW        |     6 |        2.4% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 104 Row 27 Seats 7–8  avg $2,818/ea  total $5,636
Cheapest New: Sec 149 Row 34 Seats 24–25  avg $34,477/ea  total $68,954

Pairs eligible for merge (NEW below G2 min $5,060): 0

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 163 groups, price range $3,795 – $43,700 total
G4 fetched: 85 groups → 255 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   255 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 310 Row 26 Seats 23–24  avg $1,933/ea  total $3,866
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 53 groups, price range $3,450 – $23,000 total
G4 fetched: 31 groups → 93 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    87 |       93.5% | May exist in G2, not top-100   |
| NEW        |     6 |        6.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 326 Row 14 Seats 11–12  avg $1,834/ea  total $3,668
Cheapest New: Sec 350 Row 14 Seats 4–5  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $3,450): 0

## Category 4 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 3 groups, price range $5,750 – $8,050 total
G4 fetched: 1 groups → 3 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     3 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 321 Row 20 Seats 23–24  avg $3,220/ea  total $6,440
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            249 | DERIVE          |
| Cat 2    |       0.0% |         0 |            255 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             87 | DERIVE          |
| Cat 4    |       0.0% |         0 |              3 | SKIP            |

Overall recommendation: **DERIVE**

