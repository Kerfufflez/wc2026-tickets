## Category 1 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 32 groups, price range $9,200 – $69,000 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    15 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 422 Row 8 Seats 15–16  avg $5,002/ea  total $10,004
Cheapest New: —

## Category 2 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 11 groups, price range $9,154 – $16,215 total
G4 fetched: 2 groups → 6 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     6 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 522 Row 10 Seats 5–6  avg $5,705/ea  total $11,410
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 24, 2026

G2 fetched: 11 groups, price range $8,798 – $18,400 total
G4 fetched: 5 groups → 15 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |       60.0% | May exist in G2, not top-100   |
| NEW        |     6 |       40.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 649 Row 9 Seats 18–19  avg $5,750/ea  total $11,500
Cheapest New: Sec 665 Row 9 Seats 17–18  avg $14,375/ea  total $28,750

Pairs eligible for merge (NEW below G2 min $8,798): 0

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         0 |             15 | INVESTIGATE     |
| Cat 2    |       0.0% |         0 |              6 | SKIP            |
| Cat 3    |       0.0% |         6 |              9 | DERIVE          |

Overall recommendation: **DERIVE**

