# Core-completed child bases pay 85000 more shortened dimensions

Status: PROVED. Retain this node's original KoalaBear row and exact
rank-twelve hypothesis. Set R=1048576, d=67472, B=274980728111395087.
In addition to the old g<=793576 payment, the whole interval

    793577<=g<=878576, equivalently 170000<=J=K-g<=254999,

is paid, with original near-inclusive total at most

    270992495272115150, reserve 3988232839279937.        (PAY)

No raw-margin, row-space, subfield-source or polynomial-relation
hypothesis is imposed. Both zero and cyclic cases are covered here.

## 1. A degree-aware cap for every second child

For 1<=s<=9 and L>=s, put

    A_s(j)=(R+j)_falling_(s+1)
                /((d+j)*product_(i=1)^(s-1)(d+i)),
    Q_s(L)=floor((d+s)/((s+1)*d) * max(A_s(s),A_s(L))),
    U_9(L)=max_(s=1)^9 Q_s(L), for L>=9.

The new basis-completion supplier applies, since d>=s(s+1). For any
actual degree bound k in [s,L], the resource's second endpoint is
A_s(s); its first is A_s(k). A_s(k) is convex on k>=s: with y=d+k,
the numerator is product_(i=0)^s(y+R-d-i), whose coefficients are
positive. After division by y it is a positive polynomial plus a
positive multiple of 1/y. Each term has nonnegative second derivative.
Thus its maximum on [s,L] is at an endpoint, proving Q_s(L).
Taking the maximum over ACTUAL dimensions covers all 1..9; dimension
zero has the existing cap R-d+1, smaller than U_9(L).

U_9(L) is nondecreasing because each max(A_s(s),A_s(L)) is the
maximum over the growing interval [s,L]. This monotonicity does not
assume that the unmaximized A_s itself is increasing.

## 2. Transport the actual child degree, not an independent maximum

Use this node's existing common-zero normalization: z common carrier
zeros, g universal zeros, e=z-g, tau<=e exceptional slopes. The
zero-free parent has K'=K-z=J-e<=J, and excess d'=d+e>=d.
Its second selected-support children have degree bound K'-2<=J-2,
actual explanation dimension <=9, and the same R. They remain
full-code-bad. If needed, exchange inside their complete bad support
to obtain the baseline excess d, preserving the chosen explanation
and badness. No old margin is transported through that exchange.
Therefore U_9(J-2), in the SAME field, bounds every such second child.

The existing two-anchor theorem and its joint normalization comparison
give, with s_parent=11,

    |Gamma|<=tau+floor(U_9(J-2)*max(F_bal(J),F_spike(J))),
    F_bal(J)=(R+J)*(2R+J+9)/((d+J)*(2d+J+9)),
    F_spike(J)=(R+10)/(d+10)
                 +(R+10)*(R-d)/((d+J)*(d+J-1)).

Both F branches decrease with J. The original near charge is 134944;
use tau<=R as before. No new near removal or child exceptional charge.

## 3. A short covering certificate

Cover J=170000..254999 by the 85 consecutive intervals
[a,b]=[170000+1000i,170999+1000i], i=0..84. On each interval,

    total<=R+2d+floor(U_9(b-2)*max(F_bal(a),F_spike(a))).

All 85 rational bounds are <= (PAY); the largest is at [170000,170999].
The primary product replay and independent binomial/integer replay check
every interval, every actual child dimension, coverage and the final
near/exception charge. No millions-point field computation is required.

## 4. New residual and nonclaims

Combining (PAY), the old J>=255000 payment, and the unchanged all-rank
J<=4800 payment, every unpaid rank-twelve source now has

    4801<=J<=169999,
    878577<=g<=1043775.

The previous zero/cyclic classification, union lower bounds and
bounded-remainder payments still apply on this smaller interval.
Higher error ranks, all-source safety of the original row, the unrestricted
threshold bracket and both prize problems remain open. The number 170000
is a convenient certified endpoint, not asserted sharp or optimized.
