# Proof

Write the received pair as (u,v). Raw margin means the uncapped minimum
on the selected size-m support; theta=min(d+1,raw). The margin supplier
proves theta>=1. Keep its stronger, pre-maximization bound: if z counts
zero lifted normals (v(x),-C'(x)), then

    sum theta <= F(z),   0<=z<=K-s.                         (1)

Replacing the supplier's universally satisfied zero count by z only
increases its upper bound. No numerical C_s is substituted yet.

Only complete cores of LOW records must lie in U. The tuple resource
is still taken over ALL selected records on the original full domain.
No assertion about a high record's core or its behavior on U is used.

## 1. The scalar kernel and its ordinary list

Call a record low when raw<=T. Its selected support contains at least
m-T>=K points of its complete pair core. If there are no low records,
(1) alone pays the claimed result, since the maximum of F is at the two
endpoints. Otherwise distinguish the two projective kernel charts.

Finite chart: write u+gamma_0 v=c on U, with deg c<K. For a low record,
root counting on its at-least-K core points gives

    c=h_gamma+(gamma_0-gamma)b_gamma,
    h_gamma=c+(gamma-gamma_0)b_gamma.                       (2)

In particular c belongs to h_*+C'. Discard the one possible label
gamma_0 at cost at most one. Group all other low records by b=b_gamma.
For a represented b, its complete joint pair is (c-gamma_0 b,b),
independent of the slope. On U its core is exactly {v=b}.

Infinite chart: write v=c on U. Root counting gives b_gamma=c in C'
for every low record. Group them by a=h_gamma-gamma c in h_*+C'.
On U the complete pair core of (a,c) is exactly {u=a}.
There is no discarded finite label here; the same +1 is conservative.

In either chart let f denote a represented list polynomial and a_f its
agreement count on U with the relevant receiver. Set

    t_f=max(1,m-a_f).

Its represented low records satisfy 1<=t_f<=raw<=T. Indeed their
selected supports need at least m-a_f coordinates outside U. They also
need at least one such coordinate if a_f>=m: otherwise their selected
support is contained in their complete polynomial pair core, contrary
to pair noncontainment. This explicitly covers cores of size >=m;
no whole-line-farness assumption is used.

For one fixed f, an outside coordinate can lie in the selected support
of at most one of its slopes. In the finite chart its equation is

    (u-c+gamma_0 b)+gamma(v-b)=0.

If it held for two labels, that coordinate would be in the complete
core of (c-gamma_0 b,b), and hence in U. The infinite chart uses
(u-a)+gamma(v-c)=0 and the identical argument. Thus at most e/t_f
distinct labels represent f. Complete cores, not truncated supports,
are essential to this injection.

## 2. The shared zero parameter

In the finite chart let g count points of U where C' vanishes and v=0.
In the infinite chart let g count points of U where C' vanishes and
u=h_*. In both cases g is the number of universally agreeing common
zeros of the ordinary list carrier. Also 0<=g<=z<=K-s in (1): in the
finite chart this is immediate; in the infinite chart v=c in C' on U,
so v vanishes at every common zero of C'.

For threshold m-t, remove the common-zero coordinates from the ordinary
list incidence count. At most g agreeing coordinates per word are removed.
Every other anchor imposes a proper affine constraint, and subtraction
and division by X-x inject its list into the declared V_t child.
If z_U counts all common zeros on U, the cumulative number M_t of
polynomials with t_f<=t therefore satisfies

    M_t <= (n-e-z_U)V_t/(m-t-g)
         <= (n-e-g)V_t/(m-t-g).                            (3)

The denominator is positive: g<=K-s and t<=d imply m-t-g>=s.
The ordinary list carrier is C' in the finite chart, h_*+C' in the
infinite chart. Thus the same g governs (1) and (3).
If an anchor has degree bound zero, its polynomial list contains at
most one word and is covered by V_t>=1.

## 3. Weighted resource, not separate worst cases

Let N be the selected count after the optional kernel-label removal.
The high records contribute theta>=T+1, so

    N-sum(theta)/(T+1)
       <= sum_low (1-raw/(T+1)).                           (4)

For each represented f, its term is at most
e(1/t_f-1/(T+1)). Summation by parts gives exactly

    sum_f (1/t_f-1/(T+1))
       = sum_(t=1)^T M_t/(t(t+1)).                         (5)

The resource of the retained labels is no larger than the original
resource. Since z>=g, (1) is at most C(g). Combining (3)-(5) gives
|Gamma|<=1+W(g). It remains to eliminate the unknown g correctly.

## 4. Convex elimination of the shared parameter

Let a=n-m>=s and y=m-g>0. Up to the positive constant P,

    F(g)=prod_(j=0)^s (y+a-j)/y.

This is a polynomial in y with nonnegative coefficients, plus a
nonnegative constant times 1/y. Every term has nonnegative second
derivative for y>0. Hence F is convex in g. This also proves that its
maximum on [g,K-s] is at an endpoint, justifying C(g) above.
The maximum of a convex function and a constant is convex.

Each list factor in W has the form

    (n-e-g)/(m-t-g)=1+(n-m-e+t)/(m-t-g).

Its constant numerator is nonnegative because e<=n-m. It too is
convex in g. Thus W is convex, so W(g)<=max(W(0),W(K-s)).
This proves (GL1), including the no-low case handled in step 1.

The common parameter is load-bearing. Maximizing the margin resource
and the list bound independently loses the payment in the finite
consumer; that loss does not falsify either bound separately.
