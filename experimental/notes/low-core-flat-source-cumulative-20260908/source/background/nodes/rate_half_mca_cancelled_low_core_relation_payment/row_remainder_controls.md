# Exact cyclic control for the new remainder band

Use E=F_13 and F=E(beta), beta^6=2, as in the preceding saturation
controls. Take D={+/-1,+/-2,+/-3,+/-4}, k=1,m=4,T=2,ell=1,A=2.
On the pair of points +/-j give the receiver the constant value

    (u_j,v_j)=(j^2,v_j),
    (v_1,v_2,v_3,v_4)=(0,beta,beta^2,beta^3).

There are six different secant slopes between the four received values.
Their denominators, as E-polynomials in beta, have distinct monomial
supports, and their numerators are nonzero E-scalars, so the degree-six
minimal polynomial implies they are distinct. A support comprising the
two point-pairs of a secant has size four and a constant scalar explanation.
It is not contained in the degree-<1 pair code: its two received values
are different. The owner second polynomial has raw exactly two, since
the two different second values each occur twice.

Choose owners so that each of the four complete two-point cores is
represented. Then U=D. The nonzero row R=(1,0) has unique remainder
Q=X^2, degree A=2, rather than degree <A. The core-ceiling lemma forces
raw>=m-deg Q=2 and attains equality. The carrier is the actual one-
dimensional constant polynomial space. Its margin resource is 14, so
the six selected labels obey 6<=floor(14/2)=7.

## Full row space is cyclic, not a former relation case

Write a row as (a+bX,c+dX), with offset q_0+q_1 X. Taking even and
odd parts on each +/-j pair shows that admissibility is equivalent to

    a*u_j+c*v_j-q_0 in E,
    b*u_j+d*v_j-q_1 in E, for all j.

Subtract the j=1 equations. For (a,c), the three constraints are

    3a+beta*c in E,
    8a+beta^2*c in E,
    2a+beta^3*c in E.

Eliminating a gives c*(3beta^2-8beta) in E and
c*(3beta^3-2beta) in E. If c!=0, their ratio would be in E,
giving a nonzero degree-three equation for beta, impossible. Hence c=0
and a in E. Similarly d=0 and b in E, then q_0,q_1 in E.
Conversely every such row is admissible. The FULL old-threshold E-row
space is therefore E[X]_(<=1)*(1,0), the hard cyclic case.

A polynomial relation with remainder of degree <2 would belong to this
space. It would make (a+bX)X^2 a polynomial of degree <2 on eight
points. Since the difference has degree at most three, it vanishes
identically, forcing a=b=0. Thus the old nonzero relation test fails,
whereas the new bounded-remainder test applies.

These are actual small MCA witnesses, not deployed prize parameters.
They demonstrate strictness of the theorem's scope without asserting
that every cyclic source has low-degree residual.
