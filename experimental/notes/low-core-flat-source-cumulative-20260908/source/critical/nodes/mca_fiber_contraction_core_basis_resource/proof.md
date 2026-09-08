# Proof By Contracting The Entire Projective Fiber

## 1. Exact Polynomial Contraction

The nonzero evaluations span V*: a nonzero degree-<K polynomial cannot
vanish on N>=K distinct points. There are therefore at least r fibers.
For x in a fiber A, W=ker(ev_x) has dimension r-1. The coordinates
in H where W vanishes are exactly A: their nonzero evaluation functionals
belong to the one-dimensional annihilator of W in V*.

The full locator P_A divides every W-polynomial. Division gives actual
dimension r-1, degree <K-a, and nonzero evaluations on H minus A.
The common-root-space bound gives a<=K-r+1, so K-a>=r-1.
Independence after selecting x first is precisely independence of the
remaining r-1 evaluations on W. Locator division scales those evaluations
by nonzero numbers and preserves rank. Counting the possible first
coordinates gives (CONTRACT), with no multiplicity loss.

Fibers here are relative to the counted core H. Coordinates outside H
are not discarded from an MCA source; this is an auxiliary basis count.

## 2. A Fiber Second-Moment Bound And The Seed

Any r-1 projective fibers lie in a proper subspace. A nonzero annihilating
polynomial shows that their total size is at most K-1. Put h=K-1,
m=r-1, and order sizes decreasingly. Let b=a_m. Then

    1<=b<=h/m, a=h-(m-1)b>=b.

Tail fibers have size <=b, so their squares are at most b times their
mass. For the top m fibers, the function s^2-b*s is convex and increasing
on s>=b. Increasing the top mass to h, then concentrating its excess in
one entry, bounds their excess squares by a(a-b). Consequently

    sum a_i^2 <= b*N+a(a-b)
       <=max(N*(K-1)/(r-1), N+(K-r+1)(K-r)).          (MOMENT)

The second inequality follows by convexity of the quadratic in b on its
closed interval. Both extrema are relaxations of the integer partition.

Rank two has at least (D+k)(D+1) ordered bases, since each nonzero
evaluation fiber has size <=k-1. For rank three, contraction therefore
gives (D+1)(N^2-sum a_i^2). In (MOMENT) the difference twice the
second branch minus twice the first is

    (K-3)(K-D-4)<=0 for 3<=K<=D.

Thus sum a_i^2<=N(K-1)/2, proving (SEED).

## 3. Keep The Cubed Fiber Sizes Through The Quadratic Bound

Let F be as in (STEP). For fixed K put phi(s)=s F(K-s). Its second
derivative is

    phi''(s)=-2B-4CK+6Cs<=-2B+2CK<=0

on 1<=s<=K-r+1, because K<=D. Moreover F is increasing on the
child-degree interval. For fixed b as above, replace the tail contribution
by its mass times F(K-b), a LOWER bound because tail sizes are <=b.
The total from (CONTRACT) is at least

    N F(K-b)+sum_(top m fibers) psi(a_i),
    psi(s)=phi(s)-s F(K-b).

Here psi is concave, psi(b)=0 and psi'(b)=-b F'(K-b)<=0. It is
therefore nonincreasing on s>=b. Increasing top mass up to h only
decreases this lower expression. At fixed sum h, concavity makes its
minimum occur at the extreme partition (a,b,...,b). All intermediate
sizes remain in [b,K-r+1]. We obtain the valid lower bound

    C_K(b)=a F(K-a)+(N-a)F(K-b), a=K-1-(r-2)b.       (1)

This retains both the second and third moments implicit in phi. Replacing
the third moment by an unrelated bound would lose this conclusion.

## 4. Only Two Fiber Profiles Remain

Put t=r-2>=2. Direct expansion of (1) gives

    C_K''(b)/2 = -B*t*(t+1)
      + C*(D+t*(t-2)*K-3*t^2+1-3*t*(t^2-1)*b).

Since B>=DC, K<=D and b>=1, this is at most

    C*(D*(1-3*t)-3*t^2+1-3*t*(t^2-1))<=0.

When C=0 the unrelaxed expression is -B*t*(t+1)<=0 too.
Hence C_K is concave on 1<=b<=(K-1)/(r-1). Its minimum occurs
at an endpoint. At b=1 it is S_r(K); at b=(K-1)/(r-1) it is U_r(K).
Every evaluation of F on an actual child used an integer degree; real b
was introduced only to lower-bound a polynomial expression already valid
on actual partitions. This proves (STEP).

## 5. The Original Incidence Resource

For the selected MCA interface, choose one minimizing second polynomial.
Full-code badness gives at least one actual defect. Universal-core
emptiness ensures that joint-core evaluations are nonzero. Restrict to
any fixed m-T core subset and apply the basis lower bound.

The required completed-basis supplier identifies a core basis with s
independent incidence normals spanning the hyperplane for that pair.
Any actual defect is outside this hyperplane. Its unique position in an
ordered (s+1)-tuple recovers the insertion, giving (s+1)*B tuples.
Each independent tuple fixes the entire affine parameter, including the
original finite slope. Thus distinct slopes have disjoint tuple sets.
Use the minimum LOW/HIGH per-record count on their ONE shared budget.
No original receiver, label, coordinate or denominator is changed.

This is elementary polynomial contraction and concavity; no external
matroid extremal theorem or numerical realizability assumption is imported.
