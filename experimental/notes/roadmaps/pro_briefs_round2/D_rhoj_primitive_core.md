# Pro brief D — the rho_j product bound (primitive-core count)

*Self-contained; round 2 of the skew-tower thread. Elementary finite-field /
power-sum mathematics; all proved inputs stated inline.*

## Setup
`F_q`, `q ~ 2^256` prime; `mu_n subset F_q^*` the `n`-th roots of unity,
`n = 2^41`; a nullity parameter `t ~ 2^33`. A subset `A subset mu_n` is
`t`-null if its power sums `sum_{y in A} y^m = 0` for `m = 1..t`. Write each
`A` via the dyadic skew tower: at level `j`, a multiplicity function `m_{j+1}`
on a square-root section splits into lower multiplicities with skew
coefficient `d(y) = a - b in D_j`, `|d| <= 2^j`, `d ≡ m (mod 2)`. Set
`T_j = floor(t/2^j)`, `L_j = ceil(T_j / 2)`. Key identity (proved):
`sum_{j>=0} L_j = t` (each `1 <= m <= t` is uniquely `2^j * odd`).

## Proved inputs (the skew-tower packet, verified 12/12)
1. **Level-`j` branch factor** `B_j(M) = #{ d : d(y) in D_j(M(y)),
   sum_y d(y) sigma(y)^r = 0 for all odd r <= 2L_j - 1 }`, and the EXACT
   character-sum cascade `B_j(M) = q^{-L_j} sum_{lambda in F_q^{L_j}}
   prod_y ( sum_{d in D_j(M(y))} psi(d lambda . v_y) )`, `v_y =
   (sigma(y), sigma(y)^3, ..., sigma(y)^{2L_j-1})`. The `lambda = 0` term is
   the balanced mean `q^{-L_j} U_j(M)`, `U_j = prod_y |D_j(M(y))|`.
2. **Bounded-coefficient norm gate (proved):** every nonzero tower skew is
   norm-gated at every imposed odd `r` simultaneously:
   `q | gcd_r Res(X^N + 1, Q_{d,r})`, `Q_{d,r}` the folded polynomial. No
   bounded-coefficient escape; the only char-0 relations are opposite-pair
   (coset), absent in a section.
3. **Vandermonde support thresholds (proved):** a nonzero level-`j` skew has
   active support `>= L_j + 1`; at `t = 2^33` this is `>= 2^{32-j} + 1`
   (level 0: `2^32 + 1` of `2^40` cells).
4. **Two-level gate bound (proved):** the levels 0/1 non-coset excess is
   carried entirely by skews of support `>= 2^32+1 / 2^31+1`, each passing
   the simultaneous resultant gates for the fixed prime `q`.

## The exact target
Define `rho_j(M) = B_j(M) / (q^{-L_j} U_j(M))` (deviation from balance). The
central count is `C_central = q^{-t} sum_Pi U(Pi) prod_j rho_j(M_{j+1})`. The
prize needs

```
    #{ t-null primitive B : t+16 <= |B| <= n/2 }  <=  2^122
```

(after complement duality, the `M>t` dictionary, the `M_0`-boundary class and
the proved near-tails; interpolation is dead here — it reaches `2^128`).
Equivalently, `C_central = q^{-t + o(t)} sum_Pi U(Pi)`, i.e.

```
    log_q ( weighted-average over the central tower measure of prod_j rho_j )
        =  o(t).
```

Sufficient (proved reduction): `sum_j sup_{M central} |log_q rho_j(M)| = o(t)`
— per-level rigidity.

## The ask (choose your target; reformulation welcome)
- **(A) Full bound:** `prod_j rho_j = q^{o(t)}` on the central measure (hence
  the count `<= 2^122`). The lever is the norm gate: `rho_j` deviates from `1`
  only through nonzero skews, which (by 3,4) have huge support AND fixed-prime
  resultant divisibility — bound the number/weight of large-support bounded-
  coefficient vectors whose `L_j` folded resultants share the fixed
  `~2^250`-bit prime.
- **(B) The divisor-pair route:** exploit BOTH constrained halves of
  `L_A L_{A^c} = X^n - 1` (complement duality) simultaneously — a
  skew-equation rigidity at successive scales.
- **(C) Conditional:** the count `<= 2^122` modulo a clean per-level rigidity
  hypothesis (e.g. `sup log_q rho_j <= L_j / polylog`), reducing the core to
  that one estimate.

Numerical anchors (replayable at exceptional prime 17 / inert 97, 193): the
branching `#valid skews per profile = #{ eps in {+-1}^k : sum eps_i sigma(y_i)
= 0 }` — the signed sparse vanishing-sum object (rich at 17, zero at 97/193).
