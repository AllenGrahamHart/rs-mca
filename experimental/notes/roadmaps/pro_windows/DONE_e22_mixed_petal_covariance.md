# proof: e22_mixed_petal_covariance — source identified (Pro T6, verified + Lean)

Source = SQUARE-SHIFT CHARACTER BALANCE + off-tail exhaustivity (NOT bare
divisibility). Terminal q_cofactor_normal_form (T2) proved. Off one common
fiber-compatible tail B (|B|<min M_i), both terms of H_i=U L_{Z\C}-a_i L_{C\Z} land
in the same mu_{M_i} character residue (balance u_i+z_i≡c_i mod M_i from the
moment-trade pairing) + off-tail exhaustivity T_i\B={x in P_i\B: H_i(x)=0} =>
H_i(eta x)=eta^{e_i}H_i(x) => mu_{M_i}-invariant => prod_z(X^{M_i}-z). Counterexample
VERIFIED (F_97, M=8): L_{T_i}|H_i holds but H_i matches any monomial c X^e on <=2/8
points => needs deleting 12>=M=8, impossible for |B|<M. Lean handoff stdlib-only, no
sorry (build not run — no lean in env). Remaining: cite square-shift balance from the
E22 moment-trade construction.
