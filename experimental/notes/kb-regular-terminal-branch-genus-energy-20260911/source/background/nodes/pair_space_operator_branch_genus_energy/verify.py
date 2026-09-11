"""Small exact branch-energy controls; no official source census."""
from fractions import Fraction as Q
from itertools import product


def need(ok, why):
    if not ok:
        raise ValueError(why)


def energy(n, nu, g, pairs):
    return (n+2*nu*g)*(n+8*nu*pairs)


def abstract_controls():
    checked = 0
    for nu in (1, 2, 3):
        for rows in product(((1, 0), (1, 1), (1, 2), (2, 1), (2, 3), (3, 2)), repeat=3):
            for shrink in (0, 1):
                fibres = [(b, max(0, nu*b-shrink), r) for b, r in rows]
                n = sum(l for b, l, r in fibres)
                s = sum(l*r for b, l, r in fibres)
                pairs = sum(r*(r-1)//2 for b, l, r in fibres)
                g = sum(b*(b-1)//2 for b, l, r in fibres)
                left = sum(Q(l, b)*(Q(r)-Q(1, 2))**2 for b, l, r in fibres)
                need(left <= 2*nu*pairs+Q(n, 4), "weighted second factor")
                need(sum(l*b for b, l, r in fibres) <= n+2*nu*g, "branch first factor")
                if 2*s > n:
                    need((2*s-n)**2 <= energy(n, nu, g, pairs), "branch energy")
                checked += 1
    return checked


def conic(s):
    p = 97
    domain = [x for x in range(p) if pow(x, s, p) == 1]
    # Coefficients in (1,Z,Z^2); T is d/dZ, not differentiation in X.
    family = [(0, 0, 0), (1, -2, 1), (2, -4, 2)]
    total = 0
    for x in domain:
        z = pow(x, s, p)
        total += sum((a+b*z+c*z*z) % p == 0 and (b+2*c*z) % p == 0
                     for a, b, c in family)
    n, m = len(domain), len(family)
    need(n == s and total == m*n, "actual composed conic collision")
    need((2*total-n)**2 == energy(n, s, 0, m*(m-1)//2), "sharp smooth energy")
    return n, total


def multiple_branch(branches, s):
    p = 97
    roots = (-1, 1) if branches == 2 else (-1, 0, 1)
    # U=(1,f(Z),Z*f(Z)), T cycles this basis; y=f, Ty=Z*f.
    # The point (1,0,0) has distinct tangents with slopes in roots.
    # Z=Y/X off that point, so the image has degree branches+1, nu=s.
    def f(z):
        value = 1
        for root in roots:
            value = value*(z-root) % p
        return value
    domain = [x for x in range(p) if f(pow(x, s, p)) == 0]
    incidences = sum(1+int(f(pow(x, s, p)) == 0
                           and pow(x, s, p)*f(pow(x, s, p)) % p == 0) for x in domain)
    n, g = len(domain), branches*(branches-1)//2
    need(n <= s*branches and incidences == 2*n, "actual singular complete cores")
    need((2*incidences-n)**2 <= energy(n, s, g, 1), "singular energy")
    if branches == 2:
        need(n == 2*s > s, "normalization degree alone is not a fibre cap")
        need((2*incidences-n)**2 > energy(n, s, 0, 1), "omitted branch budget falsified")
    if branches == 3 and s == 1:
        need((2*incidences-n)**2 > energy(n, s, branches-1, 1),
             "linear branch budget falsified")
    return n, incidences, g


def main():
    print("PASS", abstract_controls(), "weighted branch-energy configurations")
    print("PASS sharp actual conic controls", conic(1), conic(3))
    print("PASS actual nodal fibres", multiple_branch(2, 1), multiple_branch(2, 3))
    print("PASS ordinary triple branch and ramified composition",
          multiple_branch(3, 1), multiple_branch(3, 3))
    print("Removing singular branches or replacing their quadratic budget is refuted")
    print("Universal normalization and actual-owner geometry remain written proofs")


if __name__ == "__main__":
    main()
