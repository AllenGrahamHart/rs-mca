# PRO THREAD T6 — "E22-CF" (fresh window)

*Self-contained. The E22 source extraction. The shared TERMINAL (quotient
normal form) is already PROVED — this is the sunflower-specific SOURCE it needs.*

## Setting
E22 planted-sunflower worst-word challengers. D=mu_n (n dyadic), t=nullity param.
A non-planted listed codeword f=U*L_Z; on each touched petal i (agreement set T_i
subset petal P_i, a coset structure), the PROVED cofactor equation is
    U(x) L_{Z\C}(x) = a_i L_{C\Z}(x)  for x in T_i,
i.e. L_{T_i}(X) | H_i(X), H_i = U L_{Z\C} - a_i L_{C\Z}.

## What is proved (black boxes)
- **q_cofactor_normal_form (T2, PROVED):** if H is mu_M-covariant off a fiber-
  compatible bounded tail B (H(eta x)=eta^e H(x), equiv. H=X^e G(X^M)) AND the
  retained root set is the full off-tail zero set, then it is mu_M-invariant =>
  L_{T\B}(X)=prod_z(X^M - z). This is the terminal — supplied FOR you.
- **two_class_exhaustion (PROVED):** every non-planted word is mixed- or full-petal.
- **Full-petal case CLOSED:** a full petal beta*mu_M has locator X^M-beta^M = fiber.
- **fiber_locator_saturation, dyadic_local_to_common_saturation (PROVED).**

## What is NOT enough (verified obstructions — do not retry)
- Divisor constraints L_{T_i}|H_i ALONE do not force saturation (interpolation
  counterexample: U interpolating a_i on T_i=P_i\{u_i} defeats every |B|<min M_i).
- A quotient-SHAPED H with T one-point-short of full fibers also fails ('one point
  per fiber': T={alpha_0..alpha_M}, H=prod(X^M-z_j), L_T|H but T\B not fiber union).
  => COVARIANCE and OFF-TAIL EXHAUSTIVITY are BOTH load-bearing.

## The ask (target: e22_mixed_petal_covariance / E22-CF)
> From the actual E22 sunflower / moment-trade construction, prove there exist one
> common fiber-compatible tail B (|B|<min_i M_i), dyadic M_i>t, exponents e_i, s.t.
> off B: (i) H_i(eta x)=eta^{e_i}H_i(x) for eta in mu_{M_i} (covariance), AND
> (ii) T_i\B = {x in P_i\B : H_i(x)=0} (off-tail exhaustivity). Then
> q_cofactor_normal_form closes the factorization.

- **(A)** Extract (i)+(ii) from the sunflower model. The covariance should come from
  the moment-trade/square-shift building the petals as mu_M-cosets; exhaustivity from
  the agreement structure (T_i is the actual zero set on the petal). Identify exactly
  which construction feature supplies the mu_M-homogeneity of U, L_{Z\C}, L_{C\Z}, a_i.
- **(B)** a mixed-petal challenger with L_{T_i}|H_i whose cofactor is provably NOT
  mu_M-covariant off any bounded tail (a genuine non-quotient extra codeword).
- **(C)** conditional on a stated covariance/degree property of the sunflower model.

Downstream: closes e22 -> worst_word_challenger_pricing -> imgfib -> list_grand.
