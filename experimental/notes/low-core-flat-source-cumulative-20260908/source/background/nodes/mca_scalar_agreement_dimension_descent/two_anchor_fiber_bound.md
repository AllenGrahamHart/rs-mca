# Two-anchor bound from jointly realizable evaluation fibers

Status: PROVED, 2026-09-07. Retain the exact selected-record setup of
statement.md, and suppose 3<=s<=K. In this companion the F-linear
space C' has NO common evaluation zero on D. Let an integer U>=1
bound every resulting dimension-at-most-(s-2) family on
(n-2,K-2,m-2), in the full shortened code.

Put R=n-K, d=m-K, and

```text
W=K-s+1, H=W+1,
F_bal = n*(2*n-H)/(m*(2*m-H)),
F_spike = (R+s-1)/(d+s-1)
        + (R+s-1)*(R-d)/(m*(m-1)).
```

Then the ORIGINAL selected slope count satisfies

```text
|Z| <= floor(U*max(F_bal,F_spike)).                 (1)
```

Both branches of the maximum are necessary for this envelope. This is
an upper theorem using jointly realizable fibers, not independent choices
of a worst child at each coordinate.

## 1. The fibers and their joint restriction

Write ell_x for evaluation on C' at x. Since ell_x is nonzero,
partition D by its projective evaluation functional: x and y are in
the same fiber when ell_y is a nonzero scalar multiple of ell_x.
Let the positive fiber sizes be w_i.

For one fiber, ker ell_x is an (s-1)-dimensional polynomial space
vanishing on the whole fiber, so w_i<=K-s+1=W. For TWO distinct
fibers, their functionals are independent. Their common kernel has
dimension s-2 and vanishes on their union. Dividing by that union's
locator gives the decisive joint restriction

```text
w_i+w_j <= K-s+2=H             (i!=j).              (2)
```

The evaluation functionals span the full dual of C': otherwise a
nonzero degree-<K polynomial would vanish on all n points. Thus at
least s fibers exist. In particular there is always another fiber.

## 2. Bound one anchored child using its actual zero set

Fix x in a fiber of size w. Apply the common gauge from proof.md
to precisely the selected records whose support contains x. The child
direction is the image of ker ell_x under division by X-x.
Its common evaluation zero set is EXACTLY that fiber minus {x}:
at a remaining y, evaluation on the kernel is zero if and only if
ell_y is proportional to ell_x.

Within the fiber, let c count coordinates where the chosen common pair
(a_0,b_0) matches the received pair. The anchor is one of them, so
1<=c<=w. The child's universally satisfied zeros number c-1;
its exceptional zero coordinates number at most w-c. The scalar ledger
from proof.md, now using the second proper child cap U, gives

```text
N_x <= ((n-w)*U+w-c)/(m-c)
    <= (n-w)*U/(m-w).                              (3)
```

The last comparison follows by setting a=w-c>=0 and using
(n-w)*U>=m-w>0. No claim that the child's zeros are all universal
is made. The second anchoring step is again on its selected support,
so original slope labels and exact badness survive both steps.

Each original selected support contributes m incidences. Therefore

```text
m|Z| <= U*sum_i f(w_i),
f(v)=v*(n-v)/(m-v).                                (4)
```

## 3. A two-endpoint envelope, not independent fiber maxima

Let u=max_i w_i, so 1<=u<=W=H-1. The quotient f(v)/v is
increasing because n>=m. If u<=H/2, equation (4) has

```text
sum_i f(w_i) <= n*(n-H/2)/(m-H/2).                 (5)
```

If u>=H/2, (2) puts every other fiber below H-u. Hence

```text
sum_i f(w_i)
 <= f(u)+(n-u)*(n-H+u)/(m-H+u) =: Q(u).            (6)
```

Q is convex on [H/2,H-1]. Indeed,

```text
f''(u)=2*m*(n-m)/(m-u)^3 >=0,
[(n-u)*(n-H+u)/(m-H+u)]''
 =2*(n-m)*(n+m-H)/(m-H+u)^3 >=0.
```

All denominators are positive since m>K>=H. At u=H/2, Q
is the right side of (5); at u=H-1=W it equals

```text
W*(n-W)/(m-W)+(n-W)*(n-1)/(m-1).                   (7)
```

These are the balanced and one-large-fiber endpoints. Dividing their
maximum by m proves (1), since n-W=R+s-1, m-W=d+s-1,
and the expression in (7) divided by m simplifies to F_spike.
When H=2 the interval is a point; when n=m both branches equal one.

## 4. Monotonicity for a finite consumer

With R,d,s fixed and n=R+K,m=d+K, the two factors of

```text
F_bal(K)=(R+K)/(d+K)
         * (2R+K+s-2)/(2d+K+s-2)
```

decrease with K. F_spike(K) decreases as well by its displayed
formula. Both decrease as d increases at fixed R,K, provided d<=R.
For comparing a normalized row, the stronger useful statement is:
at fixed original R,K,d and 0<=g<=z<=K-s, put

```text
K'=K-z, d'=d+z-g, m'=K+d-g.
```

If d'<=R, then each F branch at (K',d') is no larger than
the corresponding branch at (K-g,d). For F_bal its first numerator
and second numerator decrease as z increases, its first denominator
stays fixed and its second denominator increases. For F_spike,
R+s-1 is fixed, d'+s-1 increases, R-d' decreases, and m'
is fixed. No independent choice of child field, source or row is made.

The companion finite consumer proves common-zero normalization before
using this comparison. This theorem alone is not an unrestricted
rank-twelve or prize-row payment.
