"""Small exact switching controls and the sharp one-doubleton family."""

from fractions import Fraction as F
from itertools import permutations, product
from math import factorial, prod


def need(ok, why):
    if not ok:
        raise ValueError(why)


def coefficient(n, r):
    need(n > r >= 2, "strict source length/rank guard")
    return F(r-1, 2*(n-r))


def counts(sizes, r):
    e, m = [1]+[0]*r, [0]*(r+1)
    for a in sizes:
        for j in range(r, 0, -1):
            m[j] += a*m[j-1]+a*(a-1)*e[j-1]
            e[j] += a*e[j-1]
    return factorial(r)*e[r], factorial(r)*m[r]


def actual_switches(sizes, r):
    fibers = [i for i, a in enumerate(sizes) for _ in range(a)]
    n = len(fibers)
    incoming, good, marked = {}, 0, 0
    for v in permutations(range(n), r):
        if len({fibers[x] for x in v}) != r:
            continue
        good += 1
        marked += sum(sizes[fibers[x]]-1 for x in v)
        for i in range(r):
            for y in range(n):
                if y == v[i] or fibers[y] != fibers[v[i]]:
                    continue
                for j in range(r):
                    if j == i:
                        continue
                    b = (*v[:j], y, *v[j+1:])
                    need(len(set(b)) == r, "switch keeps distinct coordinates")
                    incoming[b] = incoming.get(b, 0)+1
    need((good, marked) == counts(sizes, r), "symmetric and tuple counts agree")
    pairs = 0
    for b in permutations(range(n), r):
        multiplicity = sorted([sum(fibers[x] == i for x in b)
                               for i in {fibers[x] for x in b}])
        if multiplicity != [1]*(r-2)+[2]:
            need(b not in incoming, "only one repeated pair is produced")
            continue
        union_size = sum(sizes[i] for i in {fibers[x] for x in b})
        need(incoming.get(b, 0) == 2*(n-union_size), "exact incoming switch multiplicity")
        pairs += 1
    need(sum(incoming.values()) == (r-1)*marked <= 2*(n-r)*pairs,
         "both sides of switching incidence count")
    return len(incoming)


def main():
    cases = 0
    for length in range(1, 7):
        for sizes in product(range(1, 4), repeat=length):
            n = sum(sizes)
            for r in range(2, min(n, 6)):
                good, marked = counts(sizes, r)
                need(good+coefficient(n, r)*marked <= prod(n-i for i in range(r)),
                     "all-partition weighted resource")
                cases += 1
    sharp = 0
    for r in range(2, 9):
        for n in range(r+1, 41):
            good, marked = counts((2, *([1]*(n-2))), r)
            full = prod(n-i for i in range(r))
            lam = coefficient(n, r)
            need(marked > 0 and good+lam*marked == full, "exact sharpness family")
            need(good+(lam+F(1, 10**9))*marked > full, "larger coefficient is false")
            sharp += 1
    switched = sum(actual_switches(sizes, r) for sizes, r in
                   (((2, 1, 1, 1), 3), ((2, 2, 1, 1), 4), ((3, 1, 1, 1), 3)))
    rows = [(1, x*(x-1) % 17, x*x*(x-1) % 17) for x in range(8)]
    need(rows[0] == rows[1] and len(set(rows)) == 7, "actual polynomial sharp partition")
    need((rows[2][1]*rows[3][2]-rows[2][2]*rows[3][1]) % 17 != 0,
         "actual carrier rank three")
    need(coefficient(1010, 12) <= coefficient(1000, 12), "whole-box direction")
    for args in ((4, 4), (3, 4), (4, 1)):
        try:
            coefficient(*args)
        except ValueError:
            pass
        else:
            raise ValueError("accepted invalid switching coefficient")
    print("PASS", cases, "histogram cases;", sharp, "sharp partitions and larger-credit falsifiers")
    print("PASS", switched, "actual switch targets; actual F17 polynomial source; three guards")
    print("Sharp resource relaxation, NOT a sharp MCA row or unsafe received line")


if __name__ == "__main__":
    main()
