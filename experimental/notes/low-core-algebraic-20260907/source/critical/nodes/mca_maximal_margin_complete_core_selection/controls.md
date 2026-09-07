# Exact guards and surviving hard cases

## Necessary guards

Over F_5, with K=1,m=4,T=1 and u=0, v=(0,0,0,1,1), the label
gamma=0 has a chosen bad support with raw one, but its complete scalar
agreement set has minimum defect two. A different four-subset attains
raw two. Thus the chosen low-support conclusion is false without
maximizing, even though 2T<d=3.

At the boundary K=1,m=3,d=2,T=1, use u=0, v=(0,0,1,1).
Every bad three-subset has maximum raw one, while the complete set's
minimum defect is two. This defeats replacing 2T<d by 2T<=d.

For a positive control, K=1,m=4,T=1,u=0,v=(0,0,0,0,1) has
maximal raw one and complete defect one. Pair-contained four-subsets
occur in the exchange graph and must not be discarded from its proof.

## Zero and cyclic spaces still occur after maximization

Use F=F_13(beta), beta^6=2. Frobenius sends beta to 4 beta;
4 has order six in F_13, so this is a genuine degree-six extension.
Take K=2,m=5,d=3,T=1, V=span_F{1,X}, and three groups of four
evaluation points, 0..3, 4..7, 8..11. On group i the receiver is
the polynomial pair f_i. In both cases f_0=(0,0):

    ZERO:   f_1=(beta,X),     f_2=(beta^2 X,beta^3),
    CYCLIC: f_1=(1,beta X),   f_2=(X,beta^2).

Every pair difference has two F-independent affine components, hence
no simultaneous zero. Each complete pair core is exactly its four-point
group. There are EXACTLY 23 finite bad labels, each with a unique
admissible bad scalar explanation and a complete agreement set of size
five. Each therefore has globally maximal raw one, with one cross point.

To see completeness, an affine scalar polynomial different from the
three source-piece explanations agrees at most once per group, so cannot
reach five. Every remaining explanation is one of the three pieces.
Its cross labels are the three rational direction maps for unordered
pair differences, restricted to the two respective groups. The maps are
injective there; the first pair has seven finite values (the point x=0
is a pole), and the other two have eight each. Their images are disjoint:
equating maps gives a nonzero polynomial in beta of degree at most three,
using the disjoint group indices. The small verifier checks all labels
and also enumerates all two-point-pinned affine explanations at each.

For ell=d-T=2, the full degree-<=ell E-valued row space is zero
in ZERO and E[X]_(<=2)*(1,0) in CYCLIC. Offsets have degree <4.
Since f_0=0 on four points, every admissible offset has E-coefficients.
Write R=(a+bX+cX^2,e+fX+gX^2). The eight coefficients of
R*f_1 and R*f_2 must then lie in E, and this also suffices.

In ZERO they are

    beta a, beta b+e, beta c+f, g,
    beta^3 e, beta^2 a+beta^3 f, beta^2 b+beta^3 g, beta^2 c.

Write a=A/beta, c=C/beta^2, e=E_0/beta^3, g=G in E-scaled
form, and solve b=B/beta-E_0/beta^4, f=F_0-C/beta. The seventh
constraint gives B beta-(E_0/2)beta^4+G beta^3 in E, so B=E_0=G=0.
The sixth gives A beta+F_0 beta^3-C beta^2 in E, forcing A=F_0=C=0.

In CYCLIC the coefficients are

    a, b+beta e, c+beta f, beta g,
    beta^2 e, a+beta^2 f, b+beta^2 g, c.

The fourth/fifth constraints write g=G/beta and e=E_0/beta^2.
Subtracting the second/seventh shows E_0/beta-G beta in E, hence
E_0=G=0. Then a,b,c in E; the third/sixth force f=0. Conversely
all such rows are admissible. No nonzero old polynomial relation exists
in either example: its offset is zero on f_0 and the two other pairs
are independent over F(X), so its row must vanish.

The full row spaces are also checked by a 40x36 matrix over F_13,
with kernel dimensions zero and three. These actual low, rank-two
cross families show that canonicalization does not close either hard
type. They are not deployed-row over-budget examples.
