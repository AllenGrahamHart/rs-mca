# Proof By Following A Deficient Contraction

The required supplier proves exact complete-fiber contraction, the joint
top-fiber root budget, the capped second moment and positivity/convexity
of P_r(D,x) on x>=1. Its density assumption is only one way to ensure
the moment at all descendants. Here we do NOT assume that density bound.

## 1. Deficiency Either Stops At A Bad Moment Or Descends

At any actual rank-r descendant with degree k and length n=D+k, write
its projective fiber sizes c_i and M2=sum c_i^2. If

    M2<=n*(k-1)/(r-1)

and every rank-(r-1) child has at least P_(r-1)(D,k-c_i) bases, then
exact contraction, weighted Jensen and monotonicity give

    B_r >= sum_i c_i P_(r-1)(D,k-c_i)
         >= n P_(r-1)(D,k-M2/n)
         >= P_r(D,k).

Consequently a deficient B_r<P_r either has a failing second moment or
has an actually deficient child. Descend through such a child in the
latter case. Each step contracts a FULL fiber and preserves D.

Rank one has exactly n bases. Rank two always has at least n(D+1),
since each fiber has size <=k-1 and B_2=n^2-M2. The descent must
therefore stop at a failing moment in rank r>=3. No hypothetical
intermediate space, real-degree source or guessed cap is involved.

## 2. A Failed Moment Gives A Large Actual Fiber

Any r-1 child fibers have total size <=k-1 by the polynomial root bound.
The supplier's capped-moment argument says that if all c_i<=n/(r-1),
then M2<=n*(k-1)/(r-1). Hence a failing moment has an actual fiber
c>n/(r-1). This is a contrapositive of a proved sufficient condition,
not an equivalence between a large fiber and a deficient basis count.

The accumulated contractions correspond to one COMPLETE original flat
F of rank j=s-r and size a. Its child has n=N-a, k=K-a and rank r.
The new large fiber lifts to a complete rank-(j+1) flat G containing F.
Set t=j+1 and b=a+c. Then

    (s-t)*(b-a)>N-a,

which is FLAG. Because r>=3, t<=s-2. F is spanned by selected original
evaluations, so a>=t-1. The annihilator of G has dimension s-t>=2;
the common-root-space bound gives b<=K-s+t. All coordinates and
subspaces are actual and refer to the same original H.

If desired, a fixed order on H makes every choice deterministic by
selecting the first deficient child and then the first violating fiber.
This changes no label count. Finding one flag does not assert uniqueness,
and a basis-rich core may also contain such a flag.

## 3. MCA Scope

On an empty-universal-core MCA source, every complete pair-core evaluation
is nonzero. Fix the minimizing pair and one M-point core subset BEFORE
applying this alternative. The required earlier defect insertion counts
bases in that core without changing the explanation, minimizer or finite
slope. An exception is a property of this original record's chosen core.
Summing over its possible witnesses is neither necessary nor permitted.

The theorem supplies a geometric witness, not a count of witness-bearing
labels. The finite consumer retains their existing tuple cost and proves
a mass-forcing inequality on ONE original resource. No received-word
quotient or uncharged exceptional-label removal follows from FLAG alone.
