# Polynomial coefficients and interpolation guards

## 1. An actual weighted graph beyond constant-coefficient parabolas

Use the field F=F_787(beta), beta^2=2, and P=X+beta from
`controls.md`. Now use D={1,...,783}, K=4, m=30, d=26, T=1,
h_*=0 and V=span{P,X*P^2}. Split D into 27 consecutive groups
of 29 points. On group j the received pair equals

    f_j=(j*P, j^2*X*P^2).

All pairs satisfy b=X*a^2. Their complete cores are their groups.
For x in group j and i!=j, the unique extra-agreement direction is

    gamma=-1/((i+j)*x*(x+beta)).                         (1)

All 783*26=20358 such labels are distinct. Equality of denominators
s*x*(x+beta)=s'*x'*(x'+beta), with nonzero x,x', first gives
sx=s'x' from beta coefficients and sx^2=s'x'^2 from constant
coefficients. Thus x=x', s=s', j=j' and i=i'.

The function x*(x+beta) is injective on E: a collision at different
x,x' would force beta=-(x+x') in E. Every carrier explanation not
equal to a source-piece explanation has at most one agreement per group
after division by P. Hence it has at most 27<30 agreements. Each
printed label has just one eligible carrier explanation with a 29-point
core and one defect. A degree-<4 containing polynomial is pinned by
those core points and fails at the defect. Thus all-explanation maximum
raw is one, 2T<d holds, and all 27 pairs are represented. The census
is for explanations in the FIXED carrier, not the full ambient code.

These pairs are not mapped to b=a^2 by any constant GL_2(F) matrix
and polynomial offset, even if the offset degree is unrestricted.
Suppose its first and second rows are (A,B) and (C,D), with offsets
u_0,v_0. For each parameter t=1,...,27 one would have

    C*t*P+D*t^2*X*P^2+v_0
       =(A*t*P+B*t^2*X*P^2+u_0)^2.

As a polynomial in t over F(X), the difference has degree <=4 and
27 distinct roots, so every coefficient vanishes. The t^4 coefficient
forces B=0. The t^2 coefficient then forces D*X=A^2. Constants
A,D can satisfy this polynomial identity only when A=D=0, contradicting
invertibility. Thus the extension in polynomial X-coefficients is strict
relative to the previous constant-matrix parabola hypothesis on an ACTUAL
canonical source. No claim is made that this example escaped every other
previously paid source class or that it is a deployed unsafe witness.

## 2. The characteristic must not divide the graph degree

In characteristic three use V=span{1,X,X^3,X^9}, dimension four.
Every a=c_0+c_1*X+c_2*X^3 has a^3=c_0^3+c_1^3*X^3+c_2^3*X^9
in V. This is a dimension-three family, exceeding floor(4/2)=2.
Odd characteristic alone therefore does not validate the cubic theorem.
The hypothesis that e is nonzero in F is necessary for the stated bound.

## 3. A received graph fit is not a polynomial pair identity

Over F_5 take K=2,m=4,T=1, V=span{1}, h_*=0 and domain 0,1,2,3.
Let (u,v)=(1,0) on 0,1,2 and (0,1) at 3. At gamma=1, h=1
has a full-code-bad four-point support and minimum raw one. Its minimizing
pair is (a,b)=(1,0), with complete core {0,1,2}.

Put L(X)=X(X-1)(X-2), P_D(X)=X(X-1)(X-2)(X-3), and

    Psi(X,Y)=L(X)+P_D(X)*Y^2.

At EVERY domain point, Psi(x,u(x))=v(x), since P_D vanishes there
and L interpolates v. But Psi(X,1)=L+P_D is a nonzero degree-four
polynomial, not b=0. The weighted certificate degree is six, exceeding
m-T-1=2. This actual LOW record falsifies inferring the polynomial
identity from a pointwise graph fit without its printed degree guard.

The verifier uses exact small fields and polynomial arithmetic only. The
nonexistence of every constant GL_2 transform is proved by the coefficient
argument above, not by enumerating field matrices.
