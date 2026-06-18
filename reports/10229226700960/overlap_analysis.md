## Category 1 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 46 groups, price range $5,175 – $14,030 total
G4 fetched: 20 groups → 60 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    54 |       90.0% | May exist in G2, not top-100   |
| NEW        |     6 |       10.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **DERIVE** — Add only NEW pairs below G2 min total to G2 list.

Cheapest Duplicate: —
Cheapest In Range: Sec 245 Row 14 Seats 8–9  avg $2,760/ea  total $5,520
Cheapest New: Sec 219 Row 7 Seats 17–18  avg $2,415/ea  total $4,830

Pairs eligible for merge (NEW below G2 min $5,175): 3

## Category 2 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 33 groups, price range $3,315 – $69,805 total
G4 fetched: 12 groups → 36 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |    36 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **INVESTIGATE** — Many IN_RANGE pairs; consider paginated G2 fetch before adding.

Cheapest Duplicate: —
Cheapest In Range: Sec 418 Row 2 Seats 3–4  avg $1,941/ea  total $3,882
Cheapest New: —

## Category 3 — Pair Derivation Analysis
Date: June 18, 2026

G2 fetched: 8 groups, price range $3,450 – $9,198 total
G4 fetched: 3 groups → 9 derived adjacent pairs

| Bucket     | Count | % of derived | Notes                          |
|------------|-------|--------------|--------------------------------|
| DUPLICATE  |     0 |        0.0% | Already in G2 response         |
| IN_RANGE   |     9 |      100.0% | May exist in G2, not top-100   |
| NEW        |     0 |        0.0% | Genuinely new options          |

Overlap rate: 0.0% (DUPLICATE / total)
Verdict: **SKIP** — G2 API already surfaces pairs; derivation adds little.

Cheapest Duplicate: —
Cheapest In Range: Sec 435 Row 21 Seats 11–12  avg $3,105/ea  total $6,210
Cheapest New: —

## Summary Recommendation

| Category | Overlap Rate | NEW count | IN_RANGE count | Verdict         |
|----------|-------------|-----------|----------------|-----------------|
| Cat 1    |       0.0% |         6 |             54 | DERIVE          |
| Cat 2    |       0.0% |         0 |             36 | INVESTIGATE     |
| Cat 3    |       0.0% |         0 |              9 | SKIP            |

Overall recommendation: **DERIVE**

