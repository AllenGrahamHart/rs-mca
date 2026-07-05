# PRO WINDOW — "DLI-FLATNESS" (fresh window)

*Self-contained. THE last analytic input of the primitive core; everything else in
the b2b -> pcf -> ejm chain is proved. The object is now pinned exactly and the
calibration below is REPRODUCED on it (not a hope). Prime-field only.*

## Setting
F_q, q ~ 2^256 PRIME (the extension-row case is handled separately — a proved
subfield/trace gate reduces it; here q is prime). mu_n subset F_q^*, n = 2^s,
n | q-1, t = 2^33. Square-root section sigma(zeta_{n/2}^i) = zeta_n^i
(i = 0..n/2-1; no opposite pair). Tower levels j = 0..33, level size L_j =
ceil(floor(t/2^j)/2), with sum_j L_j = t exactly (each m <= t is uniquely 2^j*odd).

A **central level-j profile** M assigns to each active coordinate y a bounded
symmetric domain D_j(M(y)) of the signed values d (the canonical central domains
are TERNARY D={-2,0,2} and, as the stress case, SIGNED D={-1,1}). Set
U_j(M) = prod_y |D_j(M(y))|. For the odd harmonics r = 2l-1 (l = 1..L_j),
v_y = zeta_n^{(2l-1)i} is the odd-evaluation vector, and the normalized joint
transform is
    F_M(lambda) = prod_y [ (1/|D_j(M(y))|) sum_{u in D_j(M(y))} psi(a_y(lambda) u) ],
    a_y(lambda) = sum_{l} lambda_l v_{y,l},   psi(x)=e^{2 pi i x/q},  lambda in F_q^{L_j}.

## The exact object (PROVED cascade, replayed exactly against the census)
    B_j(M) = q^{-L_j} sum_{lambda} prod_y (local transform)  =  q^{-L_j} U_j(M) * rho_j(M),
    rho_j(M) := B_j(M) / (q^{-L_j} U_j(M)) = sum_{lambda in F_q^{L_j}} F_M(lambda)
             = 1 + sum_{lambda != 0} F_M(lambda).
(lambda=0 gives F_M(0)=1, the balanced mean.) The primitive-core count is
    C_central = q^{-t} sum_{tower profiles} U(Pi) prod_j rho_j(M),
and the prize needs C_central <= 2^122, i.e. the U-weighted average of prod_j rho_j
is q^{o(t)}.

## What is proved (black boxes)
- **D3 reduction (verified, banked):** rho_j <= q^{eta_j} => EJM_2 => pcf_evaluation_flatness
  => b2b_primitive_core <= 2^122, with eta_j := log_q rho_j and sum_j eta_j = o(t) the requirement.
- **Vandermonde rigidity (proved):** if the active support of a nonzero level-j skew is
  <= L_j, it must be zero. So any nonzero deviation needs support >= L_j + 1 (enormous:
  level 0 needs >= 2^32+1 of the 2^40 cells). => rho_j - 1 is carried ENTIRELY by
  large-support skews.
- **Seen-coordinate lever (proved):** every nonzero frequency is nonzero on >= 255 L_j + 1
  of the 256 L_j coordinates (P_lambda = sigma * R_lambda, deg R <= L-1).
- **Bounded-coefficient norm gate (proved):** for |c| <= C and omega of 2-power order M,
  P_c(omega)=0 forces EITHER the cyclotomic/coset case (killed on tower sections: no
  opposite pairs => d=0) OR p | Res(X^{M/2}+1, Q_c) (the explicit cleared norm). Every
  nonzero tower skew is norm-gated at EVERY imposed odd r simultaneously:
  p | gcd_r Res(X^N+1, Q_{d,r}). No bounded-coefficient escape.
- **Circle constant (proved):** int_0^1 log|cos 2pi x|^2 dx = -2 log 2.

## Calibration (GROUND TRUTH — reproduced on the exact object this session)
Using the Fourier form above (no 3^N enumeration), in the MEANINGFUL large-N regime:
- TERNARY: rho_j -> 1.0000, eta* -> 0 (essentially flat) as N grows.
- SIGNED (stress case): eta* = 0.019 at mu_32 (N=16), DECREASING with N -> 0.
Both match the recorded mu_32 calibration exactly. (Small-N/large-q values are
artifacts: B collapses to the trivial vector; not the regime.)

## The ask (target: the deviation exponent is flat on the central measure)
> Prove  sum_{j=0}^{33} sup_{M central} |log_q rho_j(M)| = o(t),
> equivalently eta_j := log_q rho_j(M) is uniformly bounded (flat) on the central
> measure, so the U-weighted average of prod_j rho_j is q^{o(t)} and C_central <= 2^122.

- **(A) Prove flatness.** The lever: rho_j - 1 = sum_{lambda != 0} F_M(lambda), and each
  nonzero term is a normalized product that (i) requires support >= L_j+1 (Vandermonde),
  (ii) is norm-gated (p | gcd_r Res), and (iii) has >= 255 L_j + 1 seen coordinates each
  contributing |local| < 1. Show the surviving mass keeps eta_j = O(1) per level (or
  o(L_j)); with only 34 levels this gives sum_j eta_j = o(t). Handle the SIGNED-midpoint
  stress case explicitly (eta*=0.019 at mu_32, shown decreasing) and the m=1 zero atom.
- **(B) Refute:** a central profile / level whose deviation exponent eta_j is Omega(L_j)
  (not flat) at fixed nonzero lambda -- would break the tower route and force a different
  primitive-core mechanism.
- **(C) Conditional:** flatness modulo a clean bound on the number of large-support
  bounded-coefficient skews whose folded L_j resultants share the fixed ~2^250-bit prime q.

Downstream: closes dli -> ejm -> pcf -> b2b_primitive_core (<= 2^122) -> ... -> mca_safe.
Prime-field only; extension rows reduce via the proved subfield/trace gate.
