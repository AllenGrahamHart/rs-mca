# Rational-coefficient graph controls

The verifier is a small exact arithmetic census, not a proof of the
geometric theorem. The following degree arguments are hand proofs.

## Actual canonical source beyond the old polynomial-X graphs

Let F=F_(787^2), beta^2=2, P=X+beta, D={0,...,782}. Partition D
into 27 groups of size 29 and put (u,v)=(j*P,j^2) on group j,
1<=j<=27. Take K=2, m=30, T=1, h_*=0, V=span{1,P}.
Represented pairs are f_i=(i*P,i^2), all satisfying

    b=a^2/P^2.

Each complete pair core is exactly its 29-point group. At x in group
j, i!=j, the scalar collision label is gamma=-P(x)/(i+j).
Equality of two such labels first identifies i+j by the beta
coefficient, then x, then its group j and finally i. Thus all
27*26*29=20358 labels are distinct and all 27 pairs are represented.

For any fixed printed gamma, a carrier polynomial other than a
source-piece polynomial h_i=i*P+gamma*i^2 agrees at at most one
point in each group, hence at at most 27<30 points. Each h_i agrees
on its own 29-point group; outside it there is at most one point,
by label uniqueness. The printed label has exactly one such extra
point. Thus it has a unique eligible carrier explanation and maximum
raw margin one. The 29 core values pin any degree-<2 second-code
component to i^2, which fails at the defect. Its 30-support is
full-code bad. The canonical cutoff condition 2<30-2 also holds.
This is a census in the specified fixed carrier, not a claim about
every explanation in the full ambient code.

No constant invertible component matrix and polynomial pair offset
puts these pairs on ANY polynomial-X graph of Y-degree 2,...,7.
Write transformed pairs as

    a_t=A*t*P+B*t^2+a_0, b_t=C*t*P+D*t^2+b_0.

If b_t=Psi(X,a_t) for 27 distinct t, the difference, of t-degree
at most 14, is identically zero over F(X). If B!=0, its top degree
2e>2 is impossible. Thus B=0 and invertibility gives A,D!=0.
Degree comparison forces e=2 and its t^2 coefficient requires
p_2(X)*A^2*P^2=D, impossible for polynomial p_2. Offsets do not
change this comparison. This separates the new graph mechanism from
the old one, not from every previously paid class.

The received certificate (4) uses B=P^2, N=Y^2. Its weighted
degree is 3<29, so it really supplies the exact pair identities.

## Primitive derivative, tangent overlap and pole guards

For H containing X and X+1 with tangent degree at most one, the
quadratic derivative images span {X,X^2} and {X+1,X^2+X}.
Their sum has dimension three, not four: the possible one-dimensional
intersection must be retained. Cubic images {X^2,X^3} and
{(X+1)^2,X*(X+1)^2} have four-dimensional sum (e.g. over F_5).
This checks both intersection endpoints, not all geometric families.

With B=X^2, N=Y^2, pair (a,b)=(2X,4), and received value
(u(0),v(0))=(0,1), both the pair identity and received relation
hold at the pole 0. Yet a(0)=u(0) and b(0)!=v(0). Dropping poles
or identifying scalar agreements with complete joint cores is invalid.
The proof uses neither shortcut. Earlier characteristic-dividing-degree
and high-degree false-fit controls remain in force.
