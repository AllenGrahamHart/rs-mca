# W3 — the chargeable pullback dictionary: a frozen grammar (v1)

- **Status:** DEFINITION / pre-registered. This grammar is FROZEN as
  v1 for the U1 falsification campaign (F4 + the toy harness). It may
  be revised only by an explicit v2 commit citing the falsifying or
  slack-revealing evidence — never silently.
- **Purpose:** make `u1_pte_trade_compression` testable and provable:
  "charged" must be decidable and countable.

## The grammar (v1)

A **ChargeablePullbackTradeFamily** over a row (D, k, A = k+t) is:

```text
DATA
  s        <= floor(log2 n)            map-orbit count
  psi_1..psi_s   rational maps, deg(psi_a) in (t, (log2 n)^2],
                 given up to the domain's PGL2-stabilizer action
                 (orbits: one representative + the acting subgroup)
  B_1..B_s       fixed tails, |B_a| < deg(psi_a)
  Y_1..Y_s       fiber-value sets, Y_a subseteq psi_a(D)

MEMBERSHIP  a locator L is CHARGED if its varying part (after the
  common core of the family's star-PTE normal form) is a union
    U_a U_{y in y(L)_a} psi_a^{-1}(y)   restricted to D, minus tails,
  with the zero-top-t coefficient constraint satisfied blockwise
  (each map's inter-fiber trades are order-t by the fiber
  symmetric-function dictionary).

COUNTING  the family's exact size is a product of binomials
  prod_a C(|Y_a^avail|, h_a)  — the staircase counting rule; these
  columns enter QA.22-style budgets as exact big integers.
```

## What v1 charges (the audit trail)

multiplicative staircases (one orbit, psi = X^M) | dihedral
(psi = X^M + zeta X^-M) | moment blocks (psi = the block's
zero-top-coefficient polynomial; scaled copies = one orbit under
the multiplicative action) | affine nets (degree-1... NOTE: v1's
degree floor deg > t excludes degree-1 maps; nets are charged at
b = 2 via their QUADRATIC trade closure per F3's charge lemma —
the F3 packet's cells are v1-expressible; if the harness finds
nets needing literal degree-1 clauses, that is v2 evidence).

## What v1 deliberately does NOT charge

arbitrary PTE trades (the star-PTE lemma makes those universal —
charging them is the tautology); unbounded map counts (s > log2 n);
maps of degree > (log2 n)^2; cross-family mixing without a shared
orbit. These exclusions are where falsification must attack:
F4's switch nets (many identical-defect gadgets = would need
s ~ R orbits) are the sharpest known candidate.

## The frozen test (for the harness and F4)

u1_primitive_star_pte_bound (v1): for every base locator at a toy
row, after removing star trades charged by SOME v1 family, at most
n^2 trades survive. Falsified by: any toy family with > n^2
v1-uncharged survivors. Confirmed at toys => U1 goes to proof
against grammar v1.
