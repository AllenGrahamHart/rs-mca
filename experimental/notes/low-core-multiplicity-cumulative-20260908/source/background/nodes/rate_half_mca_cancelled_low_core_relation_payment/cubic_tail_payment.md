# Every irreducible cubic on the double-point tail pays

Status: PROVED restricted source payment. Keep this consumer's exact
canonical normalized source on 9527..9821. Suppose all but <=256
LOW_500 pairs lie on one irreducible cubic G over F(X), whose primitive
weighted degree for (1,J-1,J-1) is <2*(J+66972). Then

    N<=274778805314695460,
    reserve>=201922796699627.                         (CT)

The source cover is a hypothesis HERE, independently proved by the
full-kernel child. Original finite labels, complete joint cores, raw
selection, all exceptions, HIGH resource and near remain unchanged.

## 1. Geometric classification and the larger weighted degree

Smooth cubics and rational-normalization cubics with at least two boundary
points have coefficient dimension <=1 by the existing suppliers. Their
direct original-coordinate pair cap is 163774741769. With 256 exceptions
and the /5500 resource/near base this is below (CT). Cubics irreducible
but not geometrically integral have at most six rational points, also paid.

For a one-boundary cubic singular at infinity, the generic classification
gives a polynomial cubic in its primitive linear projection. Its ACTUAL
new weighted degree gives

    h<=floor((2*(J+66972)-1-3*(J-1))/3)
      =floor((133946-J)/3)<=41473<51391.

Thus the existing coupled moving-projection theorem applies with its
height-51391 pair cap 223154201664. Charge 256 exceptions and the
one /5500 resource/near base; the total is again below (CT).
No old <A height bound is used for this <2A factor.

## 2. Affine-singular one-boundary cubics

Let d be actual projection-kernel dimension. The general weighted theorem
uses r=ceil(d/3) and pair count

    M<=floor(2^d*3^(22-d-r)*((1048577-h)/(66973-h))^r).

For 1<=d<11, the shared-carrier height theorem gives
h<=9820/floor(10/(11-d)); d=11 has h=0. At d=0 the coefficient
dimension is zero and M<=3^22. These bounds depend on the carrier,
not the increased interpolation weight.

The exact table in the kernel child's verify_double_point_cubic_tail.py checks every d
outside {7,10}. The largest whole-source total, including 256 exceptions,
is 268384711456990155 at d=11, below (CT).

For d=7,h<=1600, cumulative_low_accounting.md uses the required
resource's linear raw-weight bound and ALL nested LOW counts. It gives
(CT) without dropping low-label consumption or reusing an old discount.

For d=7,h>=1601, the component supplier's tail9821.md counts at most
1943 nonsingular pairs per top component and the entire lower-dimensional
complement. Including singular and 256 off-curve pairs gives
N<=142942788280886491.

For d=10, the GP supplier's tail9821.md includes all coefficient
dimensions, retains the 21h agreement loss and infinity, and gives
N<=83344622367408351 including the 256 exceptions.

These cases exhaust every irreducible cubic. Each branch supplies a
complete original-source price, so combine by MAXIMUM. A cubic occupies
the whole degree-three gcd; no additional factor groups are silently
discarded. Reducible covers have a separate line/complement proof.
