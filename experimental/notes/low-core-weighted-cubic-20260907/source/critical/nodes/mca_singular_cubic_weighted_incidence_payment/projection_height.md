# A large projection kernel limits the primitive coefficient height

Let V be an s-dimensional subspace of F[X] of degree <K. Let A,B
be coprime, not both zero, and let d be the kernel dimension of
(v,w)->Av+Bw on VxV. If one multiplier is zero, the other is a
nonzero constant by primitivity: d=s and h=0. Hence assume AB!=0.

Put rho=A/B. Projection onto v identifies the kernel with

    H_1={v in V: rho*v in V}, dim H_1=d.

If d=s, multiplication by rho preserves the nonzero finite-dimensional
space V. Cayley--Hamilton makes rho algebraic over F. The constant
field of F(X) is F, so rho is constant; primitive A,B are constant
and h=0. This argument does not require F to be algebraically closed.

For d<s set c=s-d. Define

    H_j={v in V: rho^i*v in V for every 0<=i<=j}.

The map H_(j-1)->V/H_1 sending v to rho^(j-1)*v modulo H_1
has kernel H_j. Its target has dimension c, so

    dim H_j >= s-j*c.

For 1<=d<s, m_0=floor((s-1)/c) is positive and H_(m_0) is
nonzero. Choose v there. Both v and rho^m_0*v are polynomials of
degree <K. Coprimality forces B^m_0 to divide v. Write v=B^m_0*q;
then rho^m_0*v=A^m_0*q, q a nonzero polynomial. Therefore

    m_0*deg B+deg q<K, m_0*deg A+deg q<K,
    m_0*max(deg A,deg B)<=K-1.

This proves (H) without computing an intersection matrix. No conclusion
is taken from m_0=0 when d=0. On s=11,J<=8655 the height bounds
for d=1,...,10 are respectively

    8654,8654,8654,8654,8654,4327,4327,2884,1730,865.

For d=11 the height is zero. The simple example
V=span{1,X^H,...,X^(10H)}, A=X^H, B=1, K=10H+1
has d=10 and attains 10*h=K-1. The dependence on kernel codimension
cannot simply be replaced by a constant-height assertion.

## Codimension one forces a full geometric-progression carrier

When d=s-1, the same proof gives a nonzero v in H_(s-1). Since
rho is nonconstant, v,rho*v,...,rho^(s-1)*v are F-linearly
independent and therefore form a basis of V. Write v=B^(s-1)*q.
Then the EXACT polynomial carrier is

    V=q*span_F{B^(s-1), A*B^(s-2), ..., A^(s-1)},
    deg q+(s-1)*h<K.                                (GP)

Coprimality of A,B means the displayed monomials have gcd one, so
the gcd of V is q up to a nonzero constant. On the normalized source's
COMPLETE joint-core union U, q is nonzero: otherwise V(x)=0 and a
represented pair agreeing there would give u(x)=h_*(x),v(x)=0,
contradicting the empty universal carrier core. Outside U, q may vanish;
those coordinates and their defect labels must remain in the accounting.
For the remaining d=10,s=11 case, this is a full length-eleven
geometric-progression carrier, not just a long chain inside V.
Roots of B cannot be deleted: the homogeneous monomial display
retains those coordinates. This does not replace the challenge field
or identify the received word as a function only of A/B.
