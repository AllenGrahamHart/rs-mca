# A Stronger Basis Budget At Core Cutoff500

Use the required generic contraction theorem through
mca_raw_margin_basis_mass. Put d=67472,D=d-500=66972,E=10000,X=5000,
P_r=product_(i=1)^(r-1)(D+i), and c=1/[2(D+2)].
For every nonzero rank-r polynomial evaluation space of degree<K on
D+K points, r<=K<=E, prove the ordered-basis bound

    B_r>=P_r*q_r(K), q_r(K)=a_r+b_r*K+c*K^2.

At rank3 the required seed gives a_3=D(2D+1)c,b_3=(3D+1)c.
For r=4,...,11, write a,b for the previous coefficients and set

    H=D+r-1, alpha=(r-2)/(r-1), delta=1/(r-1),
    f=q_(r-1)(r-1),
    s1=b-2c+f/H, s0=a-b+c-(r-1)f/H,
    U(K)=(D+K)*q_(r-1)(alpha*K+delta)/H
         =u0+u1*K+u2*K^2+u3*K^3,
    u3=c*alpha^2/H,
    u2=(b*alpha+2c*alpha*delta+D*c*alpha^2)/H,
    u1=(a+b*delta+c*delta^2+D*(b*alpha+2c*alpha*delta))/H,
    u0=D*(a+b*delta+c*delta^2)/H,
    t1=u1+2(u2-c)X+3u3*X^2,
    t0=u0-(u2-c)X^2-2u3*X^3,
    eta=max(0,t0+t1*r-s0-s1*r,t0+t1*E-s0-s1*E),
    a_r=t0-eta, b_r=t1.                              (REC)

These are fixed rational definitions, not fitted or rounded coefficients.
For each of the eight steps, exact arithmetic gives b>=D*c, u2>=c,
u3>=0, and all next coefficients positive with b_r>=D*c. The normalized
spike branch S(K)=s0+s1*K+c*K^2 exceeds q_r at both r and E;
their difference is affine. The other branch has the EXACT identity

    U(K)-q_r(K)=eta+(K-X)^2*((u2-c)+u3*(K+2X))>=0.    (SQ)

Thus the required universal contraction step proves B_r at every rank
on the whole interval. Both independent implementations reconstruct(REC)
and the second checks(SQ) as a polynomial identity. Those finite
certificates establish the explicit rational gates; the contraction
theorem, not a source scan, establishes their universal applicability.

## All Defects Use One Resource

Put P=P_11,q=q_11, beta(J)=12*P*q(J), and
P_d=product_(i=1)^10(d+i). Each raw<=500 record has a nonzero
rank-eleven joint-core subset of size m-500=D+J. The generic raw-mass
theorem counts ALL its defects, giving raw*beta independent tuples.
For raw>=501 the required completed-weight supplier proves at least
5500*m*P_d independent tuples, on the SAME incidence resource.

The exact all-HIGH gate is

    5500*(d+J)*P_d >=51*beta(J).                     (HIGH)

Indeed q(J)/(d+J) increases because
(d+J)q'(J)-q(J)=d*b-a+2*d*c*J+c*J^2>0, with d*b>=a.
Checking(HIGH) at the larger endpoint E=10000 therefore proves it
throughout the actual interval. Use the generic theorem's separately
funded high-record variant with T_core=500,kappa=51. The baseline
501*m*P_d does NOT fund this application; it is not substituted for5500.
The record ranges1..500 and501..m exhaust every possible raw margin.

Consequently sum min(raw,51)<=floor Q(J), where

    Q(J)=(1048576+J)_falling_12/[12*P*q(J)].

Writing L=9941, the exact certificate gives

    (b+2cL)*(1048576+L-11)>12*q(E).

Throughout[L,E], q'/q >=(b+2cL)/q(E), whereas the falling numerator's
logarithmic derivative is at most12/(1048576+L-11). Hence Q strictly
decreases on the entire real interval. Exact division gives

    floor Q(9941)=646273487661620022=W.               (MASS51)

## Two Valid Accounting Forms

For S_t=sum_(raw<=t)raw on the SAME selected source, telescoping gives

    |Gamma|<=W/51+sum_(t=1)^50 S_t/[t(t+1)].         (CUM)

For a fixed raw r<=50 its coefficient in the sum is1-r/51;
for r>=51 it is zero. Thus this is exactly the truncated-raw identity.
For any represented pair f with complete core H_f, its selected defects
across assigned slopes occupy disjoint points outside H_f. For its raw<=t
owners, |H_f|>=m-t, so their TOTAL raw is at most n-|H_f|<=981104+t.
Therefore S_t<=(981104+t)M_t, with M_t the full represented pair count
at depth t. This is not an uncharged projection from pairs to slopes.

If M bounds every raw<=50 pair, the simpler relaxation is

    |Gamma|+134944<=12672029169970630+981154*M.       (DIRECT)

Here the first term is W//51+134944. It drops the nonnegative LOW
resource contribution and pays all LOW labels at full per-pair cost.
These two forms are alternatives on one source, not independent budgets
to add. The separate coupled-line argument in proof.md uses its own
valid accounting identity and does not add(DIRECT)'s base.
