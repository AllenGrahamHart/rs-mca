# Keep The Moving Kernels Inside One Fixed Incidence Space

Translate both receiver coordinates by the FIXED a0,b0, obtaining u',v'.
Write a'=a_gamma-a0,b'=b_gamma-b0 and h'=a'+gamma*b'. Scalar
agreements and every original chosen defect are unchanged.

## 1. Moving Kernels And Their Exceptional Labels

Let U be the intersection of all e kernels ell_i. It has dimension s-e>0.
Choose dual v0,...,v_(e-1) in V and a basis phi_j of U. Then

    V_gamma=ker L_gamma
      =U+span{v_i-gamma^i*v0:1<=i<e}, dim V_gamma=s-1.

These sums are direct. In particular L_gamma is never the zero functional.
By(LINE), the actual explanation h' belongs to V_gamma.

The common zeros of U on the domain number at most K-s+e: every member
is divisible by their root product, and dim U=s-e>0. If evaluation
on V_gamma is zero at a selected joint-core coordinate x, then U(x)=0
and v_i(x)=gamma^i*v0(x) for1<=i<e. Since evaluation on V is nonzero
there, v0(x) cannot be zero. Since e>=2, x determines the UNIQUE label

    gamma=v1(x)/v0(x).

Discard from this LOW count every label having such a moving zero on
its selected joint core. At most K-s+e original labels are discarded,
each costing deficit at most T. No coordinate is removed from the common
domain and no original all-record resource is remeasured.

## 2. Every Defect Gives An Invertible Restricted Incidence Tuple

For a retained record choose L=m-T joint points from its m-tau_gamma
available joint points. All V_gamma evaluations there are nonzero. The
required weighted-carrier proof's local root-flat/greedy argument gives
at least

    B=L*product_(j=1)^(s-2)(d-T+j)

ordered independent(s-1)-bases on these points. Only its local basis
argument is used; a separate global fixed-carrier budget is NOT invoked.

The fixed ambient affine space has variables(z,y in V), dimension s+1.
At each coordinate x scalar incidence is the fixed linear equation

    z*v'(x)-y(x)=-u'(x).                            (INC)

The hypersurface Q=0 has a GLOBAL polynomial parametrization

    y=Phi(z,c,t)=sum c_j*phi_j
                   +sum_(i=1)^(e-1) t_i*(v_i-z^i*v0).

Its s coordinates are z,c,t; the differential is injective because z
and the coefficients along U,v1,...,v_(e-1) remain those same coordinates.
Its y-derivatives in c,t span V_gamma. Write y_z for its z-derivative
at the selected point. Differentiating L_z(Phi)=0 and the POLYNOMIAL
identity(LINE) gives, at z=gamma,

    L_gamma(y_z)+L'_gamma(h')=0,
    L_gamma(b') +L'_gamma(h')=0.

Thus b'-y_z belongs to V_gamma. This is formal differentiation over F,
valid also in positive characteristic, with no division by a factorial.

The z-column of the Jacobian of(INC) restricted to Phi is v'-y_z.
Subtract the appropriate other-column combination to replace it by v'-b'.
That column is zero on a selected joint-core basis and nonzero at EACH
defect. The other columns evaluate a basis of V_gamma. Therefore every
insertion of an original defect into an ordered core basis has an
invertible s-by-s restricted Jacobian. The tau_gamma*s*B tuples so
obtained are distinct within a record: its unique defect position and
the remaining ordered basis recover the construction.

## 3. A Fixed Tuple Has At Most e Owners

For any generated s-tuple the s fixed ambient linear equations have
rank s, since their restriction just had full rank. Their common solution
space in F^(s+1) is an affine line. Restrict Q to that line; it is a
univariate polynomial of degree at most e.

It is NOT the zero polynomial. Otherwise the nonzero direction of the
line lies in the tangent kernel of Q at a selected owner. This tangent
kernel is exactly the image of the differential of Phi: dQ/dy0=1 in
dual coordinates, so Q=0 is smooth and that image has dimension s.
The line direction would therefore be the image of a nonzero restricted
parameter direction annihilated by all s incidence equations. This
contradicts their invertible restricted Jacobian.

A nonzero degree-at-most-e polynomial has at most e distinct field roots.
Every owner gives one point on this line, and different original labels
have different z-coordinates. Hence there are at most e owners of a
common tuple. There are only(n)_s ordered tuples of distinct domain
coordinates. Summing tau_gamma*s*B and dividing proves(DEGREE).
Finally T+1-tau<=T*tau for every positive tau, and the discarded labels
each cost at most T. This proves the claimed full low-deficit bound.

For the stronger-basis interface, replace the local lower bound B in
section2 by the separately proved uniform B_*. The same record owns
at least tau_gamma*s*B_* tuples; all subsequent ownership and exception
arguments are unchanged. No per-carrier global budget is substituted.

For e=2 this recovers the previous split-cone mechanism after a sign and
functional relabeling. The proof uses neither characteristic zero nor
separately normalized moving-source budgets. A finite consumer must still
count graph lines whose restriction of Q is a NONZERO polynomial.
