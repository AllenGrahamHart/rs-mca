# Proof: Exhaustive Flat Splitting With Heavy-Record Tuple Credit

Set L0=45000, H=52999, R=1048576, d=67472, T=6,
D=d-T=67466, M=J+D, c=D+1=67467, near=134944,
P_d=prod_(i=1)^10(d+i), and U_0(J)=(R+J)_falling_12.
All sources and selected finite labels are those of statement.md.

## 1. Every Record Already Pays Half The HIGH Charge

The required completed-basis suppliers give weight >=w=10488/125
for raw>=7, including margins above d. Put beta_max=m*P_d*w.

For raw<=6 the required quadratic contraction certificate gives at least
12*P_11*q(J) tuples, where P_11=prod_(i=1)^10(D+i) and
q(J)=A+B*J+C*J^2 is the exact rank-eleven quadratic in that supplier's
proof section 1. Its universal basis scope is 11<=J<=65000, not just
the narrower range where it alone paid the full numerator.

The exact eight-step certificate also gives

    B*d>=A, C>=0,
    24*P_11*q(L0)>=(d+L0)*P_d*w.

Indeed the derivative numerator for q(J)/(d+J) is
B*d-A+2*C*d*J+C*J^2>=0. Thus throughout [L0,H], EVERY LOW
record pays at least beta_max/2. HIGH records pay beta_max. This proves
the generic shared-budget input eta=1/2 for EVERY original record.

The resource C(J)=U_0(J)/[(d+J)P_d] is convex: with y=d+J it
expands as a positive polynomial plus a positive constant/y. Its endpoint
ceilings give

    C(J)<=C_0=13541615650357694642.                 (RESOURCE)

## 2. The Low-Density Branch

Choose a proper maximum-density flat of the actual nonzero evaluations,
of rank j and size a=j*h. Put h_r(J)=1+(J-11)/r.
If h<=h_6=(J-5)/6, the hybrid degree/density count gives at least

    B_low=(J+D)*prod_(i=1)^5(J+D-i*h_6)
                     *prod_(i=6)^10(D+11-i)

ordered bases in every M-point core subset. The six nonconstant factors
have positive slopes summing to 7/2 and values at most D+H. Since
(7/2)/(D+H)>12/(R+L0-11), U_0/(12*B_low) decreases throughout
the whole interval. The exact floor at L0, including near, is

    272429083415036159.                            (LOW-DENSITY)

HIGH uses the SAME resource and is bounded by C_0/w+near, which is
smaller. This pays the complete low-density source, not a separate owner.

## 3. All Other Maximizing Flats Have Rank At Most Five

If h>h_6, the root-space bound a<=J-11+j gives h<=h_j.
For j>=6, h_j<=h_6, a contradiction. Therefore

    1<=j<=5, j*h_6<a<=j*h_j=J-11+j.               (RANK-SPLIT)

In particular a<c. The required maximum-density basis theorem applies
for j<=4, and its proved rank-five supplement applies for j=5, c>=100.
That supplement absorbs two negative coupling coefficients using actual
inside-tuple inequalities; it does not assume all five coefficients positive.

Put l=11-j, e=J-a-l, h=a/j, and define

    P(X)=X*prod_(i=1)^(l-1)(X-min(e+i,i*h)),
    A_k=prod_(i=0)^(k-1)(c+i),
    g_j(z)=prod_(i=0)^(j-1)(c+i-z)+11*A_(j-1)*z,
    F(z)=P(M-z)*g_j(z), 0<=z<=a<c.

The coupled theorem gives this lower count at the actual inside-core
occupancy z. It is positive log-concave, so a light occupancy cap b
gives beta(b)=min(12*F(0),12*F(b),beta_max).

## 4. Projected Pairs And Their Full Child Bounds

Maximum density gives projected-pair distance Delta=a/j. The required
receiver-flat theorem isolates at most one heavy projected pair with
core size t>a-Delta/2. All light pair cores have occupancy at most
b(t)=2a-Delta-t. Its retained heavy child has EMPTY UNIVERSAL CORE,
degree J-a and actual agreement m-t. The anchored dimension is at most
10-j; the proved padded scalar-descent caps at baseline gap d are

    j        U_j
    1        10755802499540570
    2        737012707696078
    3        50371450079970
    4        3424826154478
    5        231038329409.

They are full selected-family caps with no post-near hypothesis. The
larger actual anchor gap d+a-t can be reduced by exact bad-subset
selection. The heavy cap is (n-a)*U_j/(m-t)+(a-t), with all exceptions
explicitly paid. Since all records consume at least half beta_max,
the shared-budget theorem gives

    |Gamma|+near <= max(U_0/(12*F(0)),U_0/(12*F(b(t))),C_0/w)
                    +(n-a)*U_j/[2*(m-t)]+H/2+near.  (PAID)

Here a-t<=H is only a harmless upper bound on the exception charge.
The half coefficient is proved by tuple consumption, not a budget fit.
No heavy group is also covered by the relaxed endpoint t=a-Delta/2.

## 5. A Complete Finite Router, Not A Grid Extrapolation

For fixed J,a the right side of (PAID) is convex in t on
[a-Delta/2,a]: 1/(m-t) is convex, while reciprocal positive
log-concave basis functions are convex, and maxima preserve convexity.
Therefore use t=kappa*a, with kappa in {1-1/(2j),1}. The light cap
is lambda*a, lambda=2-1/j-kappa. Include z=0 as the other light case.

For fixed J and each endpoint, (n-a)/(m-kappa*a) is convex in a:
its derivative has sign kappa*n-m>0, since n>2m and kappa>=1/2.
In P, profile switches are precisely a=j*h_r(J), r=j,...,6.
Between switches all factors are positive affine in a, and g_j(lambda*a)
is positive log-concave. Each LOW quotient plus half the child cap is
therefore convex in a. The HIGH quotient is constant in a before that
convex child term is added. It suffices to check the listed breakpoints.

Now fix a=j*h_r(J)=alpha*J+beta, alpha=j/r, beta=j*(1-11/r).
All P factors are positive affine in J with fixed density/degree branch.
Also g_j(lambda*a) is positive log-concave. Thus log F is concave
along the profile. The exact certificates verify for EVERY one of the
80 indexed profiles (j,r,kappa,z-choice) that

    (log F)'(H)>12/(R+L0-11)>=(log U_0)'(J).

This proves each LOW quotient decreases on the entire J interval.
The child ratio decreases too: its derivative numerator is

    (1-alpha)*d-(1-kappa*alpha)*R+beta*(1-kappa)<=0,

because R>d, beta<=0 and 0<alpha<=1. Constants H/2 and near do
not vary with J. Therefore all LOW-profile maxima occur at J=L0.
Real a,t,J breakpoints are only relaxations of actual integer sources.

For the HIGH part, each child ratio is at most
(R+11-j)*U_j/(d+11-j). The five exact comparisons show the largest
is Q_max=(R+10)*U_1/(d+10). Thus its uniform endpoint total is
floor(C_0/w+Q_max/2+H/2+near). No separate HIGH maxima are summed.

## 6. Exact Totals And Scope

The 80 LOW-profile totals have maximum floor 259673779829962642,
at j=1,r=4,kappa=lambda=1/2. The uniform HIGH total is
244960029415389035. Both are below (LOW-DENSITY). These three
WHOLE-source alternatives combine by maximum, proving (NEW).

The prior contraction/high interval already pays 53000..169999 by
274929007493481160. Its maximum with (NEW) proves (UNION), adding
all 8000 values 45000..52999. The original-source assembly retains its
field, labels, complete-core transport and single near add-back downstream.
No source-rank bound, owner atom, unrestricted endpoint or Prize closure
is inferred from this normalized interval theorem.
