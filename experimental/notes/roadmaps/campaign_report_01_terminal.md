# The terminal open problem (community-facing)

- **Status:** DRAFT / living. Sibling of `campaign_report_00_overview`.
- **Purpose:** state the single estimate the clean-rate MCA
  determination reduces to, in self-contained additive-combinatorics
  language, with the proved base cases and the empirical profile — so
  it can be posed to specialists independently of the prize framing.

## The problem

Let `n = 2^s`, let `H = mu_n` be the group of `n`-th roots of unity
in `F_q` with `n | q-1`, and let `p = char(F_q) >= n^2`. For an
integer `h` with `3 <= h <= (log_2 n)^2`, call two disjoint
`h`-subsets `P, Q ⊂ H` a **trade** if their first `h-1` power sums
agree (equivalently their locator polynomials `L_P, L_Q` differ by a
constant). A trade is **charged** if the common connecting map
`ψ = L_P` factors through a symmetry of `G_m` — i.e. `ψ = F(x^m)`
(cyclic) or `ψ = F(x^m + a x^{-m})` (dihedral), or through the
boundary/coset and moment-block forms — and **primitive** otherwise.

> **Conjecture (terminal estimate).** For `h >= 3`, the number of
> primitive trades in `H` is at most `n^3` per anchored core
> (equivalently the anchored primitive active-core count is
> `<= n^{1+o(1)}`). In sharpest empirical form: for `q >= n^3`,
> there are **no** primitive trades at all.

Any polynomial bound closes the application (the constant `n^3`
suffices after the verified compiler rewiring; the sharp `n^{1/3}`
active-core form is the trophy).

## What is proved

- **`h = 2`** (not needed by the application but the method's base):
  primitive trades number `<= 6 n^{5/3}`, via Corvaja-Zannier /
  Garcia-Voloch subgroup-point bounds on the line `x + y = s`.
- **`h = 3`, the cubic cap:** primitive (indeed *all* anchored)
  active pairs number `< n^3`. Proof: the solution triples matching
  the top two symmetric sums of `{1,a,b}` are an explicit rational
  parametrization `(x(t),y(t),z(t))`, `D = t^2+t+1`; membership
  `x(t) in H` forces `t` to be a root of the nonzero degree-`<=2n`
  polynomial `N_x(t)^n - D(t)^n` (nonzero because `N_x = D` forces the
  invalid core `a=b=1`), giving `<= 2n` partners per core and
  `C(n-1,2)` cores.
- **The charged classification** is complete: charged = the pullback
  class, and (tame Laurent-Ritt, self-contained) the only toral
  symmetries are `x^m` and `x^m + a x^{-m}`.

## Empirical profile

- In-range primitive counts are single digits: `C_3 = 18` at
  `(n,q)=(128,17921)`, `129` at `(256,65537)`; multiplicity
  `K(P) = 1` throughout.
- **Vanishing at high `q`:** across every tested row, `q >= n^3`
  gives count `0` (`n` up to `256`, and `h = 4` up to `n = 64`).
- The transition below `n^3` is **non-monotone** (e.g. `n=32` has a
  nonzero count at `q ~ n^{9/4}` between zeros) — an
  exceptional-prime effect, not a smooth density threshold.

## Why standard tools stop (each failure quantified in-repo)

Weil sums (subgroup below the `sqrt(q)` floor); single-curve
subgroup-point bounds (our count is a moving family in `(G_m)^{2h-1}`;
summing per-curve diverges); finite-field quadratic Vinogradov mean
value (`n^{2h-3-1/9}`, too weak); characteristic-zero lifting
(threshold `C^{phi(n)}`); resultant elimination (degree-`n` objects).
The one mercy: the application affords any exponent up to `q >= n^6`,
and the empirical transition is at `n^3`.

## Update (2026-07-04): the dichotomy — the problem is no longer a point count

The "missing high-dimensional point-count" framing above is
superseded. A verified chain (`x24`/`x81`/`x83` + the good-reduction
lemma `a3`, all with green verifiers and independent replays) now
gives:

1. **The universal obstruction gate.** A 2h-support underlies a trade
   iff a forced square-shift system vanishes; the obstruction variety
   `W_h` is a *graph* in coefficient space, depends only on `h`, and
   is scaling-equivariant.
2. **Char-0 classification (complete).** Characteristic-zero trades
   are exactly full `mu_h`-fiber pairs (2-power `h`; none otherwise).
   Verified censuses: non-toral char-0 torsion EMPTY at every tested
   `(n, h)`.
3. **Good reduction (proved, fixed `(n,h)`).** Away from an explicit
   finite exceptional set of primes, finite-row trades do not exceed
   the char-0 structure. Validated end-to-end at `(16,3)`: predicted
   exceptional set `{7, 17, 97}` matches brute force both directions —
   the observed "exceptional primes" (F_193 etc.) *are* the bad
   reduction primes.

**What actually remains** is certification, not theory: (i) direct
MITM certificates at the window's bottom (`h = 4/5`, feasible,
running); (ii) a descent-injection certificate for mid `h <= ~10`
(seed identity verified; band budget saturates at `~log2 h` levels);
(iii) the `h`-window cap derivation (which `h` the consumers need —
in audit); (iv) if the window reaches `h >= ~16`, a large-h emptiness
lemma (first moment empty by hundreds of bits). The giant regime
(prize-max rows) is decomposed separately: the char-0 coset theorem
is proved (Galois-orbit argument); the residue is a no-concentration
bound with a 123-bit cushion at the first-moment balance point.
