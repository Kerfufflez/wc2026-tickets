## Category 1 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 30 groups, price range $9,200 – $69,000 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 454 Row 3 Seats 5–6  avg $4,600/ea  total $9,200
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 10 groups, price range $9,154 – $17,181 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 520 Row 11 Seats 14–15  avg $6,210/ea  total $12,420
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 23, 2026

G2 fetched: 10 groups, price range $8,798 – $17,250 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |       40.0% | May exist in G2, not top-100   |
| NEW        |     9 |       60.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 649 Row 9 Seats 18–19  avg $5,750/ea  total $11,500
Cheapest New: Sec 644 Row 6 Seats 9–10  avg $9,200/ea  total $18,400

Pairs eligible for merge (NEW below G2 min $8,798): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             15 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |              6 | SKIP            |
| Cat 3    |       0.0% |         9 |              6 | DERIVE          |

Overall recommendation: **DERIVE**

