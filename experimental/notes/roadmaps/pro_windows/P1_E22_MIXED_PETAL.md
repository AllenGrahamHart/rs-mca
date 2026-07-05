# PRO WINDOW P1 — "E22-MIXED-PETAL"

*Self-contained. One sharp algebra obligation: the sole remaining core of the
entire 46-node E22 worst-word program. Everything else is proved.*

## Setting
D = mu_n (n-th roots of unity, n dyadic), t = nullity parameter. An E22 planted
sunflower receiver plants r petals sharing a core C; each petal is a coset of a
dyadic subgroup. A non-planted listed codeword f = U * L_Z (L_Z = zero-agreement
locator, U = cofactor). On each touched petal i with agreement set T_i, the
PROVED cofactor equation is
    U(x) L_{Z\C}(x) = a_i L_{C\Z}(x)   for x in T_i,
equivalently the divisibility L_{T_i}(X) | H_i(X), H_i = U L_{Z\C} - a_i L_{C\Z}.

## What is proved (black boxes)
- two_class_exhaustion: every non-planted word is mixed-petal or full-petal.
- FULL-PETAL is already saturated: a full petal beta*mu_M has locator
  L = X^M - beta^M = the exact fiber of x->x^M over beta^M (VERIFIED).
- kernel_invariance_full_fiber_criterion: S is a union of full x->x^M fibers IFF
  S is mu_M-invariant (x in S, eta^M=1 => x eta in S).
- dyadic_local_to_common_saturation: local M_j-fiber blocks (M_j>t) glue to one
  common M_* = min M_j fiber structure.
- fiber_locator_saturation: X^M - z | L_R  iff  the whole fiber over z is in R.
- tail_removed_quotient_factor_passthrough: once the structure is known, the
  factors X^{M_i}-z pass through the divisor relation formally.

## The ask (the single irreducible core: e22_cofactor_common_tail_kernel_invariance)
> From the cofactor divisibility constraints L_{T_i}(X) | H_i(X) for the
> MIXED-petal challengers, construct one common exceptional tail B and dyadic
> local moduli M_i > t with |B| < min_i M_i, and prove that each non-tail set
> T_i \ B is mu_{M_i}-kernel-invariant (hence a union of full x->x^{M_i} fibers).

- **(A) Prove the mixed-petal completion:** show the partial agreements across
  several petals, under the sunflower degree/scalar data, force mu_M-invariance
  after removing a bounded tail. Likely lever: a degree-count / completion
  argument — a bounded-degree H_i divisible by many partial-coset locators must
  in fact be divisible by the FULL coset locators X^M - z (so the missing fiber
  points are forced roots). Make the tail bound |B| < min M_i explicit.
- **(B) Refute:** a mixed-petal divisor pattern satisfying all L_{T_i}|H_i whose
  non-tail roots are NOT mu_M-saturated for any M>t and any bounded tail.
- **(C) Conditional:** the completion modulo a clean stated covariance/degree
  hypothesis on (U, L_{Z\C}, L_{C\Z}, a_i) — and please state exactly which
  property of the sunflower construction you need (so we can supply it).

Downstream: closes e22_cofactor_coset_saturation -> the tail-removed factor
manifest -> worst_word_challenger_pricing -> list_grand (the list side of the prize).
