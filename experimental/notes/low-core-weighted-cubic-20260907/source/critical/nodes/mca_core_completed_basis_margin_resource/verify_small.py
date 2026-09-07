"""Tiny exact weight and actual incidence-basis controls."""

from fractions import Fraction as Q
from itertools import permutations
from math import prod


def weight(s, d, m_minus_g, r):
    old = min(d+1, r)
    new = (s+1)*r*Q(m_minus_g-r, m_minus_g)*prod(
        Q(d-r+i, d+i) for i in range(1, s)) if r <= d else Q(0)
    return max(old, new)


def determinant(rows, p):
    a, b, c = rows
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0])) % p


def verify():
    checks = 0
    for s in range(1, 10):
        for d in (s*(s+1), s*(s+1)+3, 67472):
            alpha = Q((s+1)*d, d+s)
            for extra in (0, 1, 17):
                for r in tuple(range(1, s+2)) + (d, d+1, d+7):
                    assert weight(s, d, d+s+extra, r) >= alpha
                    checks += 1
            assert weight(s, d, d+s, 1) == alpha

    # K=s=2, d=7, m=9. Eight shared zero-pair points and three outsiders.
    p, n, m, s, d = 17, 11, 9, 2, 7
    core = set(range(8))
    u = [0]*8 + [-1 % p, -2 % p, -3 % p]
    v = [0]*8 + [1, 1, 1]
    normals = [(v[x], -1 % p, -x % p) for x in range(n)]
    owned = set()
    for outsider in (8, 9, 10):
        gamma = outsider-7
        support = core | {outsider}
        assert all((u[x]+gamma*v[x]) % p == 0 for x in support)
        assert len(core) >= 2 and v[outsider] == 1  # Full-code pair badness.
        raw = min(sum(v[x] != (a+b*x) % p for x in support)
                  for a in range(p) for b in range(p))
        assert raw == 1
        bases = {points for points in permutations(sorted(support), s+1)
                 if determinant([normals[x] for x in points], p)}
        assert len(bases) == (s+1)*(m-1)*(m-2) == 168
        assert all(len(set(points)-core) == 1 for points in bases)
        assert owned.isdisjoint(bases)
        owned |= bases
        old = m*(d+1)*raw
        assert Q(len(bases), old) == Q((s+1)*d, d+s)
        assert old+len(bases) > len(bases)  # Reject adding overlapping lower bounds.
    assert len(owned) == 504 <= n*(n-1)*(n-2)
    print("PASS:", checks, "exact weight checks; sharp alpha factors")
    print("PASS: three actual full-code-bad supports, 168 bases each, 504 disjoint tuples")
    print("PASS: adding the old and new tuple lower bounds is rejected")


if __name__ == "__main__":
    verify()
