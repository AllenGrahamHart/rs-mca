# Proof: use weights two and three, with every component retained

Work over the algebraic closure k of the constant field. Actual finite
labels, polynomial pairs and row denominators stay over F. The required
jet supplier supplies its pure-power lemma and, transitively, the ordinary
hypersurface degree and algebraic-incidence facts.

## 1. Coordinates adapted to the cubic and the common carrier

Set x=A*a+B*b and choose a complementary F(X)-linear coordinate y.
The cubic has equation

    c*x^3+q20*x^2+q11*x*y+q02*y^2+q10*x+q01*y+q00=0,
    c*q02!=0.                                       (1)

Indeed the unique infinity point is [0:1:0]; its smoothness says q02!=0.
The top binary form has a unique linear factor defined over F(X):
in characteristic >3 a coefficient ratio recovers its direction.

Use affine coordinates xi_1,...,xi_N for the image of the carrier under
x, and eta_1,...,eta_d for the projection kernel; N=2s-d. A linear
section of the projection gives affine coordinates on the WHOLE pair
carrier, not just the curve. Then x depends affinely only on xi, while
y depends affinely on both xi and eta, with rational X coefficients.
Give xi weight two and eta weight three. Every coefficient equation in
(1), after clearing fixed X denominators, has weighted degree <=6.
In particular the cubic term contains no eta. This is the improvement
over treating all 2s coordinates as ordinary degree-three variables.

The projection of the coefficient locus to its x polynomial has finite
fibers: fixing x fixes at most two rational functions y by (1), hence at
most two pairs. This remains true on every closed subvariety, after
constant extension. We will need it for the incidence induction.

## 2. Bound dimension without assuming a polynomial normalization parameter

Completing the square in y transforms (1) into y_1^2=R(x), deg R=3.
Its affine singularity gives a repeated root alpha of R, defined over
F(X): the double-root gcd is linear, or the triple root is recovered
from the x^2 coefficient by dividing by three. Write

    R(x)=a*(x-alpha)^2*(x-alpha+b), a!=0.

Away from the single singular point, tau=y_1/(x-alpha) satisfies
tau^2=a*(x-alpha+b). Thus the original pair is

    f=f_s+(tau^2-lambda)*(P+tau*Q), lambda=a*b,          (2)

with fixed independent P,Q in F(X)^2. Its cubic leading vector Q
is in the kernel of A*first+B*second because x is quadratic in tau.

All admissible tau lie in a FIXED bounded rational-function space.
To see this, tau^2 is a fixed rational affine expression in the original
bounded polynomial pair. Choose a polynomial D clearing its denominators
and a uniform degree bound on the resulting numerator. At each finite
place ord(tau)>=-ord(D)/2, so D*tau is polynomial. The same equation
bounds its degree at infinity. Thus h_0=D*tau belongs to a fixed
finite-dimensional polynomial space; D and that space need not be small.

Impose original affine pair membership on (2) in these h_0 coordinates.
At projective infinity, the leading cubic pair is Q*h_0^3/D^3 and
belongs to the projection kernel. Choose a nonzero component of Q.
Projection onto that component is injective on the kernel: its other
multiplier in A*first+B*second is nonzero. Its image W is a d-dimensional
subspace of V, with degree bound <K. The required pure-power jet lemma
therefore bounds each positive-dimensional parameter component by
ceil(d/3); when d=0 no nonzero leading pair can occur at infinity.
The image of the admissible parameter locus contains every nonsingular
pair and cannot have larger dimension. The extra singular pair has
dimension zero. This proves r_0, without deleting parameter poles or
assuming that tau has degree <K. The characteristic guard concerns W.

## 3. A degree budget for ALL dimensions of an equation locus

We use the following elementary strengthening of the degree-cover lemma.
If Z in affine M-space is defined by equations of degree <=e, e>=1,
then its distinct irreducible components Z_i satisfy

    sum_i deg(Z_i)*e^(dim Z_i) <= e^M.                 (3)

Start with affine M-space, whose budget deg*e^dim is e^M. At any
irreducible current piece not contained in Z, select a defining equation
nonzero on it and cut by that equation. A nonzero constant removes the
piece. Otherwise all children have dimension one less and their degrees
sum to at most e times the parent's degree, by the existing hypersurface
degree lemma. Hence their total budget does not increase. Keep a piece
already contained in Z, and continue cutting the others. Each branch
terminates in at most M cuts; the final union is exactly Z. Every maximal
irreducible component of Z occurs among the final pieces. Duplicates or
extra lower-dimensional pieces only overcount the nonnegative budget.
This proves (3), including nonpure loci and isolated points.

It is important to use the actual equation locus here. A convenient pure
cover could have extra components with positive-dimensional x fibers;
the incidence argument below would then not be justified on that cover.

## 4. Ordinary finite power cover proves the weighted incidence bound

There are finitely many counted polynomial pairs: F is finite in the row
application; alternatively agreement at K prescribed coordinates already
determines a polynomial pair, so the rich set is finite over k too.
Choose constants c_i,b_j in k different from all their respective xi_i,
eta_j coordinates. Consider the finite power cover of affine 2s-space

    xi_i=z_i^2+c_i, eta_j=w_j^3+b_j.                  (4)

Each counted pair has exactly 2^N*3^d distinct lifts. No branch coordinate
vanishes on those fibers, and characteristic is neither two nor three.
This is an existence device, not enumeration or alteration of the code.

Pull back the entire coefficient locus. Call the reduced result Z.
It has dimension <=r and equations of ordinary degree <=6. By (3),

    sum_i deg(Z_i)*6^(dim Z_i) <=6^(2s).              (5)

The map to the x polynomial still has finite fibers. For any irreducible
positive-dimensional subvariety T of Z, let g count coordinates at
which scalar agreement x(x_j)=A(x_j)u(x_j)+B(x_j)v(x_j) is identical.
Two points of T with distinct x polynomials exist, so g<=K+h-1.
Each counted point satisfies at least A_agree-g nonidentical equations.
After (4), each such agreement equation is an ordinary polynomial of
degree <=2. Its proper section has total degree <=2*deg(T).

The usual degree-weighted incidence induction, now with these quadratic
sections, gives at dimension v

    #rich points on T <= deg(T)*(2*Q_h)^v.             (6)

The base v=0 is its degree. The induction counts incidences and uses
(n-g)/(A_agree-g)<=Q_h; all section components still have finite
x fibers. It can overcount scalar agreements relative to joint agreements,
which is harmless. No X-coordinate, including a denominator root in
the displayed curve equation, has been removed from this count.

Since Q_h>=3, (5)--(6) and dim Z_i<=r imply

    #rich lifts <=6^(2s-r)*(2*Q_h)^r.

Divide by the EXACT lift multiplicity 2^N*3^d from (4). This gives

    M <=2^d*3^(2s-d-r)*Q_h^r,

as asserted. In dimension zero the same proof gives 2^d*3^(2s-d);
when d=0 this is 3^(2s), without any ratio assumption. The singular
pair was present throughout. Integrality allows the final floor.

## 5. Baseline raw-resource assembly

Use `projection_height.md` with s=11,K=J<=8655. For d>=1 its
height bound is independent of the larger kernel coefficient bound.
For d=0 use dimension zero directly. For all other cases the largest
Q_h on the interval occurs at the printed height ceiling, since
(1048577-h)/(66973-h) increases with h. It is always >=3.

The common resource/near upper is base=46043200488601452. One pair
carries at most D=981604 original LOW labels. For a cubic group plus
<=64 off-curve pairs the bound is base+D*(floor(WC)+64). Exact values:

    d   r   h_max    floor(WC)       whole-source bound
    0   0   unused    31381059609       76846974187856944
    1   1    8654    124350118988      168105774750520860
    2   1    8654     82900079325      127418250017161408
    3   1    8654     55266719550      100293233528582308
    4   2    8654    218999078992      261013572486287276
    5   2    8654    145999385995      189356781841660088
    6   2    4327     85054993483      129533522374310840
    7   3    4327    315063751327      355311039109012616
    8   3    2884    196986237004      239405678739498524
    9   3    1730    124890780289      168636490046227664
   10   4     865    423859179691      462105066772828472
   11   4       0    269141725396      310233794767039292

Only d=7,10,11 exceed B=274980728111395087 in this sufficient recipe.
At those d, using r one smaller instead gives whole bounds
101703415100342464, 124800581927315144, 96665052831852940,
all within budget. Hence an unpaid source must attain dimension r_0.

The largest paid bound is 261013572486287276, with reserve
13967155625107811. This is larger than the earlier cubic dichotomy's
paid alternative 255637082913634099: the NEW, stronger residual
restriction needs this NEW bound if phrased as a dichotomy. It does not
retroactively strengthen the old numerical bound. Both are below B.

The global resource and near allowance occur once. Labels on other groups
are not declared HIGH. No kernel-coverage assertion is proved here;
the existing full-kernel consumer supplies its <=64 exceptional pairs.

The stronger required completed-basis resource is used in
`completed_high_weight.md`. It pays d=11 and d=7 at low height;
the three cases in this baseline table are not the final unresolved set.
