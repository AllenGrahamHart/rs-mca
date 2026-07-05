# proof: petal_cofactor_chargeability — conditional on PRK_pet (Pro T7)

T2 is TERMINAL not generative (confirmed): it finishes a cofactor already in
X^e G(X^M) form but does NOT prove a residue-kernel family is chargeable. The
missing family-level step reduces to ONE lemma.

## Lemma PRK_pet(B0,b0) (the remaining leaf: petal_primitive_residue_kernel_rank)
Absolute B0,b0 s.t. for every full-petal in-regime chart and squarefree-realizable
cofactor family Y=A_i(Z) subset V_c, after peeling paid quotient/coset/signed/
antipodal/cyclotomic/low-defect sheets, the residual Y^u has (1) bounded primitive
tangent rank dim Pi_prim(T_y Y^u)<=B0, (2) no unbounded invisible primitive fibers
except absolute tails dim(T_y Y^u ∩ ker dPi_prim)<=b0, (3) uniform affine-linear
slicing => <=q^r points for dim r. USES the residue-kernel EQUATIONS + squarefree-
realizability — NOT dim K<=c+1 + T2 alone.

## Conditional theorem (PROVED given PRK_pet)
B_pet=B0+b0+b_tail. Every squarefree-realizable family is charged (T2 finishes) OR
uncharged with dim Pi_prim(Y)<=B_pet => <=q^{B_pet} points; summing gives
2^M poly(M) q^{B_pet}=n^{O(1)}, exponent c-INDEPENDENT.

## Route-cut (VERIFIED): dimension-excess alone is false
A_c={1+X+sum a_k X^k} has dim c-1 but support in classes 0,1 mod M => never a
pullback (VERIFIED earlier). So the proof MUST use the residue-kernel equations.
