"""Tiny actual polynomial and partition controls; not universal proof certification."""

from fractions import Fraction as Q
import importlib.util
from itertools import combinations
from math import factorial, prod
from pathlib import Path

path = Path(__file__).resolve().parents[1]/"mca_fiber_contraction_core_basis_resource/verify.py"
spec = importlib.util.spec_from_file_location("contraction_controls", path)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
need, rank = c.check, c.rank


def product(d, k, r):
    if r == 1:
        return d+k
    return prod(d+k-Q(i*(k-1), r-1) for i in range(r))


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    for first in range(min(n, maximum or n), 0, -1):
        for rest in partitions(n-first, first):
            yield (first,)+rest


def moment_controls():
    count = 0
    for n in range(4, 15):
        for sizes in partitions(n):
            for r in range(2, min(5, len(sizes))+1):
                m = r-1
                if m*sizes[0] > n:
                    continue
                for k in range(max(r, sum(sizes[:m])+1), n):
                    need(m*sum(a*a for a in sizes) <= n*(k-1), "joint capped moment")
                    count += 1
    need(count > 0, "partition coverage")
    need(2*sum(a*a for a in (10,1,1,1)) > 13*11, "omitting fiber cap fails")
    for s in range(2, 20):
        need(max((s-j-1)*(j+1) for j in range(s-1)) == s*s//4, "hereditary coefficient")
    print("PASS", count, "joint-moment controls; missing cap rejected")


def actual(p, k, points, polys, equality=False):
    rows = c.rows_for(polys, points, p)
    n, s = len(rows), len(polys)
    need(n > k >= s and all(any(row) for row in rows) and rank(rows,p)==s,
         "actual nonzero polynomial space")
    flats = {(0, ()): ()}
    for j in range(1, s):
        for indices in combinations(range(n), j):
            basis = [rows[i] for i in indices]
            if rank(basis,p) != j:
                continue
            closure = tuple(i for i,row in enumerate(rows) if rank(basis+[row],p)==j)
            flats.setdefault((j,closure), indices)
    h = max(Q(len(inside),j) for j,inside in flats if j)
    need((s*s//4)*h <= n, "actual proper-flat density")
    count = 0
    for (j,inside), indices in flats.items():
        r, kk = s-j, k-len(inside)
        if r < 2:
            continue
        basis = [rows[i] for i in indices]
        outside = [i for i in range(n) if i not in inside]
        fibers = set()
        for x in outside:
            fibers.add(tuple(y for y in outside if rank(basis+[rows[x],rows[y]],p)==j+1))
        sizes = sorted(map(len,fibers),reverse=True)
        nn = len(outside)
        need(sum(sizes)==nn and (r-1)*sizes[0]<=nn, "actual child fiber cap")
        need(sum(sizes[:r-1])<=kk-1, "actual top-fiber root capacity")
        need((r-1)*sum(a*a for a in sizes)<=nn*(kk-1), "actual hereditary moment")
        bases = factorial(r)*sum(rank(basis+[rows[i] for i in chosen],p)==s
                                for chosen in combinations(outside,r))
        lower = product(n-k,kk,r)
        need(bases>=lower, "actual contracted product bound")
        if equality:
            need(bases==lower, "repeated-fiber equality in every descendant")
        count += 1
    print("PASS actual",(p,k,n,s),"density",h,"descendants",count,
          "bases",c.basis_count(rows,p,s))


def main():
    moment_controls()
    mono = lambda k,powers: [tuple(int(i==power) for i in range(k)) for power in powers]
    actual(17,4,list(range(9)),mono(4,range(4)),True)
    actual(23,7,[x%23 for x in range(-8,9) if x],mono(7,(0,2,4,6)),True)
    actual(17,5,list(range(13)),mono(5,(0,1,4)))
    loc = c.locator(range(10),17)
    polys = [[1]+[0]*11,loc+[0],[0]+loc]
    rows = c.rows_for(polys,list(range(13)),17)
    bases = c.basis_count(rows,17,3)
    need(bases<=186<product(1,12,3), "actual unqualified-product counterexample")
    print("PASS actual omitted-density counterexample: bases",bases,"candidate",product(1,12,3))
    rows = c.rows_for([polys[0],[0,1]+[0]*10,polys[1],polys[2]],list(range(13)),17)
    need(all(rank([x,y],17)==2 for x,y in combinations(rows,2)), "root fibers all singletons")
    fibers = {tuple(y for y in range(1,13) if rank([rows[0],rows[x],rows[y]],17)==2)
              for x in range(1,13)}
    sizes = sorted(map(len,fibers),reverse=True)
    need(sizes==[9,1,1,1] and 2*sum(a*a for a in sizes)>12*10,
         "root fiber cap alone does not give the hereditary moment")
    print("PASS actual all-flat guard: singleton root fibers, child moment fails")
    print("Controls supplement the hand proof; no unsafe MCA line or row closure")


if __name__ == "__main__":
    main()
