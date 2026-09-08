# Rank Five When The Inside Core Is Smaller Than c

Status: PROVED supplement to the existing coupled-basis theorem.
Keep its actual dimension-eleven source and maximum-density flat, but
allow j=5 provided a<=c and c>=100. Then its same formula (FLAT)
is valid, with t in [0,a] and

    g_5(t)=prod_(i=0)^4(c+i-t)+11*A_4*t.

The minimum is at t=0 or a. Restricted intervals [0,b], b<=a, likewise
need only 0 and b. The original j<=4 theorem is unchanged.

## Do Not Discard The Negative Coefficients

The exact inside-extension coupling in proof.md gives, after the b=0
and b=1 terms, the signed remainder sum_(b=2)^5 C_b E_b, with

    C_2=11*(c^3-3*c^2-12*c-6),
    C_3=-165*c-110, C_4=-165, C_5=132.

Here E_b counts ACTUAL independent ordered b-tuples inside the core.
The two negative coefficients make a termwise nonnegativity claim false.
However E_3<=t*E_2 and E_4<=t^2*E_2, even for rank-deficient inside
sets. Therefore the signed remainder is at least

    [C_2-(165*c+110)*t-165*t^2]*E_2+132*E_5
    >=11*(c^3-33*c^2-22*c-6)*E_2+132*E_5>=0.

For c>=34, c^2*(c-33)>=c^2>22*c+6. Thus c>=100 suffices.
All other steps of the existing disjoint inside-cardinality count apply.
This proves the same lower basis function without assuming full inside rank.

## Positive Log-Concavity

Put R(t)=prod_(i=0)^4(c+i-t). On [0,c], R''>=0 and R'''<=0.
Thus g_5''>=0, g_5'''<=0, and

    g_5'(0)/A_4 >=11-5*(1+4/c)>=29/5,
    g_5(0)*g_5''(0)/A_4^2 <=20*(1+4/c)^2<=20*(26/25)^2.

The square of 29/5 exceeds the last bound. Consequently
g_5*g_5''-(g_5')^2 is negative at zero, and its derivative
g_5*g_5'''-g_5'*g_5'' is nonpositive throughout [0,c]. Positivity
and increasingness follow from g_5(0)>0 and g_5'(0)>0. Hence g_5
is positive log-concave on [0,c]. Multiplication by the positive affine
factors in P(M-t) preserves this property. The endpoint conclusion follows.

No claim is made for j>=6 or j=5,a>c. This supplements the actual coupled
identity; it is not an extrapolation from the four earlier coefficient rows.

## Boundary Of This Linear-Tangent Argument

At j=6 the same exact coupling coefficients are

    C_2=-110*c^3-550*c^2-770*c-264,
    C_3=-55*c^3-495*c^2-880*c-330,
    C_4=-165*c^2-660*c-330,
    C_5=-198*c-330, C_6=0.

For every c>=1, the first four are strictly negative. Thus once E_2>0,
the remaining signed sum is negative, not something that the rank-five
absorption argument can make nonnegative. This is an obstruction to that
specific proof step, NOT a counterexample to the proposed basis count or
the MCA bound: the discarded convex remainders can carry additional mass.
Any higher-rank extension must retain those remainders, keep and price the
negative terms, or use a different inside-tuple lower bound.
