"""Exact endpoints and small actual raw-one sources; no original-row search."""

from fractions import Fraction as F
import importlib.util
from itertools import combinations
from math import factorial, prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("credited_actual_counts",
    ROOT/"critical/nodes/mca_fiber_contraction_core_basis_resource/verify.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
BUDGET = 2130706433**6//2**128


def check(ok, why):
    if not ok:
        raise ValueError(why)


def falling(n, r):
    return prod(n-i for i in range(r))


def ratio(j, offset, coefficient=None):
    check(9941<=j<=13999 and offset==10 or 14000<=j<=17000 and offset==2001,
          "exact source-gate regimes")
    a, N, b = j-offset,1048576+offset,67471+offset
    sharp = F(11,2*(N+a-12))
    lam = sharp if coefficient is None else F(coefficient)
    check(0<=lam<=sharp, "declared coefficient range only")
    X = a*(1+lam*(a-1))
    U = falling(N,11)*(N-11+12*X)
    H = 12*falling(b,10)*(b-10+11*X)
    check(12*(b-10)<11*(N-11), "strict ratio monotonicity")
    check(a*a+(2*a-1)*(N-12)>0, "X-star monotonicity numerator")
    check(a+9<j and b+a==67471+j and N+a==1048576+j,
          "actual degree and source/core lengths")
    return U/H


def fixture(p,s,a,k,m,n):
    points = list(range(n))
    loc = c.locator(range(a),p)
    polys = [[1]]+[[0]*i+loc for i in range(s-1)]
    rows = c.rows_for(polys,points,p)
    check(a+s-2<k<=m-1<n<p and c.rank(rows,p)==s, "actual carrier")
    check(c.rank(rows[:m-1],p)==s, "actual complete-core rank")
    fibers = {}
    for x,row in enumerate(rows):
        check(row[0]==1, "nonzero normalized projective rows")
        fibers.setdefault(row,[]).append(x)
    check(sorted(map(len,fibers.values()))==[1]*(n-a)+[a], "full source partition")
    received = [(0,0) if x<m-1 else (1,1) if x==m-1 else (0,1) for x in points]
    check(2*k-1<m, "all nonconstant explanations excluded by two levels and one point")
    check([x for x,(u,v) in enumerate(received) if (u-v)%p==0]==list(range(m)),
          "complete scalar support at gamma=-1")
    vand = [[pow(x,i,p) for i in range(k)] for x in range(m)]
    check(c.rank(vand,p)==k, "full degree-k evaluation rank")
    for column in (0,1):
        check(c.rank([row+[received[x][column]] for x,row in enumerate(vand)],p)==k+1,
              "no full-code polynomial component")
    check(sum(v!=0 for _,v in received[:m])==1, "raw one attained by zero")
    check(len({received[x] for x in range(a)})==1, "no fiber secant exceptions")
    bad_labels,minus_choices = set(),[]
    for gamma in range(p):
        for constant in range(p):
            agree = [x for x,(u,v) in enumerate(received) if (u+gamma*v-constant)%p==0]
            if len(agree)<m:
                continue
            matrix = [[pow(x,i,p) for i in range(k)] for x in agree]
            bad = any(c.rank([row+[received[x][column]] for x,row in zip(agree,matrix)],p)>k
                      for column in (0,1))
            if bad:
                bad_labels.add(gamma)
                if gamma==p-1:
                    minus_choices.append((constant,agree))
    check(bad_labels=={0,p-1}, "exact bad-label set after root-count reduction")
    check(minus_choices==[(0,list(range(m)))], "unique canonical raw-one support/explanation")
    normals = [list(row)+[received[x][1]] for x,row in enumerate(rows)]
    weights = [a-1 if x<a else 0 for x in points]
    core_bases = [ix for ix in combinations(range(m-1),s)
                  if c.rank([rows[i] for i in ix],p)==s]
    owned = [ix for ix in combinations(range(m),s+1)
             if c.rank([normals[i] for i in ix],p)==s+1]
    check(all(m-1 in ix for ix in owned) and len(owned)==len(core_bases),
          "all independent tuples contain the unique defect")
    good = [ix for ix in combinations(points,s+1) if sum(i<a for i in ix)<=1]
    N,b = n-a,m-1-a
    for lam in (F(0),F(s,4*(n-s-1)),F(s,2*(n-s-1))):
        actual = factorial(s+1)*sum(1+lam*sum(weights[i] for i in ix) for ix in owned)
        source = factorial(s+1)*sum(1+lam*sum(weights[i] for i in ix) for ix in good)
        upper = (s+1)*(falling(b,s)+s*a*(1+lam*(a-1))*falling(b,s-1))
        expected = falling(N,s+1)+(s+1)*a*(1+lam*(a-1))*falling(N,s)
        check(0<actual<=upper and source==expected, "full weighted counts")
    print("ACTUAL",(p,s,a,k,m,n),"unordered owned",len(owned),"good",len(good))


def main():
    floors = ((13999,10,379243051432496463),(17000,2001,275795460861917515))
    for j,offset,value in floors:
        q = ratio(j,offset)
        check(value<=q<value+1 and value>BUDGET, "endpoint floor already exceeds budget")
        check(ratio(j,offset,0)>q, "zero credit is worse")
        for wrong in (value-1,value+1):
            check(not wrong<=q<wrong+1, "reject adjacent wrong floor")
        print("ENDPOINT",j,"floor",value,"excess before near",value-BUDGET)
    check(floors[-1][-1]-BUDGET==814732750522428, "minimum obstruction margin")
    check(13999-9941+1+17000-14000+1==7060, "complete analytic interval cover")
    for args in ((9940,10),(13999,2001),(14000,10),(17001,2001),(17000,2001,-1),(17000,2001,1)):
        try:
            ratio(*args)
        except ValueError:
            pass
        else:
            raise ValueError("accepted invalid scope/coefficient")
    fixture(17,3,3,5,10,14)
    fixture(19,4,4,7,14,17)
    print("PASS two endpoint certificates, four wrong floors, six scope guards, two actual sources")
    print("METHOD boundary only; source-adaptive larger weights and actual ownership remain open")


if __name__=="__main__":
    main()
