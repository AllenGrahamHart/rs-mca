# proof: e22 mixed-petal kernel invariance — conditional (Pro P1, verified)

## Pro P1 obstruction (verified): divisor constraints ALONE are insufficient
Counterexample: M=2^s>t, D=mu_{2M}, disjoint petals P_0=mu_M, P_1=gamma mu_M;
C=Z=empty (L_{C\Z}=1). Omit u_i in P_i, T_i=P_i\{u_i}, distinct a_i. Interpolate
U with U=a_i on T_i, U(u_i)!=a_i. Then H_i=U-a_i satisfies L_{T_i}|H_i for both
petals, BUT to make T_i\B a union of mu_{m_i}-orbits, B must contain the m_i-1
retained orbit points per petal, so |B| >= (m_0-1)+(m_1-1) >= min(m_i),
contradicting |B|<min M_i. So the divisor constraints do NOT force saturation —
a missing covariance/degree property is load-bearing. (Confirms my earlier read:
full-petal done, mixed completion needs sunflower-specific data.)

## Clean conditional closure (Pro P1)
Sufficient: for local moduli M_i>t, with B_light = union of light fibers
(|T_i ∩ fiber| <= t), assume (1) common-tail packing: one B ⊇ B_light, |B|<min M_i,
tail-compatible (B disjoint from any retained fiber); (2) low nonzero fiber
remainder: H_i restricted to a non-tail fiber is 0 or has <= t zeros; (3)
exhaustive agreement off tail: x in T_i iff H_i(x)=0. Then T_i\B is
mu_{M_i}-invariant. Cleaner COVARIANCE form: off B, H_i(eta x)=eta^{e_i}H_i(x),
i.e. H_i(X)=X^{e_i}G_i(X^{M_i}) on the petal coordinate — then roots off B are
automatically full fibers.

## Remaining obligation
Supply the degree/remainder OR covariance property from the actual E22 sunflower
construction (the mu_M-semi-invariance of the cofactor ratio U L_{Z\C}/L_{C\Z}
off a bounded tail). This is the exact sunflower-specific input.
