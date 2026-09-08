"""Exact rank-profile formula and small actual-polynomial controls."""

from fractions import Fraction as F
import importlib.util
from itertools import combinations
from math import factorial, prod
from pathlib import Path


def need(ok, why):
    if not ok:
        raise ValueError(why)


def profile(gap, low, high, dimension, density):
    need(gap >= 1 and high >= low >= dimension >= 2 and density >= 1,
         "rank/degree/density box")
    values = {}
    for r in range(3, dimension+1):
        j = dimension-r
        root = F(high-dimension+1, gap+high-dimension+r)
        local = F((j+1)*density-j, gap+low-j)
        values[r] = max(F(1, r-1), min(root, local))
        need(F(1, r-1) <= values[r] < 1, "positive rank coefficient")
    return values


def product(gap, argument, dimension, values):
    need(gap >= 1 and argument >= 1 and dimension >= 2, "product domain")
    need(set(values) >= set(range(3, dimension+1)), "complete rank profile")
    x, result = F(argument), F(gap+1)
    for r in range(dimension, 1, -1):
        result *= gap+x
        if r >= 3:
            need(0 <= values[r] <= 1, "convex product coefficient")
            x = 1+(1-values[r])*(x-1)
    return result


def bound(gap, low, high, dimension, density):
    return product(gap, low, dimension, profile(gap, low, high, dimension, density))


def main():
    path = Path(__file__).resolve().parents[1]/"mca_quantitative_density_basis_product/verify.py"
    spec = importlib.util.spec_from_file_location("older_controls",path)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    b = old.b
    rank = b.rank
    mono = lambda k,powers: [tuple(int(i == v) for i in range(k)) for v in powers]
    sources = [(17,4,list(range(9)),mono(4,range(4))),
               (23,7,[x%23 for x in range(-8,9) if x],mono(7,(0,2,4,6)))]
    loc = b.c.locator(range(10),17)
    p3 = [[1]+[0]*11,loc+[0],[0]+loc]
    sources += [(17,12,list(range(13)),p3),
                (17,12,list(range(13)),[p3[0],[0,1]+[0]*10,p3[1],p3[2]])]
    loc9 = b.c.locator(range(9),17)
    sources.append((17,11,list(range(13)),mono(11,(0,1,2))+[loc9+[0],[0]+loc9]))
    sources.append((17,14,list(range(15)),[[1]+[0]*13]+
                    [[0]*i+loc+[0]*(3-i) for i in range(4)]))
    total, outside = 0, 0
    for p,k,points,polys in sources:
        rows = b.c.rows_for(polys,points,p)
        n,s = len(rows),len(polys)
        need(n>k>=s and rank(rows,p)==s and all(any(row) for row in rows),"actual source")
        flats = {(0,()):()}
        for j in range(1,s):
            for indices in combinations(range(n),j):
                basis = [rows[i] for i in indices]
                if rank(basis,p) != j:
                    continue
                closed = tuple(i for i,row in enumerate(rows) if rank(basis+[row],p)==j)
                flats.setdefault((j,closed),indices)
        h = max(F(len(inside),j) for j,inside in flats if j)
        mu = profile(n-k,k,k,s,h)
        wide = profile(n-k,s,k+2,s,h)
        inflation = max(F(1),F(s*s//4)*h/n)
        outside += inflation > 2
        for (j,inside),indices in flats.items():
            r,kk,nn = s-j,k-len(inside),n-len(inside)
            basis = [rows[i] for i in indices]
            remaining = [i for i in range(n) if i not in inside]
            if r>=3:
                fibers = {tuple(y for y in remaining
                                if rank(basis+[rows[x],rows[y]],p)==j+1)
                          for x in remaining}
                moment = sum(len(fiber)**2 for fiber in fibers)
                need(sum(map(len,fibers))==nn,"complete actual fibers")
                need(F(moment,nn*(kk-1))<=mu[r],"actual rank-profile moment")
                need(F(moment,nn*(kk-1))<=wide[r],"whole-box moment at actual descendant")
            if r>=2:
                bases = factorial(r)*sum(rank(basis+[rows[i] for i in chosen],p)==s
                                         for chosen in combinations(remaining,r))
                need(bases>=product(n-k,kk,r,mu),"frozen profile at every descendant")
                need(bases>=product(n-k,kk,r,wide),"wide degree-box profile")
            total += 1
        root_count = b.c.basis_count(rows,p,s)
        need(root_count>=bound(n-k,s,k+2,s,h),"whole degree-box root lower count")
        if inflation<=2:
            need(bound(n-k,k,k,s,h)>=old.product(n-k,k,s,inflation),"dominates old product")
        print("ACTUAL",p,k,n,s,"density",h,"old_lambda",inflation,
              "flats",len(flats),"bases",root_count,"bound",bound(n-k,k,k,s,h),flush=True)
    need(outside>=1 and total>=840,"genuinely larger scope")
    controls = 0
    for s in range(2,12):
        for k in (s,s+4,s+19):
            for h in (F(1),max(F(1),F(k,3)),F(k)):
                mu = profile(7,k,k+3,s,h)
                for x in (1,s,k):
                    unrolled = 8*prod(8+(x-1)*prod(1-mu[r] for r in range(a+1,s+1))
                                      for a in range(2,s+1))
                    need(product(7,x,s,mu)==unrolled,"unrolled profile")
                    need(product(7,x+2,s,mu)-2*product(7,x+1,s,mu)+product(7,x,s,mu)>=0,
                         "fixed-profile convexity")
                    controls += 1
    for args in ((0,5,5,3,F(1)),(7,2,5,3,F(1)),(7,5,4,3,F(1)),(7,5,5,3,F(1,2))):
        try:
            bound(*args)
        except ValueError:
            pass
        else:
            raise ValueError("accepted invalid profile domain")
    for mu in ({}, {3:F(11,10)}):
        try:
            product(7,5,3,mu)
        except ValueError:
            pass
        else:
            raise ValueError("accepted missing or nonconvex rank profile")
    print("PASS",total,"actual descendants;",controls,"formula/curvature controls; six guards")
    print("Hand proof, not numerical extrapolation or received-word payment")


if __name__ == "__main__":
    main()
