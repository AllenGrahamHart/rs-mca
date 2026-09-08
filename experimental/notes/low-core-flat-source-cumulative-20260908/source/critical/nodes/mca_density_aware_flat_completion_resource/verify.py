"""Small actual polynomial controls, not a field-scale search or formal proof."""

from fractions import Fraction as Q
import importlib.util
from itertools import combinations
from math import comb, factorial, prod
from pathlib import Path


path = Path(__file__).resolve().parents[1]/"mca_maximum_density_flat_core_basis_resource/verify.py"
spec = importlib.util.spec_from_file_location("basis_controls", path)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
need, rank = base.check, base.rank


def control(s, j, a, t):
    p, ell = 37, s-j
    K, M = a+ell, 2*a+ell
    c, h = M-K+1, Q(a, j)
    inside, outside = tuple(range(t)), tuple(range(a, a+M-t))
    core = inside+outside
    def vector(x):
        locator = prod(x-y for y in range(a)) % p
        return tuple(pow(x, i, p) for i in range(j))+tuple(locator*pow(x, i, p)%p for i in range(ell))
    vectors = {x: vector(x) for x in range(a+M)}
    need(max(a+ell-1, j-1) < K and rank([vectors[x] for x in core], p) == s, "actual rank and degree")
    need(rank([vectors[x] for x in range(a)], p) == j and a < c, "actual flat and positive completion")
    # Low monomials make any <=j points independent; higher flats obey K-s+i.
    need(all(Q(K-s+i, i) <= h for i in range(j, s)), "global maximum-density guard")
    actual = [0]*(j+1)
    for points in combinations(core, s):
        if rank([vectors[x] for x in points], p) == s:
            actual[sum(x < a for x in points)] += factorial(s)
    qout = prod(len(outside)-i for i in range(ell))
    factors = [max(c+i, M-(s-1-i)*h) for i in range(j)]
    E, Y, sums = [], [], []
    for b in range(j+1):
        eb = yb = 0
        rb = Q(0)
        for points in combinations(inside, b):
            rows = [vectors[x] for x in points]
            if rank(rows, p) != b:
                continue
            y = sum(rank(rows+[vectors[x]], p) > b for x in inside)
            eb += factorial(b)
            yb += factorial(b)*y
            rb += factorial(b)*prod(x-y for x in factors[:j-b])
        E.append(eb)
        Y.append(yb)
        sums.append(rb)
        need(qout*comb(s,b)*rb <= actual[b], "disjoint completion class")
    need(Y == E[1:]+[0], "exact inside-extension identity")
    for b in range(1, j):
        need(max(t-b*h,0)*E[b] <= E[b+1] <= max(t-b,0)*E[b], "coupled ratios")
    bracket = sum(comb(s,b)*sums[b] for b in range(j+1))
    for alpha in range(5):
        q, last, coefficients = Q(alpha*t,4), Q(0), []
        for b in range(1,j+1):
            values = [x-q for x in factors[:j-b]]
            derivative = sum(prod(values[i] for i in range(len(values)) if i!=v) for v in range(len(values)))
            coefficients.append(comb(s,b)*(prod(values)+q*derivative)-last)
            last = comb(s,b)*derivative
        signed = prod(x-t for x in factors)+sum(coefficients[b-1]*E[b] for b in range(1,j+1))
        tail = coefficients[-1]
        for b in range(j-1,0,-1):
            tail = coefficients[b-1]+tail*(max(t-b*h,0) if tail>=0 else max(t-b,0))
        reduced = prod(x-t for x in factors)+t*tail
        need(reduced <= signed <= bracket, "convex tangent and backward elimination")
    print("PASS actual source", (s,j,a,t), "ordered bases", sum(actual), "completion", qout*bracket)


def main():
    for s,j,a in ((4,1,2),(5,2,3),(6,3,4)):
        for t in (0,1,a):
            control(s,j,a,t)
    E1,E2,h = 3,6,Q(3,2)
    need(-(3-h)*E1 > -E2, "wrong lower ratio with negative coefficient must fail")
    need(-max(3-1,0)*E1 == -E2, "correct upper ratio is sharp")
    print("PASS: 9 actual sources; 45 tangent controls; wrong signed-ratio shortcut rejected")


if __name__ == "__main__":
    main()
