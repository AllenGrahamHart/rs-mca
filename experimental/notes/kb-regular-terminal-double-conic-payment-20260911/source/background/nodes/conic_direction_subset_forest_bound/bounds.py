"""Exact sufficient graph edge bounds and hypergeometric resources."""
from fractions import Fraction as Q
from math import comb


def choose(n, k):
    return comb(n, k) if n >= k >= 0 else 0


def phi(s, d):
    return choose(d, 3)-2*choose(d, 2)+(s-2)*d


def psi(s, x):
    if x <= 5:
        return (s-4)*x
    d = x.numerator//x.denominator
    return phi(s, d)+(x-d)*(phi(s, d+1)-phi(s, d))


def edge_bound(s):
    if s < 2:
        raise ValueError("at least two vertices required")
    if s <= 5:
        return s*s//4
    for edges in range(s*s//4, -1, -1):
        if s*psi(s, Q(2*edges, s)) <= 2*comb(s, 3):
            return edges
    raise ValueError("no sufficient edge bound")


def averaging_cost(m, s, r):
    if not 2 <= s <= m or not 0 <= r <= m:
        raise ValueError("subset parameters")
    return Q(s*r, m)-1+Q(choose(m-r, s), comb(m, s))
