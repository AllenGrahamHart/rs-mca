# proof: spi_component_control (Pro Brief G; refereed + verified)
THE SCROLL ARGUMENT (far stronger than the poly target): the alignment
incidence I_{u,v} = {(Z,[l]) in P^1 x P^j : M(Z)l = 0} for the Hankel pencil
M(Z) = Z0 Mu + Z1 Mv. Generic rank r over K(Z); a nonzero r x r minor Delta(Z)
has deg <= r <= t (entries linear in Z). On {Delta != 0} the kernel is a
projective bundle over an irreducible curve -> ONE horizontal component
(closure = a scroll, Segre degree <= (j+1-r) + r = j+1). All other components
live over rank-drop slopes, contained in {Delta = 0}: at most r <= t of them,
each fiber a single linear space. Hence #Irr(I_{u,v}) <= t+1 and
deg <= j+t+1; projection to X_{u,v} cannot increase components. Per paid
stratum L: restrict the pencil, same bound. GUARD: paid families must be
presented as polynomially many algebraic families (locator-coefficient
space), never support-enumerated. VERIFIED: rank-drop slopes <= r on 2500
random pencils (F_17).
