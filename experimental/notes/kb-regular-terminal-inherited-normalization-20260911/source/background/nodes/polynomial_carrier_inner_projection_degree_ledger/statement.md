# Actual Anchor Paths Have A Normalization-Degree Ledger

Work over a perfect field F, in particular the original finite field.
Let V_j be the shared polynomial carrier along a regular joint-anchor path,
after removing its FULL homogeneous fixed divisor. Its actual degree is D_j,
dimension s_j, algebraic image C_j subset P^(s_j-1) has degree eta_j, and
the map P1 to its normalization has degree nu_j. Then D_j=nu_j*eta_j
and eta_j>=s_j-1. These are algebraic images, not finite attained sets.
The ledger applies while parent and child images are nonconstant
(s_j,s_(j+1)>=2); the application stops at shared dimension3.

At a retained anchor x, its nonzero evaluation defines p in C_j. The child
carrier is the hyperplanes through p, followed by full fixed-divisor removal.
Let mu_j be the degree of this inner projection on the normalization, and
m_j the degree of its fixed divisor there. Then

    nu_(j+1)=nu_j*mu_j,
    eta_j=m_j+mu_j*eta_(j+1),
    D_(j+1)=D_j-nu_j*m_j.

In particular m_j>=b(p)>=1, where b(p) counts geometric branches. The
identities include fixed divisors at infinity, ramification and singular
fibres. They do not reset original owners, weights or agreement counts.

For an original dimension11 carrier of degree at most J-1, nu_0<=floor((J-1)/10).
After eight regular anchors, if nu_8 exceeds that bound then at least one
ACTUAL anchor has mu_j>=2: its inner projection is nonbirational. Merely
asserting that a generic projection is birational does not rule this out.
The exact telescope is D_0=D_8+sum_(j=0)^7 nu_j*m_j.
