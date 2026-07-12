## Category 1 — Pair Derivation Analysis
Date: July 12, 2026

G2 fetched: 114 groups, price range $9,315 – $90,057 total
G4 fetched: 31 groups → 93 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    87 |       93.5% | May exist in G2, not top-100   |
| NEW        |     6 |        6.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 118 Row 19 Seats 8–9  avg $5,175/ea  total $10,350
Cheapest New: Sec 116 Row 44 Seats 41–42  avg $4,600/ea  total $9,200

Pairs eligible for merge (NEW below G2 min $9,315): 3

## Category 2 — Pair Derivation Analysis
Date: July 12, 2026

G2 fetched: 158 groups, price range $6,254 – $69,000 total
G4 fetched: 39 groups → 117 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   117 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 308 Row 16 Seats 6–7  avg $3,795/ea  total $7,590
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 12, 2026

G2 fetched: 159 groups, price range $5,750 – $345,000 total
G4 fetched: 45 groups → 135 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   135 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 324 Row 8 Seats 17–18  avg $3,289/ea  total $6,578
Cheapest New: —

## Category 4 — Pair Derivation Analysis
Date: July 12, 2026

G2 fetched: 15 groups, price range $6,394 – $80,500 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 310 Row 31 Seats 22–23  avg $5,750/ea  total $11,500
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |             87 | DERIVE          |
| Cat 2    |       0.0% |         0 |            117 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |            135 | INVESTIGATE     |
| Cat 4    |       0.0% |         0 |              6 | SKIP            |

Overall recommendation: **DERIVE**

