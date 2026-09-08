# Density-Aware Flat Completion And Coupled Tuple Ratios

Let V have actual dimension s and degree <K on a fixed domain of distinct
field points. Let F be a proper maximum-density flat of its nonzero
evaluations, of rank j, with complete point set A of size a and density
h=a/j. Thus 1<=j<s, and every proper i-flat contains at most i*h points.
Let H be an M-point nonzero-evaluation core, with t=|H intersect A|,
and assume a<c=M-K+1. Put ell=s-j and W=ann(F)/P_A.

Let Q_out be ANY proved lower bound for the number of ordered bases of
W on H outside A. The quotient has actual rank ell, degree <K-a,
M-t nonzero evaluations and gap c-1+a-t. Define

    d_i=max(c+i, M-(s-1-i)*h),  i=0,...,j-1,
    R_k(y)=prod_(i=0)^(k-1)(d_i-y), R_0=1.

If E_b counts ordered independent b-tuples in H intersect A, and y_B
counts inside points outside the span of one such tuple B, then

    B_s(V,H) >= Q_out * sum_(b=0)^j binom(s,b) sum_B R_(j-b)(y_B). (COUNT)

In particular d_i>=c+i improves the root-only completion; neither the
greedy quotient lower bound nor the root-only final factors are compulsory.

## Signed Counts With Coupled Ratios

Choose any real 0<=q_b<c for b=1,...,j. Put

    L_k(q)=R_k(q)-q*R_k'(q), D_k(q)=-R_k'(q),
    C_b=binom(s,b)L_(j-b)(q_b)
          -binom(s,b-1)D_(j-b+1)(q_(b-1)) for b>=2,
    C_1=s*L_(j-1)(q_1).

The bracket in COUNT is at least R_j(t)+sum C_b E_b. Define backwards

    T_j=C_j,
    T_b=C_b+T_(b+1)*max(t-b*h,0) if T_(b+1)>=0,
        C_b+T_(b+1)*max(t-b,0) otherwise.

It is therefore at least R_j(t)+t*T_1. This follows from ACTUAL tuple
ratios, not independent optimization of the signs of all E_b.

For a box t0<=t<=t1<c, h<=h1 and d_i>=d_i^0>=c+i, form R,L,D,C
using d_i^0 and any fixed calibrations q_b<c. Replace the two backward
ratios by max(t0-b*h1,0), max(t1-b,0). The final lower bound is

    prod_i(d_i^0-t1)+T_1*(t0 if T_1>=0 else t1).     (BOX)

The b=0 term alone is positive. Another valid lower count is the sum
over b of binom(s,b)*prod_(i=0)^(b-1)max(t-i*h,0)
times R_(j-b)(t-b).
A consumer may take the maximum of valid lower bounds and must establish
positivity before multiplying by a lower Q_out.

In the dimension-eleven MCA interface, the existing complete-core packing
and defect insertion give twelve incidence tuples per counted basis,
without reselecting the witness or changing its minimizing pair or label.
No receiver descent, additional near allowance or finite interval follows
from this generic count alone.
