# Core-Union Restrictions Hold In Every Affine Pencil Section

Suppose neither of this node's fully paid source classes occurs. Fix
1<=t<=43 and any affine pencil subspace Z of dimension v in the original
pair carrier. Count its actual P43 pairs with COMPLETE core size>=m-t.
Empty/singleton intersections have size<=1 and satisfy every cap below.

Otherwise two distinct bounded-degree pairs determine a primitive row
of height h<J for the entire function-field pencil containing Z. Let U
be the union of complete cores of ALL P43 pairs on this full pencil,
not merely those belonging to the current affine section. Every counted
pair has all its >=m-t joint agreements in U, and scalar parameterization
there has the same affine dimension as Z. The scalar receiver is defined
at every point of U by primitive compatibility, without gcd-root deletion.

If h=0, absence of the paid constant class gives e=n-|U|>=567501.
Scalar affine incidence at degree J gives

    |Z intersect S_t|<=((|U|-J+1)/(m-t-J+1))^v
                      <=(481076/(67473-t))^v=C_t^v.

For h>=1 let ell be its lower band endpoint. Absence of the paid
nonconstant class gives e>=ebar+1, ebar=441382-8*ell. The parameter
polynomials have degree<J-h, so the scalar ratio is bounded by

    (R-ebar+h)/(d+1-t+h).

For fixed ebar,t this decreases with h, since R-ebar>d+1-t. Its maximum
on that band is attained at h=ell, where the ratio becomes

    (607194+9*ell)/(67473-t+ell)
       =9*(67466+ell)/(67473-t+ell).                        (BAND)

If t<=7 this is at most9. If t>=7 it decreases with ell, since the
derivative numerator is63-9t<=0. Its largest band endpoint is therefore
ell=1, giving607203/(67474-t). This proves the declared P_t bound for
every height, without sampling h or introducing a new pencil premise.

All scalar ratios used on a populated intersection are at least one:
U contains a complete core with >=m-t points and m-t>J-h. The relaxed
C_t,P_t are also at least one, with C_t<=P_t. Counting inside a smaller
affine section only restricts the same scalar family; it does not change
the original field, receiver, labels, raw values or complete union U.
This proves the hereditary condition needed for subsequent joint anchors.
