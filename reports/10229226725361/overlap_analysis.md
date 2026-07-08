## Category 1 — Pair Derivation Analysis
Date: July 8, 2026

G2 fetched: 451 groups, price range $3,898 – $403,650 total
G4 fetched: 251 groups → 753 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   747 |       99.2% | May exist in G2, not top-100   |
| NEW        |     6 |        0.8% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 135 Row 22 Seats 1–2  avg $2,012/ea  total $4,024
Cheapest New: Sec 130 Row 20 Seats 21–22  avg $258,750/ea  total $517,500

Pairs eligible for merge (NEW below G2 min $3,898): 0

## Category 2 — Pair Derivation Analysis
Date: July 8, 2026

G2 fetched: 158 groups, price range $3,220 – $229,999 total
G4 fetched: 57 groups → 171 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   171 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 314 Row 7 Seats 14–15  avg $2,070/ea  total $4,140
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: July 8, 2026

G2 fetched: 72 groups, price range $3,910 – $80,500 total
G4 fetched: 29 groups → 87 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    81 |       93.1% | May exist in G2, not top-100   |
| NEW        |     6 |        6.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 331 Row 23 Seats 17–18  avg $2,058/ea  total $4,116
Cheapest New: Sec 304 Row 24 Seats 5–6  avg $1,552/ea  total $3,104

Pairs eligible for merge (NEW below G2 min $3,910): 6

## Category 4 — Pair Derivation Analysis
Date: July 8, 2026

G2 fetched: 7 groups, price range $3,795 – $13,570 total
G4 fetched: 4 groups → 12 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       75.0% | May exist in G2, not top-100   |
| NEW        |     3 |       25.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 328 Row 28 Seats 3–4  avg $2,842/ea  total $5,684
Cheapest New: Sec 328 Row 30 Seats 2–3  avg $1,380/ea  total $2,760

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            747 | DERIVE          |
| Cat 2    |       0.0% |         0 |            171 | INVESTIGATE     |
| Cat 3    |       0.0% |         6 |             81 | DERIVE          |
| Cat 4    |       0.0% |         3 |              9 | SKIP            |

Overall recommendation: **DERIVE**

