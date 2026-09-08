# Polynomial core gluing and the received-pair defect

Status: PROVED, by elementary linear algebra and the root bound.

Let D be a finite set of distinct field elements, K>=1, and let a nonempty
finite family of subsets H_i have union U. C_K(X) denotes the evaluation
IMAGE of degree-`<K` polynomials on X, even when |X|<K. Define

```text
A_H={lambda in (F^U)*: supp(lambda) subset H, lambda(C_K(U))=0},
A=sum_i A_(H_i),
L={f in F^U: f|H_i in C_K(H_i) for all i},
Q=L/C_K(U).
```

Then `A^perp=L`, `A_U^perp=C_K(U)`, and
`dim Q=dim A_U-dim A`. Thus A=A_U exactly when every local section is
represented by one degree-`<K` polynomial throughout U.

If each H_i is a complete agreement core of the SAME received pair
(r_0,r_1) with a degree-`<K` polynomial pair, the restrictions of both
received components lie in L. Their image span in Q has dimension c in
{0,1,2}. Respectively, both components are global polynomial restrictions;
exactly one projective linear combination is global; or no nonzero
combination is global. The full dimension of Q need not be at most two.

If the cores can be ordered with |H_1|>=K and
`|H_i intersect (H_1 union ... union H_(i-1))|>=K` for every i>=2,
then Q=0 and hence c=0. This is sufficient, not an asserted property of
actual core families. No converse or numerical count is claimed. The
statement permits empty individual cores and union, with the usual zero
evaluation-space conventions.

## High-band continuation, 2026-09-06

Suppose every projective scalar combination of a received pair has
agreement at most A=k+h with every degree-<k codeword, where h>=2.
For distinct polynomial pairs with complete cores of sizes k+d_i,
1<=d_i<=h-1, any two with d_i+d_j>=h already force received-pair
gluing defect two. Their core intersection has size at most k-2, and
their two component-difference polynomials are linearly independent.

For a family wholly at depths >=ceil(h/2), the gluing defect is zero
exactly when there is at most one pair, and two exactly when there are
at least two pairs. Defect one is impossible. A defect-at-most-one
container cannot combine a cascade pair with any other positive-depth
band pair.

Under the actual exact-A support selector, a single pair at depth d
carries at most floor((n-k-d)/(h-d)) slopes. Thus the defect-at-most-one
high-band branch is paid by at most one pair and at most n slopes.
The potentially large defect-two population is not bounded. These facts
hold at either window rank and do not identify the two notions of rank.
See [the proof and boundary control](high_band_defect.md).
