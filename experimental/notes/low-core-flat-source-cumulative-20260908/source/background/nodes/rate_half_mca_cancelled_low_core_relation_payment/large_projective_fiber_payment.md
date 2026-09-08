# Whole sources with a large projective fiber are paid

Status: PROVED on the unchanged normalized KoalaBear source contract.
Keep actual carrier dimension eleven, empty universal carrier core,
original field and distinct original finite slope labels. If

    65000<=J<=169999

and one projective evaluation fiber has a>=ceil(J/2) nonzero ORIGINAL
coordinates, then the ENTIRE source satisfies

    N=|Gamma|+134944<=274929007493481160,
    reserve>=51720617913927.                         (LARGE-FIBER)

There is no pair-curve cover, receiver descent, field-drop premise or
unpriced exception set. Neither this fiber condition nor its complement
is claimed automatically for an arbitrary carrier.

## 1. Couple LOW and HIGH on the same tuple budget

Put R=1048576, d=67472, T=6, D=d-T=67466, M=J+D, and

    U(J)=(R+J)_falling_12,
    P=prod_(i=1)^9(D+i).

The new fiber supplier gives at least 12*b(M) independent tuples on
every raw<=6 record. Its actual minimizing core has at least M points;
restricting to M for the lower count discards no source labels or defects.

For all raw>=7 the prior completed-basis weight satisfies

    w>=L=10488/125.

For completeness, b(7) is at least 84*(1-77/67473)>10488/125,
by the eleven-factor product inequality. The formula increases on
7<=raw<=84 because 12*84<67473; for larger raw the old truncated
weight is >=84. This includes raw>d. The original completed resource
obeys F(J)<=C=23067643444721720934 on the whole normalized interval,
as previously proved by convexity and endpoint ceilings.

The source count therefore satisfies

    N<=max(floor(U(J)/(12*b(M))), floor(C/L))+134944.  (1)

LOW and HIGH are not separately maximized and added. Their counts use
one common independent-tuple budget. The second term plus near is

    floor(125*C/10488)+134944=274929007493481160.      (2)

## 2. Four explicit lower envelopes for all fiber sizes

The polynomial root-space bound gives J/2<=a<=J-10. The supplier has
e=J-a-10. Its t=0, t=a and possible t=D+1 endpoints give b(M).
Uniformly over this entire interval of a, b(M) is at least the minimum
of the following FOUR positive quantities:

    B0=(J+D)*(D+1)*(D+J/2+1)^9,
    B1=P*(D+J/2)*(D+1+5J),
    B2=11*(J-10)*(D+10)*P,
    B3=11*(D+1)*(J-1)*P.                             (3)

For t=0 the exact product increases with a; each of its nine product
factors is >=D+J/2+1, proving B0. At t=a, the exact expression is

    P*(J+D-a)*max(11a,D+1+10a).

On each side of a=D+1 this is a concave quadratic, so its minimum
occurs at J/2, J-10, or that breakpoint when present. At J/2 keep
the second member of the maximum to obtain B1; at J-10 keep the
first to obtain B2. The breakpoint gives B3.

For the supplier's third endpoint t=D+1, which exists only for a>=D+1,
the exact expression is

    11*(D+1)*(J-1)*prod_(i=0)^8(a+i)>=B3.

This accounts for both possible breakpoints, even when they are outside
the relevant interval. Including an extra positive lower-envelope term
can weaken the result but never strengthen it incorrectly.

## 3. Prove the whole J interval, not just endpoint tests

For i=0..3 let Q_i(J)=U(J)/(12*B_i(J)). Q0 decreases on the interval:
the positive numerator logarithmic derivative is at most 12/L0, where
L0=R+65000-11; the nine powered denominator terms alone have derivative
at least 9/(2D+169999+2)>12/L0. All other denominator terms help.

Q1, Q2 and Q3 are log-convex, hence convex. Their logarithmic second
derivative includes at least one positive denominator term bounded below
by 1/H0^2, where H0=169999+2D. All twelve negative numerator terms
together have magnitude at most 12/L0^2, and

    L0^2>12*H0^2.

For Q1 use its denominator factor J+2D (the other factor helps).
For Q2 and Q3 use J-10 and J-1 respectively, both <=H0. Therefore
each of Q1..Q3 is bounded above by its larger endpoint value.

Exact floors, including the one original near charge, are:

    J       Q0+near             Q1+near
    65000   34003655554524123    266514954058742090
    169999   1252453225033902    220398387206020840

    J       Q2+near             Q3+near
    65000   216764665972142342   216763564029644353
    169999  244346006891976872   244365664452173214.

Each entry means floor(Q_i)+near. Thus the LOW quotient in (1), plus
near, is at most 266514954058742090. This is below (2), proving
(LARGE-FIBER) for all J and all a in the printed ranges.

## 4. What this removes from the residual

Any unpaid normalized source on 65000..169999 has EVERY projective
evaluation fiber of size at most ceil(J/2)-1. This now excludes large
one-dimensional concentration without assuming it resembles a full
progression carrier. Indeed such a large fiber violates the earlier
bounded-flat hypothesis a<=floor((J-1)/10); the new theorem treats the
opposite concentration regime using its annihilator instead.

This carrier class is nonempty on the actual field and domain. For any
J-10 distinct domain points let G be their locator and take
V=span{1,G,XG,...,X^9G}. This has dimension eleven, degree <J and
one projective fiber of size exactly J-10. Its other source hypotheses
still concern the actual receiver and labels; the example is not an
unsafe source or an assertion that every receiver saturates the bound.

The earlier bounded-flat proof now explicitly allows real h, since all
positive greedy-choice lower bounds may be real. Taking h=(J-1)/10
leaves a heavy flat in some dimension 1<=j<=9, with at least
floor(j*(J-1)/10)+1 nonzero evaluations. Dimension ten is automatic
by the root bound J-1. With the former integer floor on h this last
conclusion would not have followed; the proved weakening removes that
rounding artifact. The no-dimension-ten rational-multiplier restriction
also remains. Higher-dimensional concentration is still unpriced.

General every-carrier coverage remains 4801..9940. No smaller-fiber or
higher-dimensional concentration payment, exhaustive original transport,
higher-rank theorem, LIST bound, unrestricted endpoint or prize closes.
