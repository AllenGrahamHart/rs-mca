# Original-coordinate list recovery and finite payment

Use `curve_descent.md` and `maximal_parameter_family.md`. The only
required node is the weighted cubic supplier; its own dependencies supply
the completed-HIGH resource and generic incidence prerequisites.
The present proof does not require its finite consumer in reverse.

## 1. Projective fibers have at most two or three parameter values

Use the polynomial model (P3). At a finite T=t, the scalar output
`t*Phi(t,z)+Psi(t,z)` has quadratic coefficient Delta(t)=t*p(t)+b(t).
If Delta(t)!=0, a prescribed received pair therefore allows at most two
values of z. If Delta(t)=0, the first output still has cubic coefficient
c!=0, giving at most three values. This counts distinct roots only.

At T=infinity, the input is z=eta_3, the leading coefficient of the
degree-three parameter section. Degree-ten homogenization of the output
pair gives exactly

    Phi_infinity(z)=p_4*z^2+u_7*z+v_10,
    Psi_infinity(z)=-c*z^3+b_4*z^2+w_7*z+j_10.                   (6)

The cubic vector is never zero. At p_4!=0 the first output gives a
two-element list, otherwise the second gives at most three. The degree-five
homogenization of Delta has value p_4 at infinity. Hence at most five
projective T-values need list size three; all others need at most two.
There is no assumption of good reduction at every finite fiber.

## 2. Build lists at original X-coordinates

Return to the original pair `a=h_*+q*B^10*P(A/B)`,
`b=q*B^10*Q(A/B)`, interpreted homogeneously. On the complete joint-core
union U, q is nonzero: q(x)=0 makes V(x)=0, so any agreeing pair there
would make u(x)=h_*(x),v(x)=0, contrary to empty universal carrier core.
For any coordinate with q=0 set its allowed parameter list empty. Such a
coordinate is in no pair core; it is NOT removed from the domain or from
original scalar-defect accounting.

For q!=0,B!=0, subtract the original h_* value from u and divide both
received coordinates by q*B^10. Give this X-coordinate the list of z
mapping to that normalized pair at t=A/B. For q!=0,B=0, coprimality
gives A!=0. Divide by q*A^10 instead and use (6). These lists may differ
between coordinates having the same t: no receiver descent is imposed.

The rational map A/B has degree h, so each projective fiber has at most
h distinct original coordinates (the equation is A-tB=0 or B=0).
At most 5h coordinates therefore need a three-element list. The number
of coordinate/value slots is at most S=2n+5h. A LOW pair supplies at
least m-500 joint agreements and hence that many accepted slots.

Two distinct parameter sections of degree <=3 agree at at most three
projective T-values, since their nonzero homogeneous cubic difference has
at most three roots. Their pullbacks thus agree at at most 3h original
coordinates. Agreement at infinity here means equality of eta_3 values;
the degree-three homogenization retains that possibility.

## 3. Variable-list Johnson count

Let M be the number of represented nonsingular pairs. Their parameters
are unique. Choose exactly a accepted coordinates for each, with a no
greater than its actual agreement. The original F-pair set is finite;
alternatively a>3h and the finite lists already ensure finiteness.
Let n_(x,z) be the incidence count at each permitted slot. Then

    sum n_(x,z)=M*a,
    sum n_(x,z)^2<=M*a+M*(M-1)*c_col, c_col=3h.

Cauchy--Schwarz, with S available slots, gives

    M^2*a^2<=S*(M*a+M*(M-1)*c_col).

For M>0 and a^2>S*c_col rearrange to (LR). M=0 is trivial.
Larger S and c_col preserve the pre-rearranged upper bound, as does
choosing a smaller common number of accepted coordinates. This justifies
the uniform interval budgets below without an unproved monotonicity step.

## 4. Two interval budgets pay the maximal-dimensional d=10 family

The carrier bound gives 10h<=J-1. Choose these conservative budgets:

    J interval    h_max   n_max    a_min   S_max    c_max  pair cap
    7117..7999      799   1056575   74089   2117145   2397       366
    8000..8655      865   1057231   74972   2118787   2595      1251

For the first row, the Johnson denominator is 414383356 and numerator
151782359340. For the second they are 122548519 and 153351446699.
Both denominators are positive and the exact floors are 366 and 1251.
This covers every integer J in the lower strip; the split is important
because mixing the full interval's smallest agreement and largest height
in one budget makes the denominator negative.

There are at most 1251 nonsingular on-cubic pairs. Add one possible
singular pair and the existing at most 64 off-curve pairs, for 1316
LOW pairs in total. Each pair carries at most n-m+500=981604 distinct
original finite labels: its nonempty scalar-defect sets outside its
complete joint core are disjoint across labels. At an outside coordinate
`(u-a)+gamma*(v-b)=0` has at most one finite solution gamma.

The required completed-HIGH theorem bounds all HIGH labels by C/5500,
C=23067643444721720934, on 4801..169999. Adding the original near
allowance once gives

    N <= C//5500+134944+981604*1316
      = 4194118281875211 < B=274980728111395087.                 (7)

No other LOW class is relabelled HIGH. One resource and one near charge
are used; the off-curve and singular pairs have been explicitly charged.

## 5. Smaller coefficient dimensions and full-kernel use

If d=10 but coefficient dimension <=3, the required weighted theorem
with h<=865 gives pair cap

    floor(2^10*3^9*(1047712/66108)^3)=80233354159.

Using the same base and <=64 exceptions gives

    N<=4194116990084347+981604*(80233354159+64)
      =82951498428798039 < B.                                  (8)

Thus ALL d=10 coefficient dimensions are paid on 7117..8655, not
just one selected component. Equation (8) is the whole d=10 constant;
the much smaller (7) is stated only for the maximal dimension-four case.

The earlier full-kernel consumer first pays all other curve patterns or
reduces to its two weighted patterns. Both (7) and (8) are below its
paid-alternative constant 274979661292365251. Removing d=10 therefore
leaves only d=7, dim Y=3, 1301<=h<=4327 with that SAME constant.
This last use is owned by the consumer; it is not a reverse premise here.
There is no assertion that the remaining d=7 pattern is impossible,
or that a larger J range or unrestricted original error rank has been paid.
