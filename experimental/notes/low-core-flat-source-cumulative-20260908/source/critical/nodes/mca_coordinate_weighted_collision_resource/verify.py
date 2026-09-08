"""Exact weighted-resource formulas and small actual-polynomial controls."""

from fractions import Fraction as F
import importlib.util
from itertools import combinations, product
from math import comb, factorial, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name, node):
    spec = importlib.util.spec_from_file_location(name, ROOT/node/"verify.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


p = load("weighted_original_profile", "mca_rank_profile_density_basis_product")
c = load("weighted_collision", "mca_fiber_collision_bonferroni_resource")


def need(ok, why):
    if not ok:
        raise ValueError(why)


def source_cap(n, K, s):
    need(n > K >= s >= 3, "polynomial source collision scope")
    return max(F(n*(K-s), s-1), F((K-s+1)*(K-s))).__floor__()


def credit(n0, n1, r, A, Tstar):
    need(n1 >= n0 >= r >= 4 and A >= 2 and Tstar >= 0, "source-credit box")
    numerator = (comb(r, 2)*(n0-2)*(n0-3)
                 -3*comb(r, 3)*(A-2)*(n1-3)-3*comb(r, 4)*Tstar)
    need(numerator >= 0, "nonnegative uniform collision credit")
    return F(numerator, r*(n1-1)*(n1-2)*(n1-3))


def value_derivative(D, x, rank, mu):
    x = F(x)
    need(D >= 1 and x >= 1 and rank >= 2, "convex product domain")
    need(set(mu) >= set(range(3, rank+1))
         and all(0 <= mu[r] < 1 for r in range(3, rank+1)), "fixed convex profile")
    value, derivative = F(D+1), F(0)
    for i in range(2, rank+1):
        slope = prod(1-mu[r] for r in range(i+1, rank+1))
        factor = D+1+(x-1)*slope
        value, derivative = value*factor, derivative*factor+value*slope
    return value, derivative


def tangent(D, K0, rank, mu, Cmin, Cmax, C0, weight, G):
    Cmin, Cmax, C0, weight, G = map(F, (Cmin, Cmax, C0, weight, G))
    M = D+K0
    need(D >= 1 and K0 >= rank >= 3 and 0 <= Cmin <= Cmax
         and Cmin <= C0 <= Cmax and weight >= 0 and G > 0,
         "weighted tangent parameters")
    need(K0-1-Cmax/M >= 1, "whole collision interval in convex domain")
    value, derivative = value_derivative(D, K0-1-C0/M, rank-1, mu)
    coefficient = weight*rank*G-derivative
    endpoint = Cmin if coefficient >= 0 else Cmax
    return M*value+C0*derivative+coefficient*endpoint


def exact_weighted_histogram(sizes, r):
    unweighted, marked = [1]+[0]*r, [0]*(r+1)
    for a in sizes:
        for j in range(r, 0, -1):
            marked[j] += a*marked[j-1]+a*(a-1)*unweighted[j-1]
            unweighted[j] += a*unweighted[j-1]
    return factorial(r)*unweighted[r], factorial(r)*marked[r]


def main():
    histograms = 0
    for length in range(1, 6):
        for sizes in product(range(1, 4), repeat=length):
            for z in (0, 2):
                n = 64
                padded = (*sizes, *([1]*(n-z-sum(sizes))))
                T, A = sum(a*(a-1) for a in padded), max(2, max(padded))
                for r in (4, 5):
                    lam = credit(n, n, r, A, max(T, 20))
                    exact, marked = exact_weighted_histogram(padded, r)
                    envelope = c.resource(n, r, A, T)+lam*r*T*c.falling(n-1, r-1)
                    need(exact+lam*marked <= envelope <= c.falling(n, r),
                         "weighted histogram and funded envelope")
                    histograms += 1
    exact, marked = exact_weighted_histogram((2, *([1]*8)), 4)
    need((exact, marked) == (4368, 2688) and exact+marked > c.falling(10, 4),
         "unfunded large weights fail even on a small histogram")
    for n0, n1 in ((64, 64), (64, 67)):
        lam = credit(n0, n1, 5, 3, 32)
        for n in (n0, n1):
            for T in (0, 8, 32):
                need(c.resource(n, 5, 3, T)+lam*5*T*c.falling(n-1, 4)
                     <= c.falling(n, 5), "whole-box endpoints")

    b = load("weighted_actual_geometry", "mca_balanced_basis_under_flat_density")
    mono = lambda k, powers: [tuple(int(i == v) for i in range(k)) for v in powers]
    loc = b.c.locator(range(10), 17)
    big = [[1]+[0]*11, loc+[0], [0]+loc]
    fixtures = [(17, 4, list(range(9)), mono(4, range(4))),
                (23, 7, [x % 23 for x in range(-8, 9) if x], mono(7, (0, 2, 4, 6))),
                (17, 12, list(range(13)), big)]
    tangents, signs = 0, set()
    for field, K, points, polys in fixtures:
        rows = b.c.rows_for(polys, points, field)
        M, s, D = len(rows), len(polys), len(rows)-K
        flats = set()
        for t in range(1, s):
            for chosen in combinations(range(M), t):
                basis = [rows[i] for i in chosen]
                if b.rank(basis, field) == t:
                    flat = tuple(i for i, row in enumerate(rows)
                                 if b.rank(basis+[row], field) == t)
                    flats.add((t, flat))
        h = max(F(len(flat), t) for t, flat in flats)
        fibers = [flat for t, flat in flats if t == 1]
        weights = {i: len(flat)-1 for flat in fibers for i in flat}
        C = sum(weights.values())
        need(C <= source_cap(M, K, s), "polynomial source collision cap")
        bases = [chosen for chosen in combinations(range(M), s)
                 if b.rank([rows[i] for i in chosen], field) == s]
        exact = factorial(s)*len(bases)
        marked = factorial(s)*sum(sum(weights[i] for i in chosen) for chosen in bases)
        mu = p.profile(D, K, K, s, h)
        G = p.product(D, K-h, s-1, mu)
        need(marked >= s*C*G, "marked original core bases")
        Cmax = M*(h-1)
        if (K, s) == (12, 3):
            need((C, exact, marked) == (90, 186, 1620)
                 and marked == s*C*G < (s+1)*C*G,
                 "attained marked bound; extra basis position is false")
        for weight in (F(0), F(1)):
            for i in range(5):
                point = Cmax*i/4
                lower = tangent(D, K, s, mu, 0, Cmax, point, weight, G)
                _, derivative = value_derivative(D, K-1-point/M, s-1, mu)
                signs.add(weight*s*G >= derivative)
                need(lower <= exact+weight*marked, "actual weighted basis lower count")
                for j in range(5):
                    value = Cmax*j/4
                    exact_product = M*p.product(D, K-1-value/M, s-1, mu)+weight*s*value*G
                    need(lower <= exact_product, "correct tangent endpoint across collision interval")
                    tangents += 1
        print("ACTUAL", field, K, M, s, "C", C, "bases", exact, "marked", marked, flush=True)
    need(signs == {False, True}, "both tangent coefficient signs tested")
    for action in (lambda: credit(12, 12, 12, 12, 100),
                   lambda: source_cap(8, 8, 3),
                   lambda: value_derivative(1, F(1, 2), 2, {}),
                   lambda: tangent(1, 12, 3, {3: F(1, 2)}, 0, 1000, 0, 0, 6)):
        try:
            action()
        except ValueError:
            pass
        else:
            raise ValueError("accepted invalid weighted-resource guard")
    print("PASS", histograms, "weighted histograms;", tangents,
          "tangent controls; attained marked bound; two false variants; four guards")


if __name__ == "__main__":
    main()
