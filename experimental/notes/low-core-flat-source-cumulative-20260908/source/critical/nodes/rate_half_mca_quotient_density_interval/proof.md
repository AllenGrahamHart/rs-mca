# Proof By Quotient Contraction And Density-Aware Completion

Use s=11,R=1048576,d=67472,T=6,D=d-T=67466,c=D+1,
M=J+D, P_d=prod_(i=1)^10(d+i), and U_0(J)=(R+J)_falling_12.
All labels and minimizing pairs are frozen on the stated original source.
The finite checkers use only exact integers; the following argument proves
the universal geometry and coverage those integers certify.

## 1. Exhaustive Source Split

Choose a proper maximum-density flat of the nonzero V-evaluations, of
rank j and size a. Write h=a/j and h_r(J)=1+(J-11)/r. Root-space
bounds give 1<=j<=10 and a<=J-11+j<c.

If h<=h_11=J/11, every LOW core has at least

    B_low(J)=prod_(i=0)^10(J+D-i*J/11)

ordered bases. On a degree block [J0,J1], all factors increase in J;
use floor(B_low(J0)) and the resource U_0(J1). HIGH records retain the
proved tuple charge (J+d)P_d*(10488/125). The same shared-resource
minimum pays both. The exact four comparisons fit the bound in NEW.

Otherwise choose r in j,...,10 such that j*h_(r+1)<=a<=j*h_r.
Equality boundaries may be covered twice; these are whole-source
alternatives, not additive owners. For j=1, any a>=J-2000 is already
paid by the required receiver-fiber theorem at 248408859318207582,
including original near. The remaining INTEGER sizes obey a<=J-2001.
Thus only the r=j=1 upper size edge is reduced from h_1 to J-2001.
This leaves no integer hole and adds no hypothesis on the original source.

Use the four consecutive degree blocks [32000,33999],...,[38000,39999].
For each j,r, split its size region into eight equal affine slices:

    a(J,u)=(1-u/8)*j*h_(r+1)(J)+(u/8)*j*h_r(J), u=0,...,8,

with j*h_r replaced by J-2001 only when j=r=1. Each [u,u+1] region
is the convex quadrilateral determined by its four (J,a) vertices.
Every edge has a=alpha*J+beta, 0<alpha<=1, beta<=0.

## 2. A Uniform Quotient Quadratic, With Directed Rounding

For a LOW record let z be the occupancy of its COMPLETE pair core in A.
Choose an M-point core subset containing ALL z points as in the required
complete-core lemma. Its quotient has rank ell=11-j, degree K'=J-a,
M-z nonzero evaluations and gap D'=D+a-z. No receiver is changed here.

For a record box z/a in [lambda0,lambda1], let a0,a1 be the minimum
and maximum size vertices. Put

    k0=floor(min_vertices(J-a)), E=ceil(max_vertices(J-a)),
    D0=floor(D+(1-lambda1)*a0).

Then ell<=k0<=K'<=E<=D0<=D'. Taking any D0+K' quotient points
retains rank, since D0+K'>K'. It can only reduce the number of bases.
We may therefore use a universal basis lower bound at gap D0. If its
normalized polynomial increases in K', evaluate it at k0. The floors
relax actual integer degrees/gaps; no fractional-degree source is used.

Here is the exact uniform certificate algorithm at gap g=D0 and upper
degree E. Ranks one and two have lower bounds g+k and (g+k)(g+1).
For rank >=3 put P_r=prod_(i=1)^(r-1)(g+i) and H=2^128. Start with

    A=floor(H*g*(2g+1)/(2(g+2))),
    B=floor(H*(3g+1)/(2(g+2))), C=floor(H/(2(g+2))).

The rank-three seed dominates P_3*(A+B*k+C*k^2)/H coefficientwise.
For target rank r=4,...,ell use the required quadratic contraction step.
After normalization by P_r its two profiles are

    S(k)=[(k-r+1)q(r-1)+(g+r-1)q(k-1)]/(g+r-1),
    U(k)=(g+k)q(((r-2)k+1)/(r-1))/(g+r-1),

where q=(A+B*k+C*k^2)/H. Keep the same quadratic coefficient C/H.
The certificate verifies B>=g*C and that U's quadratic coefficient is
at least C/H. Hence U(k)-(C/H)k^2 is convex for k>=0. Take its
tangent at X=min(5000,floor(E/2)), then round its constant and linear
coefficients DOWN to integer multiples of 1/H. This is a lower line
for every k>=0, including if the constant is negative.

Subtract the smallest nonnegative integer multiple of 1/H needed to lie
below S(k)-(C/H)k^2 at BOTH r and E. That difference is affine, so
the endpoint inequalities cover the entire interval. The tangent residual
has the form (k-X)^2*((u_2-C/H)+u_3*(k+2X)), with nonnegative factors.
The next B>=g*C condition is checked again. Induction proves this lower
quadratic for EVERY integer degree between its rank and E.

All instantiated gates, positive evaluation at k0 and B,C>=0 pass in both
implementations. Thus the integer floor of P_ell*q(k0) is a valid lower
quotient-basis count. This proof uses a checked downward-rounded certificate,
not assumed monotonicity of an empirical optimum in either degree or gap.

## 3. Density-Aware Record-Cost Boxes

Split z/a in [0,1] into 64 closed intervals [v/64,(v+1)/64]. Different
records of one source may belong to different bins. Let z0=lambda0*a0,
z1=lambda1*a1 and h1=a1/j. The generic density-aware theorem gives

    d_i=max(c+i,J+D-(10-i)*a/j), i=0,...,j-1.

Set d_i^0 to its smallest value at the four (J,a) vertices. This is a
valid lower bound throughout: max of a constant and one affine function
attains its minimum where the affine function is smallest, at a vertex.
Apply its signed BOX bound with fixed calibrations q=alpha*z1,
alpha in {0,1/4,1/2,3/4,1}. Retain the maximum of those bounds, the
positive b=0 class and the positive-class product lower bound. For j<=5
also retain the old root-only g_j(z0), which is increasing in z at this
scope. Its proof works with any quotient-basis count because the disjoint
inside-class count factors that count out; it is not tied to the old P.

The generic greedy quotient lower count is

    P(J,a,z)=(J+D-z)*prod_(i=1)^(ell-1)
               (J+D-z-min(J-a-ell+i,i*a/j)).

On the chosen r-region its branch is density when j+i<=r and degree
otherwise. For fixed lambda=z/a all factors are positive affine in J,a;
for fixed J,a they are positive affine in lambda. Log-concavity in each
stage shows the minimum of P is at one of the eight vertices including
the two lambda endpoints. Use the maximum of this lower count and the
proved quotient quadratic. Multiplication by a positive signed inner
lower bound is valid only after its positivity check; the b=0 term
guarantees an available positive bound.

We retain two additional independently valid lower counts. The hybrid
full-core greedy product has its fixed density branch at span ranks <=r
and its degree branch afterwards, so its minimum is at a size/J vertex.
Also, for each inside cardinality b separately, the positive term

    binom(11,b)*P(J,a,lambda*a)
      *prod_(i=0)^(b-1)max(lambda*a-i*a/j,0)
      *prod_(i=0)^(j-b-1)(d_i-lambda*a+b)

has its minimum at one of the eight vertices. Indeed the d_i branch is
density when 10-i<=r and constant otherwise. At fixed lambda, every
nonzero term is a product of positive affine factors in J,a. At fixed
J,a it is such a product in lambda wherever positive; below its cutoff
the term is zero. Endpoint minima therefore remain valid across that
cutoff. Sum the individual term minima, not an unjustified minimum of
the sum. The integer implementations take floors of these valid basis
lower counts and then multiply by twelve for the original defect insertion.

Take the minimum with floor((J0+d)P_d*10488/125) to cover HIGH too.
This defines one integer cost beta_v for EVERY record in that occupancy
bin, regardless of whether it later belongs to a light or heavy group.

## 4. One Resource For The Actual Receiver Groups

The required projected-pair theorem gives distance a/j and at most one
heavy group with full-core occupancy t>a-a/(2j). Its light groups have
occupancy <=2a-a/j-t. The full heavy cap is

    Q(t)=(R+J-a)*U_j/(d+J-t)+a-t,

where U_j is the proved full affine-dimension-at-most-(10-j) cap. For
j=1,...,9 use the padded-Johnson supplier's dimensions 9,...,1; for
j=10 use the scalar supplier's exact dimension-zero cap R-d+1=981105.
The larger actual child gap reduces to baseline d by exact bad-subset
selection. The child field, original labels and empty universal core
are preserved; there is no child post-near premise.

Split t/a between 1-1/(2j) and 1 into eight bins [kappa0,kappa1].
For each source box let beta_L be the minimum beta_v over every record
bin meeting [0,2-1/j-kappa0], and beta_H over every bin meeting the
heavy interval. The implementation deliberately includes a neighboring
bin at boundaries, which can only weaken the lower costs. With no heavy
group use the first source bin, whose light endpoint is the correct
threshold; later light caps are not imposed on that case.

The ratio (R+J-a)/(d+J-kappa*a) increases with a and kappa, because
kappa>=1/2 and R+J>2(d+J). Along every upper size edge a=alpha J+beta
it decreases with J: the derivative numerator is

    (1-alpha)d-(1-kappa*alpha)R+beta*(1-kappa)<=0.

Thus, writing A0=a(J0,u+1), A1=a(J1,u+1), an integer heavy cap is

    Q_box=ceil((R+J0-A0)*U_j/(d+J0-kappa1*A0)+(1-kappa0)*A1).

The existing two-cost inequality on ONE original resource gives

    floor((U_0(J1)+max(0,beta_L-beta_H)*Q_box)/beta_L)+134944.

Record bins supply a uniform minimum cost, never independently spendable
budgets. Different source/J/flat boxes are alternative whole-family
bounds and combine by maximum. The exception term and original near
allowance are not omitted or applied twice.

## 5. Exhaustive Exact Certificates And Union

Each degree block has 8*64*sum_(j=1)^10(11-j)=28160 record-cost boxes
and 8*8*sum_(j=1)^10(11-j)=3520 source boxes. The maxima for these
boxes and the low-density branch, EXCLUDING the separately paid large
rank-one-fiber class, are

    32000..33999: 261925431454675420;
    34000..35999: 242907143759668079;
    36000..37999: 225655255580817422;
    38000..39999: 220471747439971004.

The prior large-fiber class has cap 248408859318207582. The maximum
of all five numbers proves NEW, with no remaining carrier premise.
The independent audit uses a different common integer scale, fixed branch
formulas, prefix derivatives and polynomial composition for the quadratic
steps. Streaming hashes bind EVERY cost and source bound, not just the
maxima. It also rejects both adjacent incorrect integer floors for every
source box. No field-size enumeration or floating-point decision is used.

The required complete-core interval pays 40000..169999 by
274929007493481160. Taking the maximum proves UNION. Original-source
transport remains downstream and unchanged; no higher original error
rank, unrestricted row, active-v4 atom or Prize conclusion is inferred.
