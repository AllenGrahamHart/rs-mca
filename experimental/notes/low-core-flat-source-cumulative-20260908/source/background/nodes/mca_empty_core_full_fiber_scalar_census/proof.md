# Proof

## 1. A Scalar Restriction Suffices For Full-Fiber Transport

The nonzero evaluations span V*: evaluation on all n>K points is injective
on degree-<K polynomials, and zero evaluations add no span. There are at
least s projective fibers. The annihilator W=ker ell has dimension s-1
and vanishes on the entire A. Polynomial root capacity gives
a<=K-s+1. Its full locator P_A divides every W-polynomial, leaving actual
dimension s-1 and degree <K-a.

Fix a receiver color C=(alpha,beta). The common pair
(h_*+alpha*f,beta*f) matches the received pair exactly on C inside A.
For EVERY label satisfying the printed scalar restriction,

    h_gamma-h_*-(alpha+gamma*beta)f belongs to W.

This is the only group property used by the earlier receiver-fiber
transport. It does not require that the record's minimizing pair have
restriction (alpha,beta). At a point of A outside C, its gauged scalar
equation has at most one solution gamma. Remove the union of those
exceptional original labels within this family, at cost at most a-t.

For each survivor its COMPLETE scalar agreement set meets A exactly in C.
Divide both gauged received words and explanations by P_A outside A.
A degree-<K-a pair explaining the complete child agreement set would lift
to a degree-<K pair explaining the entire original complete set, including
C, contradicting its full-code-bad selected witness. The child has at least
m-t agreements. The required one-point-exchange argument gives an exact
bad subset of size m-t, or m-a: adjacent subsets overlap in at least K-a
points, and polynomial uniqueness glues hypothetical explaining pairs.
If m-t>n-a, the claimed survivor's agreement count is impossible.

Outside A, a W-evaluation is zero precisely when the V-evaluation is zero:
otherwise it is a nonzero multiple of ell and belongs to A by completeness.
At a V-zero the common gauging pair equals (h_*,0). The original empty
universal core and nonzero locator division therefore preserve empty
universal core in the fixed child carrier. The selected explanation span
may shrink, but the enclosing carrier retains actual dimension s-1.

## 2. Count Original Scalar Incidences

Each original support contributes m incidences. A carrier-zero coordinate
has at most one agreeing finite label because its scalar equation is not
identically zero. Their total contribution is at most z.

For each nonzero fiber A and color C, the selected incidences in C number
at most t|Gamma_(A,C)|. The child transport bounds this by
t(G(K-a)+|E_(A,C)|). Sum these incidence bounds, not a disjoint partition
of slope sets. Since the actual colors partition A, sum_C t=a and

    sum_C t(a-t)=a^2-sum_C t^2.

This proves LEDGER. The same label may occur in several colors or fibers;
the charged object at this step is its selected coordinate incidence.

## 3. Retain The Joint Fiber-Size Constraint

Any s-1 distinct fibers lie in a proper subspace of V*. A nonzero
annihilating polynomial shows that their total size is <=K-1. This root
argument remains valid when the nonzero subdomain has fewer than K points:
its evaluations still span V*, as proved from the original full domain.

Every color has positive integer size, so sum_C t^2>=a. With N=n-z,
LEDGER is at most

    sum_A phi(a)+z, phi(a)=a(F(K-a)+a-1).

Order the sizes decreasingly; let b0 be the (s-1)-st size and put
q=s-2, h=K-1, A0=h-q*b0. Then 1<=b0<=h/(s-1).
Tail fibers have size at most b0. Their contribution is at most their
mass times F(K-b0)+b0-1, by monotonicity of F.

For top fibers subtract that same linear mass cost. The resulting
function psi(a)=phi(a)-a(F(K-b0)+b0-1) has

    psi(b0)=0, psi'(b0)=-b0*F'(K-b0)+b0>=0,
    psi''(a)=-2F'(K-a)+aF''(K-a)+2>=0.

It is convex and nondecreasing for a>=b0. Increase the total top mass
to h, then concentrate its excess above b0 in one entry. This gives

    C_N(b0)=A0(F(1+q*b0)+A0-1)
                    +(N-A0)(F(K-b0)+b0-1).

All top entries remain within [b0,K-s+1]. This is an upper bound from
a real partition relaxation, not an asserted realizable fiber profile.
As F(K-b0)+b0-1>=1, C_N(b0)+z<=C_n(b0).

## 4. Convexity Leaves Two Endpoints

For real b in [1,(K-1)/(s-1)], set A=K-1-q*b. Differentiating gives

    C_n''(b)=q^2[A F''(1+q*b)-2F'(1+q*b)]
              +(n-A)F''(K-b)-2q F'(K-b)+2q(q+1)>=0.

Thus C_n is convex and its maximum is at an endpoint. At b=1 its
value is S; at b=(K-1)/(s-1), A=b and its value is U. The argument
also covers s=2 (q=0). If K=s the interval is a singleton and no
derivative is needed. Dividing by m and taking the integer floor proves
PROFILE. All evaluations of a child cap on an actual source were at
integer degrees before this continuous relaxation.

The proof neither establishes convexity of iterated upper envelopes nor
allows the hypotheses on F to be omitted. In particular, taking maxima,
dividing by d+K, and adding color charges does not automatically preserve
the required nonincreasing convex shape.
