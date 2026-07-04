# A-closure pilot: W_h torsion census + eliminant feasibility

- **Status:** EXPERIMENTAL computational pilot (feasibility scouting, not a proof).
- **Branch:** `allen/prize-dag-delta`.
- **Verifier / driver:** `experimental/scripts/verify_a_pilot_wh_torsion.py`
  (single Python process, memory ceiling ~2 GB; every result below is
  reproduced by two independent methods inside that one script).
- **Upstream context:**
  `experimental/notes/roadmaps/x83_uniform_square_shift_obstruction_gate.md`
  (square-shift obstruction gate); the census confirms the qualitative X24
  dichotomy at the torsion level.

## What this pilot decides

For the (A)-closure we need, per `h` and per row order `n`, the NON-toral
torsion structure of the obstruction variety `W_h` and the discriminant/eliminant
data at Row-C scale `n = 1024`. This note reports the **feasibility curve**: what
is cheap (the direct root-of-unity census), what is expensive (the variable
eliminant), and hence whether the campaign can lean on a direct eliminant at
`n = 1024` or must use the structural shortcut the proof agent is formalising.

Setup (from X83). A split `2h`-support `R = {x_1,...,x_{2h}}` has locator
`C(X) = prod (X - x_i) = X^{2h} + c_{2h-1}X^{2h-1} + ... + c_0`. The forced monic
degree-`h` square root `S_R` is fixed top-down by dividing by 2; `E_R = S_R^2 - C`
has `deg <= h-1`. The obstructions are `O_i = [X^i] E_R`, `1 <= i <= h-1`; the
constant is `lambda_R = [X^0] E_R`. `W_h = {O_1 = ... = O_{h-1} = 0}`, a cone
(scaling-equivariant), anchored with `x_1 = 1`. Toral (paid-fiber) points:
`R = alpha*mu_h ∪ beta*mu_h`, two full `mu_h`-cosets (only exist when `h | n`).

---

## Task 1 — h = 4 obstruction polynomials (DONE, PASS)

Built the 3 obstructions in the locator-coefficient variables `c_0..c_7`
(monic `c_8 = 1`) directly from the forced top-down recursion. Independent
recomputation (linear solve of `[X^7..X^4] (S^2 - C) = 0` for `s_3..s_0`) gives
byte-identical polynomials — cross-check PASS.

Forced root coefficients:

```
s_3 = c7/2
s_2 = c6/2 - c7^2/8
s_1 = c5/2 - c6*c7/4 + c7^3/16
s_0 = c4/2 - c5*c7/4 - c6^2/8 + 3*c6*c7^2/16 - 5*c7^4/128
```

Obstructions (`#mon` = monomials in `c`):

```
O_3 = [X^3]E = -c3 + c4*c7/2 + c5*c6/2 - 3*c5*c7^2/8 - 3*c6^2*c7/8
              + 5*c6*c7^3/16 - 7*c7^5/128                              (#mon 7)
O_2 = [X^2]E = -c2 + c4*c6/2 - c4*c7^2/8 + c5^2/4 - c5*c6*c7/2
              + c5*c7^3/8 - c6^3/8 + 9*c6^2*c7^2/32 - 15*c6*c7^4/128
              + 7*c7^6/512                                             (#mon 10)
O_1 = [X^1]E = -c1 + c4*c5/2 - c4*c6*c7/4 + c4*c7^3/16 - c5^2*c7/4
              - c5*c6^2/8 + 5*c5*c6*c7^2/16 - 9*c5*c7^4/128 + c6^3*c7/16
              - 7*c6^2*c7^3/64 + 11*c6*c7^5/256 - 5*c7^7/1024          (#mon 12)
lambda = -c0 + c4^2/4 - ... + 25*c7^8/16384                           (#mon 15)
```

**Quasi-homogeneity / degree cross-check (PASS).** With weight `w(c_k)=2h-k`
each `O_i` is isobaric of weight `2h-i`, i.e. in the x-coordinates
`O_i(gamma R) = gamma^{2h-i} O_i(R)`:

| obstruction | x-degree (= 2h-i) | isobaric check |
|---|---|---|
| O_3 (i=3) | 5 | PASS |
| O_2 (i=2) | 6 | PASS |
| O_1 (i=1) | 7 | PASS |
| lambda    | 8 | PASS |

Largest 2-power denominator is `2^{14} = 16384` in `lambda`, matching the X83
clearing exponent `4h-2 = 14`.

**Toral sanity check (PASS).** A fiber pair `R = alpha*mu_4 ∪ beta*mu_4` has
`C = (X^4 - alpha^4)(X^4 - beta^4)`, i.e. `c_1=c_2=c_3=c_5=c_6=c_7=0`,
`c_4 = -(alpha^4+beta^4)`, `c_0 = alpha^4 beta^4`. Every monomial of
`O_1, O_2, O_3` contains at least one of `c_1,c_2,c_3,c_5,c_6,c_7`, so all three
vanish identically; and `lambda = -c_0 + c_4^2/4 = (alpha^4 - beta^4)^2/4`,
a nonzero square when `alpha^4 != beta^4`. Verified BOTH symbolically (in `c`)
and numerically by plugging the explicit `mu_16` cosets `alpha = 1`,
`beta = zeta_16` (so `alpha^4 = 1`, `beta^4 = i`) into the obstruction
expressions: `O_i = 0`, `lambda = (1 - i)^2/4 = -i/2`, a square. PASS.

---
