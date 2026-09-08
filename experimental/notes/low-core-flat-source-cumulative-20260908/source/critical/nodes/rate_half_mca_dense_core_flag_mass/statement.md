# Over-Budget KoalaBear Sources Force Many Actual Dense-Core Flags

Status: PROVED by the hand argument and exact arithmetic; independent review due.

Use the normalized KoalaBear source with R=1048576, d=67472,
(n,K,m)=(R+J,J,d+J), 23000<=J<=29999, actual carrier dimension eleven,
distinct original finite labels, full-code-bad size-m supports and empty
universal carrier core. There is NO flat-density hypothesis here.

For each label fix a minimizing pair and its untruncated raw margin. For
each raw<=6 record, choose one M=J+67466 point subset of its full joint
core, retaining the original pair. Call the label exceptional if this
chosen core has nested complete flats F<G of ranks t-1,t, 1<=t<=9,
whose coordinate sizes a,b satisfy

    (11-t)*b-(10-t)*a > M.                              (FLAG)

Let e be the number of distinct exceptional labels, counted ONCE each.
Define P(J)=product_(i=0)^10(67466+J-i*(J-1)/10),
U(J)=(1048576+J)_falling_12, P_d=product_(i=1)^10(67472+i), and

    G(J)=134944+floor(max(U(J)/(12*P(J)),
                    125*U(J)/((67472+J)*P_d*10488))).

G is a good-record comparison, NOT an unconditional MCA upper bound.
If |Gamma|+134944>B*=274980728111395087, then

    e >= floor(8*(B*-G(J))/7)+1
      >= 6933965264351691.                              (MASS)

At J=25000,28000,29999 the respective lower bounds are
38626081114513530, 79264171528992278 and 102451841872190189.
This holds for EVERY fixed choice of the original minimizing pairs and
M-point cores, not for a favorable reselected family.

Every exceptional flag actually has 1<=t<=7 and

    b >= floor((J+67466+(10-t)*(t-1))/(11-t))+1,
    b <= J-11+t.

For t=7 the annihilator of the corresponding complete nonzero SOURCE
flat has actual dimension four and degree at most 5628 after locator
division. This is an auxiliary polynomial-space fact, not free transport
of all original labels to a received-word child.

The existing original-source assembly transports MASS to an over-budget
rank-twelve original line in this J interval. No upper bound on e is
proved, no whole degree interval closes, and higher ranks and both prizes
remain open. Different flags of one label are never separately counted.
