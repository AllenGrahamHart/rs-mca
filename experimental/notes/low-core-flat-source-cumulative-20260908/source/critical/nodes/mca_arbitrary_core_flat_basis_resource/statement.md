# Count Bases Through An Arbitrary Complete Core Flat

Status: PROVED. No maximum-density-flat hypothesis.

Let V have actual dimension s and degree <K on a set H of M>K distinct
nonzero evaluations. For every proper rank-r flat suppose its coordinate
count on H is <=c_r. Put u_r=min(c_r,K-s+r).
Choose ANY complete H-flat G of rank t, with b coordinates B=H intersect G,
1<=t<s and b<M-K+1. Write ell=s-t.

The annihilator of G divided by P_B has actual dimension ell, degree
<K-b and M-b nonzero evaluations. A proper rank-i quotient flat has
at most u_(t+i)-b coordinates. Thus its ordered basis count is at least

    Q_greedy=(M-b)*product_(i=1)^(ell-1)(M-u_(t+i)).

Any other PROVED lower quotient-basis count Q may replace Q_greedy.
Set d_i=M-u_(s-1-i), R_k(y)=product_(i=0)^(k-1)(d_i-y).
If E_i counts ordered independent i-tuples inside B, y_T counts B points
outside the span of T, then

    B_s(V,H)>=Q*sum_(i=0)^t binom(s,i)*sum_T R_(t-i)(y_T),
    max(b-c_i,0)*E_i<=E_(i+1)<=(b-i)*E_i.                 (COUNT)

The signed tangent and BOX formulas of the required density-completion
supplier hold with these d_i and c_i in place of i*h. In particular use
lower ratios max(b0-c_i^upper,0), upper ratios max(b1-i,0), and final E_1
endpoint according to the coefficient sign. The b=0 class is always positive.

If a proper-flat density bound h holds on H and b<=t*h, the quotient has
proper-flat density at most min(K-b-ell+1,(t+1)*h-b). A verified hereditary
balanced-product gate for this quotient therefore supplies another Q.
All division is auxiliary polynomial counting, not received-word descent.
