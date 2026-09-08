# Proof of the whole normalized interval

## 1. One LOW/HIGH budget

Put R=1048576, d=67472, T=6, D=d-T=67466, M=J+D and c=D+1=67467.
The required maximum-density supplier gives a lower count B of ordered
core bases for every M-point actual core subset. Every raw<=6 record
therefore has at least 12*B independent incidence tuples.

For raw>=7 the completed-basis weight is at least L=10488/125.
Indeed its value at seven is at least 84*(1-77/67473)>L by the
eleven-factor product inequality. It increases on 7..84 because
12*84<67473; beyond 84 the old truncated weight is at least 84.
This includes margins above d, where the core formula is not used.

Write U(J)=(R+J)_falling_12 and P_d=prod_(i=1)^10(d+i). The common
resource F(J)=U(J)/[(J+d)*P_d] is at most

    C=23067643444721720934.

To verify the whole interval, write y=J+d. Each numerator factor is
y+(R-d-i), with R-d-i>0. Dividing their product by y gives a positive
sum of nonnegative powers and 1/y, hence a convex function. Endpoint
ceilings are 14024864706947406176 at 65000 and C at 169999.

Both label classes use the SAME tuple resource. Thus

    |Gamma|+134944
      <=max(floor(U(J)/(12*B)),floor(C/L))+134944.     (1)

The second quotient plus near is 274929007493481160. It remains to
bound the LOW quotient for every carrier. No LOW/HIGH maxima are added.

## 2. Exhaustive maximum-density split

Choose a maximum-density proper flat of the original nonzero evaluations,
with dimension j, cardinality a and density h=a/j. Put

    h_r(J)=1+(J-11)/r, h_5=(J-6)/5.

If h<=h_5, the hybrid root/density bound gives

    B>=(J+D)*prod_(i=1)^4(J+D-i*h_5)
                  *prod_(i=5)^10(D+11-i).           (2)

The quotient U/(12*B) for this lower bound decreases on the entire
interval. Put L0=R+65000-11. The numerator logarithmic derivative is
at most 12/L0. The first four variable denominator factors have slopes
1,4/5,3/5,2/5 and values at most D+169999. Their derivative sum is
at least 14/[5(D+169999)]>12/L0. All other factors help. At 65000,
the resulting floor plus near is 253456757626524982.

If h>h_5, the root-space bound a<=J-11+j implies h<=h_j. Since
h_j<=h_5 for j>=5, the maximizing flat must have 1<=j<=4, and

    j*h_5<a<=j*h_j=J-11+j.                           (3)

This is a proved exhaustive split, not a conjecture about the flat rank.
For j<=4 the supplier's coupled bound reduces B to the minimum of
P(M-t)*g_j(t) at t=0,a,c when c<=a. All factors and g_j are exactly
those in its statement. The rest of this proof certifies those quotients
for every J and every a in (3), including the endpoints as a relaxation.

## 3. A finite completeness router for a and t

In P, the degree and density bounds change order when

    e+i=i*a/j  <=>  a=j*h_(j+i)(J).

For j+i>=5, the degree bound is already the smaller one throughout (3).
Thus all possible breakpoints in a are

    a=j*h_r(J), r=j,j+1,...,5, and a=c when present. (4)

For fixed J, between these breakpoints every factor of P(M-t) is a
positive affine function of a, for each choice t=0,a,c. For t=a,
g_j(a) is positive log-concave on each side of a=c by the supplier's
proof. For t=0 or c, g_j(t) is constant in a. Consequently each product
is positive log-concave on its interval in a, and its minimum is at an
endpoint in (4). Restrict t=c to its actual domain a>=c.

The symbolic a variable need not be an integer in this minimization;
relaxing the actual integer cardinalities only weakens the lower bound.
No enumeration of original flats, supports or received words is required.

## 4. All-J bounds for the moving breakpoints

Fix 1<=j<=r<=5 and set a=j*h_r(J). The profile choices in P now
stay fixed: indices with j+i<r use density and the rest use degree.
The only additional t=a or t=c regime change is

    J_(j,r)=11+r*(c/j-1), where a=c.                 (5)

For t=0, all l=11-j>=7 factors of P(M) have positive J-coefficients.
After scaling each coefficient to one, its constant shift is at most
5D+50. Therefore the denominator logarithmic derivative is at least
7/(169999+5D+50)>12/L0, so the quotient decreases throughout.

For t=c, use P(J-1) on its valid domain. The same shifts are at most
50, and 7/(169999+50)>12/L0 again proves decrease. These shift bounds
follow directly from the density factor J+D-i*h_r and the degree
factor D+a+l-i (or their t=c versions): r<=5 and j>=1; every variable
factor has positive slope. No sign is extrapolated from endpoint tests.

For t=a and a>=c, g_j(a)=11*A_(j-1)*a. All P factors are positive
affine or constant in J, and the a factor alone gives logarithmic second
derivative at least 1/169999^2-12/L0^2>0 for the quotient. It is
log-convex, hence convex, on this regime.

For t=a and a<=c, put g=g_j. The supplier proves g'>0, g''>=0,
g'''<=0 and g'^2-g*g'' is increasing on [0,c]. Direct exact arithmetic
at c=67467 gives

    g'(0)^2-g(0)*g''(0)>=n_j*A_(j-1)^2,
    n_1=99, n_2=78, n_3=57, n_4=36.

Also g(a)<=A_(j-1)*(c+j-1+11a). Since a'=j/r and
J<=min(169999,6+5c/j) in this regime,

    -(log g(a(J)))'' >= n_j/E_j^2,
    E_1=2207258, E_2=4048025/2,
    E_3=4048030/3, E_4=4048035/4.

Indeed (c+j-1+11a)/a' is at most
(5/j)*(c+j-1)+11*(min(169999,6+5c/j)-6)=E_j.
The exact inequalities n_j*L0^2>12*E_j^2 hold for all four j.
The P factors contribute nonnegative curvature to the quotient, so
the quotient is log-convex here as well. Its maximum on either side
of (5) is therefore at an endpoint, not at an unchecked interior J.

Thus for each moving breakpoint in (4), it suffices to check
J=65000,169999 and J_(j,r) when it lies between them, with t=0,a
and t=c only when c<=a. Fractional J endpoints here are valid analytic
certificates bounding all integer J sources.

## 5. The constant breakpoint a=c

Its valid J interval is j*h_5<=c<=J-11+j. Profile changes occur
precisely at (5), with j<=r<=5. For t=0 or c each P factor is a
positive affine function of J or a positive constant on such a piece.
The factor J+D (t=0) or J-1 (t=c) gives quotient logarithmic second
derivative at least 1/(169999+D)^2-12/L0^2>0. Thus these quotients
are convex on every piece.

All internal boundaries are already covered by the moving tests at
J_(j,r), where a=c. The only additional outer boundary in this problem
is a=c at J=169999 for j=1, with t=0,c. At J=65000 this breakpoint
is outside the allowed range for every j. This completes the finite
router: exactly 91 indexed endpoint evaluations suffice, allowing
duplicate values from different symbolic branches.

## 6. Exact endpoint certificate and conclusion

The finite maxima of floor(U/[12*P*g_j])+134944 are:

    j=1: 266533517899145497, at J=65000, r=2, t=a=64991/2;
    j=2: 244377164689337849, at J=169999, r=2, t=a=169990;
    j=3: 244401081788492566, at J=169999, r=3, t=a=169991;
    j=4: 244417756062852746, at J=169999, r=4, t=a=169992.

Together with (2), the uniform LOW quotient plus near is at most
266533517899145497. This is smaller than the HIGH quotient plus near
in (1). Equation (1) proves (HIGH-INTERVAL), with reserve
274980728111395087-274929007493481160=51720617913927.

The two small implementations evaluate all 91 cases and certify the
listed curvature inequalities with exact arithmetic. Their finite
completeness is sections 2--5, not an assumption that sampled J values
are representative. Geometry and original-source transport are not
certified by arithmetic alone. No unrestricted original row or prize
closure is inferred from this normalized interval theorem.
