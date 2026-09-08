# Proof

All arithmetic is over F. The domain has n distinct points, and
1<=k<=a<=n. Put ell=a-k. No computation or imported theorem beyond
elementary polynomial and linear algebra facts is a premise.

## 1. Every low-degree relation constrains every listed pair

Fix R=(R_0,R_1) in V_a(y), and put

```text
T_R=rem_(P_D)(R_0 U_0+R_1 U_1),  deg T_R<a.
```

For a listed pair f, the polynomial

```text
T_R-R_0 f_0-R_1 f_1
```

vanishes at each common agreement coordinate. Its degree is <a:
deg(R_i f_i)<=ell+k-1=a-1. It has at least a distinct roots, so
it is zero. This proves (R1)'s consequence simultaneously for the
whole threshold list, including larger agreement sets. No agreement
set is selected or counted as an additional object.

If two relation rows R and S are independent over F(X), subtracting
their equations for any two listed pairs gives a homogeneous 2-by-2
system with nonzero polynomial determinant. It is invertible over
F(X), so the two polynomial pairs are equal. Therefore N(y)<=1.

## 2. One row gives an exact scalar list, with the gcd roots retained

Choose any nonzero R in V_a(y). Let G be the monic gcd of its two
entries, allowing one entry to be zero. Write

```text
R_i=G A_i,  gcd(A_0,A_1)=1,  c=deg G,
d=max(deg A_0,deg A_1).
```

If G does not divide T_R, the polynomial equation proved in section 1
has no solution. The joint list is empty. Otherwise put T=T_R/G.
All listed pairs belong to the affine polynomial solution set

```text
S_R={f: deg f_i<k, A_0 f_0+A_1 f_1=T}.                (5)
```

If S_R is empty, again N(y)=0. If it is nonempty, fix ANY f* in it;
f* need not be a list member. Its choice introduces no multiplicity.
The homogeneous polynomial solutions are exactly

```text
(f_0,f_1)=(f*_0+A_1 H, f*_1-A_0 H).                  (6)
```

Indeed, A_0 v_0+A_1 v_1=0 and coprimality imply A_1 divides v_0
and A_0 divides v_1, with the same scalar polynomial H and opposite
signs. If an entry is zero, the other primitive entry is a nonzero
constant, and the same conclusion follows directly. At least one
A_i has degree d, so for nonzero H the degree bound on both
differences in (6) is equivalent to deg H<k-d.

If d>=k, S_R therefore consists of f* alone and N(y)<=1. Suppose
now d<k. The crucial source-only exceptional set is

```text
J={x in D: A_0(x)y_0(x)+A_1(x)y_1(x) != T(x)},
D'=D\J.                                             (7)
```

Because the original, undivided relation holds on D, J is contained
in {x in D:G(x)=0}. In particular |J|<=c. At every x in J, no
pair satisfying (5) can equal y at that coordinate. These points
are forced errors, not free agreement points. Dividing G in the
evaluation identity without retaining (7) would be invalid.

For x in D', define e_i(x)=y_i(x)-f*_i(x). They satisfy
A_0(x)e_0(x)+A_1(x)e_1(x)=0. Coprimality implies that A_0 and A_1
never vanish simultaneously at any field element. Consequently there
is a UNIQUE value w(x) satisfying

```text
(e_0(x),e_1(x))=(A_1(x),-A_0(x))*w(x).               (8)
```

It can be defined as e_0/A_1 where A_1 is nonzero, and as -e_1/A_0
otherwise. For (6), common agreement at x in D' is now equivalent
to H(x)=w(x). There is no common agreement at x in J. Thus (6)
gives an exact bijection

```text
{joint codeword pairs with agreement >=a on D}
    <-> {H: deg H<k-d, agreement(H,w on D')>=a}.      (9)
```

It preserves the exact agreement set, considered as a subset of D'.
If |D'|<a, both sets are empty. Otherwise k-d<=k<=a<=|D'|, so
the scalar RS code is well-defined. Its field is F, its dimension
is k-d, and the agreement threshold remains a, NOT a-|J|.

Extend w arbitrarily from D' to D. Each polynomial in the right side
of (9) is also an RS[F,D,k] codeword with at least a agreements
with this extension. Distinct H remain distinct codewords since
their degrees are <k<=n. Hence N(y)<=M_1. The empty and singleton
cases satisfy this too, since M_1>=1 by taking a codeword as receiver.

## 3. Exact worst-case split

Every source with V_a(y) nonzero is bounded by M_1, by section 2.
The other sources are exactly those used to define M_0. Therefore
max_y N(y)<=max(M_1,M_0).

For the reverse inequality, the M_0 class is a subclass of all sources.
For any scalar received word W, the joint source (W,0) has exactly
the pairs (f,0) with f in W's scalar list. Any second polynomial
agreeing with zero on at least a>=k points must be zero. Taking W
that realizes the finite maximum M_1 gives max_y N(y)>=M_1.
This proves (R2), including when the relation-free class is empty.

Equivalently, for every integer budget B>=0, full two-component
safety at B is equivalent to scalar safety at B AND relation-free
two-component safety at B. This is an equality of actual worst-case
counts, not the proposal of either upper assertion as a theorem.

## 4. Source invariance and the dimension gate

If codeword polynomials g_i are added to the received components,
the remainder changes by R_0 g_0+R_1 g_1. Its degree is <=a-1<n,
so the condition of vanishing coefficients in degrees a,...,n-1
is unchanged. Thus V_a(y) itself is unchanged. A constant invertible
2-by-2 component transformation sends relation rows by its inverse;
it preserves the degree limit and rational-function rank.

Taking those n-a high coefficients defines an F-linear map

```text
F^(2(ell+1)) -> F^(n-a)
```

with kernel V_a(y). If 2(ell+1)>n-a, every source has a nonzero
row. This inequality is precisely 3a>n+2k-2. In that range the
relation-free class is empty, and (R2) gives (R3). The equality
case of the dimension inequality is not included.

The relation rank over F(X) can only be zero, one or two. Rank
zero here means the WHOLE row space is zero, not merely that one
chosen row failed. Rank one is handled by any nonzero row with
the explicit root treatment above; rank two is the singleton case.
The argument proves existence where stated, not a fast algorithm
for constructing the kernel on a million-point domain.

## 5. What relation-free candidates must look like

Let V_a(y)={0}, and suppose a listed pair exists. Its canonical
polynomial error pair (U_0-f_0,U_1-f_1) cannot be identically zero:
otherwise both constant unit rows would belong to V_a(y). Factor
the error pair as G(E_0,E_1) with G monic and primitive (E_0,E_1).
All common agreement points are roots of G, so deg G>=a.

If max deg E_i<=ell, then the nonzero row (E_1,-E_0) satisfies

```text
E_1 U_0-E_0 U_1 = E_1 f_0-E_0 f_1,
deg(E_1 f_0-E_0 f_1)<a.
```

It belongs to V_a(y), a contradiction. Therefore max deg E_i>=ell+1.
With h=max(k-1,deg U_0,deg U_1), one has
h>=deg G+max deg E_i>=a+ell+1=2a-k+1. This proves (R4).
It does not bound the number of these high-cofactor candidates.

## 6. Hand checks and a normalization counterexample

For y=(W,0), the constant row (0,1) recovers exactly the scalar
RS[k] list, with no domain deletion. For y=(W,XW), where the
second component means coordinatewise multiplication on D, the
row (-X,1) lies in V_a(y) whenever a>=k+1. Its complete list is
exactly {(H,XH):deg H<k-1, agreement(H,W)>=a}. This remains true
when the degree-<n interpolant of XW involves reduction modulo P_D.

To see why gcd-root deletion matters, take a field of characteristic
>2, D={0,1,2}, k=1,a=2, and y_0=(1,0,0), y_1=0. The row (X,0)
has T_R=0 and lies in V_a(y). Dividing its gcd gives the row (1,0),
but the alleged divided received identity y_0=0 is false at x=0.
Formula (7) correctly gives J={0}. The actual pair (0,0) agrees
at the other two coordinates. Nonprimitive rows are valid inputs;
silently treating them as primitive received identities is not.
