# Most agreeing fibers have one parameter value

Status: PROVED. This extends the d=10 source payment to 8656..9526;
it does not extrapolate the earlier two-list Johnson denominator.
Keep the exact source contract and the generic maximal-family model
already proved in `maximal_parameter_family.md`. Write

    P=c*z^3+p*z^2+u*z+v,
    Q=-c*T*z^3+b*z^2+w*z+j,
    E=T*p+b, F=T*u+w, H=T*v+j,
    T*P+Q=E*z^2+F*z+H.

Here c is a nonzero constant, deg(p,b)<=4, deg(u,w)<=7,
deg(v,j)<=10, and E!=0 has degree <=5. Every nonsingular bounded
pair has one parameter eta(T) of degree <=3. All original receiver
values and coordinates remain as in `proof.md`.

## 1. A degree-sixteen polynomial controls double fibers

At a finite T-value with E!=0, two distinct parameters z1,z2 having
the same pair output satisfy

    z1+z2=-s, s=F/E,
    z1*z2=t, t=s^2-(p/c)*s+u/c.

Indeed the quadratic output gives the sum, and division of the cubic
output difference by z1-z2 gives the product. Thus both roots satisfy

    E^2*z^2+E*F*z+F^2+(E/c)*(u*b-p*w)=0.             (D)

The cancellation -p*F+u*E=u*b-p*w is important: its degree is <=11,
not the larger bound from separately pricing the two T-terms.

Over k(T), the monic quadratic z^2+s*z+t is the preimage polynomial
of the generic singular pair. For completeness, reduction of P modulo
this quadratic kills its linear coefficient and gives
P_s=(c*s-p)*t+v; the quadratic projection is also constant, so Q is
constant on its roots. If the roots differ this is a double fiber of
the birational normalization, hence a singular point. If they coincide,
both output derivatives vanish there, again giving the singular point:
normalization is an isomorphism over the smooth locus. The cubic has
exactly the one affine singular point from the existing normal form.

Consequently, for any GENERICALLY NONSINGULAR pair, substituting its
eta in (D) gives a NONZERO polynomial S_eta(T). Each term has degree
<=16: E^2*eta^2, E*F*eta, F^2 and E*(u*b-p*w)/c all do. An
identically zero polynomial would instead represent the singular pair,
which is charged separately.

## 2. Infinity is included in the same degree budget

Use degree-five homogenization of E, degree-eight of F, degree-three
of eta, and degree-sixteen of S_eta. At T=infinity the original
degree-ten outputs are

    P_inf=p4*z^2+u7*z+v10,
    Q_inf=-c*z^3+b4*z^2+w7*z+j10.

E_inf=p4. When p4!=0, the same sum/product calculation, now with
Q_inf as the cubic output, gives the double-fiber polynomial

    p4^2*z^2+p4*u7*z+u7^2+(p4/c)*(u7*b4-p4*w7).

This is exactly S_eta's degree-sixteen homogenization at infinity.
Thus there are at most sixteen projective T-values where a fixed
nonsingular pair agrees at a good fiber with a multivalued joint list.
The bad fibers E_hom=0 have at most five projective T-values.

## 3. Count single-valued lists on original coordinates

Pull back by rho=A(X)/B(X) of degree h. Every projective fiber
contains at most h original coordinates. Remove from the PARAMETER LIST
COUNT the bad E-fibers and every good coordinate whose received pair has
more than one allowed parameter value. For each nonsingular pair this
costs at most 5h+16h agreements. Constant receiver values need not agree
within a rho-fiber; the argument is coordinatewise.

Every remaining coordinate has at most one allowed value. Distinct
degree-three parameter sections agree at at most 3h original coordinates.
If a is the original joint agreement, put a1=a-21h. For a1>3h and
a1^2>3hn, the ordinary incidence proof therefore gives

    M<=floor(n*(a1-3h)/(a1^2-3hn)).                    (SL)

The removed coordinates are NOT deleted from the source, its complete
cores, or scalar-defect labels. The reduction pays their agreement loss
inside this auxiliary list bound only. Common multiplier zeros outside
the core union have no joint agreements; roots of B use the infinity
model above. The challenge field and original label units are unchanged.

## 4. Uniform new interval

For 8656<=J<=9526, the GP height theorem gives h<=952. Use

    n_max=1058102, a_min=75628, h_max=952,
    a1_min=55636, collision_max=2856.

These are legitimate incidence relaxations. Their Johnson denominator
is 73425184 and numerator 55846623560, giving M<=760 nonsingular
pairs in the dimension-four case. One singular pair and 64 off-curve
pairs give 825 LOW pairs in total.

If the coefficient dimension is <=3, the required weighted bound gives

    M<=floor(2^10*3^9*(1047625/66021)^3)=80530893115.

With base=C//5500+134944=4194116990084347 and at most 981604
finite labels per LOW pair, ALL d=10 coefficient dimensions satisfy

    N<=base+981604*(80530893115+64)
      =83243563858163463<B=274980728111395087.          (GP4)

This extends a source-class bound, not full-kernel coverage. The separate
kernel consumer may add another factor's LOW labels to these pair counts
while using the resource and near allowance only once. Neither a quartic
payment nor an unrestricted original-row theorem is asserted here.
