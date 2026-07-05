# proof: e22 cofactor factorization proved MODULO the CF certificate (Pro W3, verified)

Target (C). The exact squarefree factorization holds once the E22 cofactor
equations supply a common-tail / kernel-saturation certificate; it is NOT
derivable from bare divisibility.

## The factorization (VERIFIED given CF)
D=mu_n. Certificate CF(B,{M_i}): one common tail B subset D with B subset T_i;
dyadic M_i | n with M_i > t; |B| < M_* = min_i M_i; and KERNEL SATURATION of the
non-tail support: (T_i \ B) mu_{M_i} = T_i \ B. Then with Z_i := {x^{M_i}: x in T_i\B},
    L_{T_i \ B}(X) = prod_{z in Z_i} (X^{M_i} - z),   squarefree.
Proof: x |-> x^{M_i} has fibers alpha*mu_{M_i}; saturation makes T_i\B a disjoint
union of full fibers; one fiber's locator is exactly X^{M_i} - z; disjoint fibers
=> coprime factors => squarefree (char F does not divide n). VERIFIED: p=97, n=16,
M=4, |S|=8 -> L_S == prod_z(X^M - z) exactly.

## Why not target A (verified counterexample)
Bare L_{T_i}|H_i does NOT force saturation: take distinct z_0..z_M in mu_{n/M},
one root alpha_j per fiber, T={alpha_0..alpha_M}, H=prod(X^M - z_j). Then L_T | H
but T has one point per fiber; if |B|<M then T\B lies in incomplete fibers, so NO
identity L_{T\B}=prod(X^M - z) holds. Hence the essential E22-specific content is
the certificate CF (common-tail extraction + full-fiber saturation), which the
actual cofactor equations must supply.

## Exact remaining obligation
Establish CF from the actual E22 cofactor equations: extract the common tail B and
prove kernel saturation (T_i\B)mu_{M_i}=T_i\B for the touched-petal cofactor
divisors. (Supporting full-fiber locator + local-to-common saturation lemmas are
already PROVED; this is the extraction step.)
