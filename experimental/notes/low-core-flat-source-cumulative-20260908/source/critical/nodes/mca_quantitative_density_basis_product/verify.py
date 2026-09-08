"""Exact product and small actual contraction controls for quantitative density."""

from fractions import Fraction as F
import importlib.util
from itertools import combinations
from math import factorial, prod
from pathlib import Path

path = Path(__file__).resolve().parents[1]/"mca_balanced_basis_under_flat_density/verify.py"
spec = importlib.util.spec_from_file_location("balanced_controls", path)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
need, rank = b.need, b.rank


def product(gap, degree, dimension, inflation):
    need(gap > 0 and degree >= 1 and dimension >= 1 and 1 <= inflation <= 2,
         "positive product scope")
    if dimension == 1:
        return F(gap+degree)
    argument, value = F(degree), F(gap+1)
    for r in range(dimension, 1, -1):
        value *= gap+argument
        if r >= 3:
            argument = 1+(1-F(inflation, r-1))*(argument-1)
    return value


def partitions():
    count = 0
    for n in range(4, 15):
        for sizes in b.partitions(n):
            for r in range(2, min(5, len(sizes))+1):
                for k in range(max(r, sum(sizes[:r-1])+1), n):
                    bound = (k-1)*max(F(n, r-1), sizes[0])
                    need(sum(a*a for a in sizes) <= bound, "quantitative capped moment")
                    count += 1
    need(2*sum(x*x for x in (10,1,1,1)) > 13*11,
         "balanced moment without loss is false")
    print("PASS", count, "quantitative partition moments; omitted loss rejected")


def actual(p, k, points, polys):
    rows = b.c.rows_for(polys, points, p)
    n, s = len(rows), len(polys)
    need(n > k >= s and rank(rows,p) == s and all(any(row) for row in rows), "actual source")
    flats = {(0, ()): ()}
    for j in range(1, s):
        for indices in combinations(range(n), j):
            basis = [rows[i] for i in indices]
            if rank(basis,p) != j:
                continue
            closed = tuple(i for i,row in enumerate(rows) if rank(basis+[row],p) == j)
            flats.setdefault((j,closed), indices)
    h = max(F(len(a),j) for j,a in flats if j)
    inflation = max(F(1), F(s*s//4)*h/n)
    need(inflation <= 2, "actual source within quantitative guard")
    count = 0
    for (j,inside),indices in flats.items():
        r, kk, nn = s-j, k-len(inside), n-len(inside)
        basis = [rows[i] for i in indices]
        outside = [i for i in range(n) if i not in inside]
        if r >= 2:
            fibers = {tuple(y for y in outside if rank(basis+[rows[x],rows[y]],p) == j+1)
                      for x in outside}
            sizes = sorted(map(len,fibers),reverse=True)
            need(sum(sizes) == nn and sum(sizes[:r-1]) <= kk-1, "actual quotient partition and roots")
            moment = sum(a*a for a in sizes)
            if r >= 3:
                need((r-1)*sizes[0] <= inflation*nn, "same hereditary loss factor")
                need((r-1)*moment <= inflation*nn*(kk-1), "actual quantitative moment")
            else:
                need(nn*nn-moment >= nn*(n-k+1), "independent rank-two seed")
        bases = factorial(r)*sum(rank(basis+[rows[i] for i in chosen],p) == s
                                 for chosen in combinations(outside,r))
        need(bases >= product(n-k,kk,r,inflation), "all actual descendant products")
        count += 1
    print("PASS actual",(p,k,n,s),"density",h,"lambda",inflation,
          "descendants",count,"bases",b.c.basis_count(rows,p,s),
          "lower",product(n-k,k,s,inflation))
    return inflation > 1, count


def main():
    partitions()
    mono = lambda k,powers: [tuple(int(i == v) for i in range(k)) for v in powers]
    sources = [(17,4,list(range(9)),mono(4,range(4))),
               (23,7,[x%23 for x in range(-8,9) if x],mono(7,(0,2,4,6)))]
    loc = b.c.locator(range(10),17)
    p3 = [[1]+[0]*11,loc+[0],[0]+loc]
    sources += [(17,12,list(range(13)),p3),
                (17,12,list(range(13)),[p3[0],[0,1]+[0]*10,p3[1],p3[2]])]
    loc9 = b.c.locator(range(9),17)
    sources.append((17,11,list(range(13)),mono(11,(0,1,2))+[loc9+[0],[0]+loc9]))
    outcomes = [actual(*source) for source in sources]
    need(sum(nontrivial for nontrivial,_ in outcomes) >= 3, "quantitative rather than exact-gate cases")
    for r in range(2,12):
        for x in range(1,7):
            need(product(7,x,r,F(1)) == b.product(7,x,r), "exact balanced endpoint")
            values = [product(7,x,r,z) for z in (F(1),F(3,2),F(2))]
            need(values[0] >= values[1] >= values[2] > 0, "loss monotonicity")
            for z in (F(1),F(3,2),F(2)):
                value = (8*prod(8+(x-1)*prod(1-z/j for j in range(a,r))
                                for a in range(2,r+1)))
                need(product(7,x,r,z) == value, "independent unrolled product")
                need(product(7,x+2,r,z)-2*product(7,x+1,r,z)+product(7,x,r,z) >= 0,
                     "convexity controls")
    for z in (F(9,10),F(21,10)):
        try:
            product(7,4,4,z)
        except ValueError:
            pass
        else:
            raise ValueError("accepted unproved loss range")
    print("PASS exact lambda=1 identity, unrolled product, curvature and guard mutations")
    print("Controls supplement the hand proof; no received-word or MCA payment inferred")


if __name__ == "__main__":
    main()
