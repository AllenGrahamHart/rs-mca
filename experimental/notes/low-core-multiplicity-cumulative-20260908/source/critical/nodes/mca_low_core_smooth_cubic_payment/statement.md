# Smooth cubic joint lists and LOW group gains

Status: PROVED, 2026-09-07.

Let F have characteristic zero or >3, let V be an s-dimensional
subspace of degree-<K polynomials, s>=1, and fix affine offsets a_0,b_0.
Pairs lie in (a_0+V) x (b_0+V), with both component degrees <K.
Suppose they satisfy Q(a,b)=0 for one fixed total-degree-three
polynomial Q over F(X) whose projective homogenization is
geometrically smooth. On any n distinct evaluation points, the number
M_t of such pairs with at least m-t JOINT agreements to a received
pair, where K<=m-t<=n, satisfies

    M_t <= 3^(2s-1)*(n-K+1)/(m-t-K+1).                 (1)

If the cubic has nonconstant j-invariant, the stronger bound is

    M_t <= 3^(2s).                                    (2)

The same improvement holds whenever its elliptic surface over the
algebraic closure of F has a singular fiber. Fixed X-denominators
are cleared for coefficient identities only, without deleting domain
points. The cover degree is charged in the ORIGINAL 2s coordinates.

For a group of assigned finite LOW labels with raw margins 1..T,
complete pair cores, and supports as in the existing homogeneous-level
supplier, its gain G=sum_gamma(1-raw_gamma/(T+1)) satisfies

    G <= sum_(t=1)^T (n-m+t)*M_t/(t*(t+1)).            (3)

In the zero-dimensional case the simpler bound
G<=3^(2s)*(n-m+T) also holds. Partition pairs and their labels before
combining group prices; resource and HIGH labels are not charged here.

For s=11, (n,K,m)=(1048576+J,J,67472+J), T=500, the group
prices are <=159185671413625180 for any such smooth cubic, and
<=30803773636432836 for nonconstant j. The latter is less than
three ordinary factor units W=17200000000000000. Whole-source
totals and affine-factor cover composition are owned by the finite
consumer; this theorem does not supply a cubic identity for an
arbitrary source or price a singular generic cubic.
