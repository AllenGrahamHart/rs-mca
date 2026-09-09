# Proof By Counting Every Recoverable Outside Coordinate

Choose a minimizing b_gamma in V and put a_gamma=h_gamma-gamma*b_gamma.
On the selected support, scalar agreement shows that v=b_gamma if and
only if both receiver components equal(a_gamma,b_gamma). Thus the in-support
joint core has size m-r_gamma.

Every joint-core evaluation of V is nonzero. Otherwise b_gamma(x)=0
and a_gamma(x)=h_*(x), so that coordinate would be in the assumed empty
universal carrier core. This assertion concerns joint cores, not all
coordinates in the source or all scalar agreement coordinates. Nonuniversal
carrier zeros elsewhere are retained, with no exceptional-label deletion.

For r_gamma<=T, choose a fixed subset H of m-T points of this joint core.
It has actual evaluation rank s, because m-T>=K and a nonzero polynomial
of degree<K cannot vanish on all of it. By hypothesis H has at least B
ordered bases. The incidence normals on H span the s-dimensional hyperplane
determined by the chosen b_gamma, as in the required completed-basis proof.
Each of the r_gamma defects lies outside that hyperplane.

For EACH defect insert it in each of s+1 positions of EACH ordered H-basis.
All resulting tuples are independent. Exactly one coordinate lies outside
H, so both that defect and its position are recoverable from the tuple.
The tuples from different defects are disjoint, not repeated copies of one
count. Thus the record owns at least r_gamma*beta tuples.

For r_gamma>T, the required nonuniform incidence proof gives at least

    m*P*min(d+1,r_gamma) >= (T+1)*m*P

independent tuples. Here its universally satisfied common-zero count is
zero by the same empty-carrier-core assumption. (HIGH) lower-bounds this
by kappa*beta. Consequently EVERY record owns at least
beta*min(r_gamma,kappa) independent tuples, with no gap in raw values.

Distinct selected finite slopes own disjoint independent tuples. There
are at most U ordered tuples in the full original domain. Summing and
flooring the integer weighted count proves(MASS).

For each positive integer raw, min(raw,t+1) equals t+1 minus the number
of j in1..t with raw<=j. Sum this identity to get(FLAG); its left-side
truncated mass is at most the kappa-truncated mass. Since the nested
counts satisfy L_j<=L_t for j<=t, (TAIL) and its inverse payment follow.
Different proved caps on the nested L_j may also be used directly in
(FLAG). This is an exact weighted identity, not disjointness of those sets.

This sharpens the one-defect insertion interface by retaining the actual
number of available defects before summation. It credits the existing
incidence and polynomial-basis theorems. It introduces no new resource,
receiver descent, field change, canonical choice or source classification.

For(OWNER), a label assigned to f uses exactly raw_gamma coordinates of
its selected support outside H_f. These subsets are disjoint for distinct
assigned labels: at such a coordinate the nontrivial scalar equation
(u-a)+gamma*(v-b)=0 has at most one finite solution gamma. Thus their
total raw is at most n-|H_f|. Each raw is at least c_f, both by the support
size and by full-code badness. Consequently

    kappa-raw <=((kappa-c_f)/c_f)*raw.

Sum and floor the integer deficit to prove(OWNER). No canonical premise
is needed here and no coordinate is counted twice for the SAME owner.
Different owners may reuse coordinates; their census remains an explicit
obligation and is not bounded by this argument alone.
