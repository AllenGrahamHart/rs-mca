"""Small actual polynomial flats, including nonmaximizers; no source search."""

from fractions import Fraction as F
import importlib.util
from itertools import combinations
from math import comb, factorial, prod
from pathlib import Path

path = Path(__file__).resolve().parents[1]/"mca_fiber_contraction_core_basis_resource/verify.py"
spec = importlib.util.spec_from_file_location("actual_polynomials", path)
actual = importlib.util.module_from_spec(spec)
spec.loader.exec_module(actual)
need, rank = actual.check, actual.rank


def test(p, k, points, powers):
    polynomials = [tuple(int(i == power) for i in range(k)) for power in powers]
    rows = actual.rows_for(polynomials, points, p)
    n, s = len(rows), len(polynomials)
    need(n > k >= s and rank(rows, p) == s and all(any(x) for x in rows),
         "actual nonzero polynomial source")
    flats = {}
    for t in range(1, s):
        for indices in combinations(range(n), t):
            basis = [rows[x] for x in indices]
            if rank(basis, p) != t:
                continue
            closed = tuple(x for x in range(n) if rank(basis+[rows[x]], p) == t)
            flats.setdefault((t, closed), basis)
    caps = {t: max(len(a) for (j, a) in flats if j == t) for t in range(1, s)}
    h = max(F(len(a), t) for t, a in flats)
    bases = actual.basis_count(rows, p, s)
    checked, nonmax, tangents = 0, 0, 0
    for (t, inside), basis in flats.items():
        b, ell = len(inside), s-t
        if b >= n-k+1:
            continue
        outside = [x for x in range(n) if x not in inside]
        q = factorial(ell)*sum(rank(basis+[rows[x] for x in subset], p) == s
                              for subset in combinations(outside, ell))
        qlower = (n-b)*prod(n-min(caps[t+i], k-s+t+i) for i in range(1, ell))
        need(q >= qlower > 0, "arbitrary flat quotient count")
        ds = [n-min(caps[s-1-i], k-1-i) for i in range(t)]
        inside_counts, bracket = [1], prod(x-b for x in ds)
        for i in range(1, t+1):
            count, total = 0, 0
            for subset in combinations(inside, i):
                chosen = [rows[x] for x in subset]
                if rank(chosen, p) != i:
                    continue
                y = sum(rank(chosen+[rows[x]], p) > i for x in inside)
                count += factorial(i)
                total += factorial(i)*prod(x-y for x in ds[:t-i])
            inside_counts.append(count)
            bracket += comb(s, i)*total
        need(q*bracket <= bases, "actual basis interleavings and no overcount")
        for mode in range(5):
            coeff, previous = [], F(0)
            for i in range(1, t+1):
                point = F(mode*b, 4)
                factors = [x-point for x in ds[:t-i]]
                slope = sum(prod(factors[z] for z in range(len(factors)) if z != v)
                            for v in range(len(factors)))
                coeff.append(comb(s, i)*(prod(factors)+point*slope)-previous)
                previous = comb(s, i)*slope
            tail = coeff[-1]
            for i in range(t-1, 0, -1):
                lower, upper = max(b-caps[i], 0), max(b-i, 0)
                need(lower*inside_counts[i] <= inside_counts[i+1]
                     <= upper*inside_counts[i], "actual extension ratios")
                tail = coeff[i-1]+tail*(lower if tail >= 0 else upper)
            bound = prod(x-b for x in ds)+b*tail
            need(bound <= bracket and qlower*max(bound, 0) <= bases,
                 "signed tangent lower count")
            tangents += 1
        nonmax += F(b, t) < h
        checked += 1
    print("PASS actual", (p,k,n,s), "flats", checked, "nonmaximizers", nonmax,
          "tangent controls", tangents)
    return checked, nonmax


def main():
    results = [test(17,4,list(range(9)),(0,1,2,3)),
               test(23,7,[x%23 for x in range(-8,9) if x],(0,2,4,6)),
               test(17,5,list(range(13)),(0,1,4))]
    need(sum(x for x,y in results) > 0 and sum(y for x,y in results) > 0,
         "nonmaximum actual flats exercised")
    print("Actual controls supplement the arbitrary-flat hand proof")


if __name__ == "__main__":
    main()
