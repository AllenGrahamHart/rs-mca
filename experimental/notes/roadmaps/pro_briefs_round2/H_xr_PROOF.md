# proof: light-triangle eliminant nonvanishing (Pro, basis-free; verified)

The inventory obligation is discharged by a UNIFORM parametric certificate:
one argument covers every light profile at once (stronger than a per-profile
record table; covers paid/boundary too).

## The map
The normal-form matrix (= evaluator's, verified normal_rank == brute_rank) is
Phi_z: Lambda_{T0} + Lambda_{T1} + Lambda_{T2} -> F^U + F^U,
  (l0,l1,l2) |-> (l0+l1+l2, z0 l0 + z1 l1 + z2 l2), each li zero off Ti.
dim Lambda_Ti = t, so full column rank 3t <=> injectivity.

## The certificate (admissible specialization: points distinct, slopes pairwise distinct)
Let I = T0 ∩ T1 ∩ T2, r = |I|. Since I ⊆ Ti ∩ Tj for all three pairs,
pair_sum = |T0∩T1|+|T0∩T2|+|T1∩T2| >= 3r, so pair_sum - trip >= 2r. The light
inequality pair_sum - trip <= 2k then gives r <= k.

Take (l0,l1,l2) in ker Phi_z. At u in U:
- u in exactly one Ti: the two rows force li(u)=0.
- u in exactly two Ti,Tj: [[1,1],[zi,zj]] (li(u),lj(u))^T = 0 with det zj-zi != 0,
  so li(u)=lj(u)=0.
Hence each li is supported only on I. But li in Lambda_Ti obeys the k moment
equations sum_{u in Ti} li(u) x_u^d = 0 (d=0..k-1); restricted to support I,
sum_{u in I} li(u) x_u^d = 0. The k x r Vandermonde on the distinct {x_u : u in I}
has full column rank since r <= k, forcing li|_I = 0. So l0=l1=l2=0: Phi_z is
injective, rank 3t. Thus some 3t x 3t maximal minor is nonzero at this
specialization, hence is not the zero polynomial. QED.

## Verification
- Mechanism replayed (verify_pro_proof.py): on 2837 light triples,
  pair_sum-trip >= 2r, r <= k, and full rank 3t at distinct slopes ALL hold.
- Independent census (notes/census_result.md): 152/152 light profile types
  certified nonvanishing across k=2..6, 0 gaps.

The paid/non-boundary distinction is NOT needed: nonvanishing holds for every
light profile. This directly proves xr_profile_eliminant_nonvanishing.
