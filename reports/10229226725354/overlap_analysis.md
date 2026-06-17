## Category 1 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 135 groups, price range $6,130 – $60,950 total
G4 fetched: 68 groups → 204 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   198 |       97.1% | May exist in G2, not top-100   |
| NEW        |     6 |        2.9% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 231 Row 14 Seats 9–10  avg $3,344/ea  total $6,688
Cheapest New: Sec 233 Row 2 Seats 17–18  avg $126,989/ea  total $253,978

Pairs eligible for merge (NEW below G2 min $6,130): 0

## Category 2 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 197 groups, price range $4,025 – $57,500 total
G4 fetched: 135 groups → 405 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |   405 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 542 Row 22 Seats 21–22  avg $2,240/ea  total $4,480
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 50 groups, price range $4,025 – $32,200 total
G4 fetched: 22 groups → 66 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    63 |       95.5% | May exist in G2, not top-100   |
| NEW        |     3 |        4.5% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 551 Row 19 Seats 20–21  avg $2,299/ea  total $4,598
Cheapest New: Sec 548 Row 21 Seats 13–14  avg $28,750/ea  total $57,500

## Category 4 — Pair Derivation Analysis
Date: June 17, 2026

G2 fetched: 3 groups, price range $6,325 – $28,750 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       66.7% | May exist in G2, not top-100   |
| NEW        |     3 |       33.3% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 504 Row 21 Seats 1–2  avg $4,145/ea  total $8,290
Cheapest New: Sec 526 Row 12 Seats 1–2  avg $17,250/ea  total $34,500

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |            198 | DERIVE          |
| Cat 2    |       0.0% |         0 |            405 | INVESTIGATE     |
| Cat 3    |       0.0% |         3 |             63 | INVESTIGATE     |
| Cat 4    |       0.0% |         3 |              6 | SKIP            |

Overall recommendation: **DERIVE**

