"""Actual small flags and bases; no field-scale computation or proof certification."""

import importlib.util
from itertools import combinations
from pathlib import Path

path = Path(__file__).resolve().parents[1]/"mca_balanced_basis_under_flat_density/verify.py"
spec = importlib.util.spec_from_file_location("balanced_controls",path)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
need, rank = b.need, b.rank


def excess(n,s,t,a,z):
    return 1<=t<=s-2 and (s-t)*z-(s-t-1)*a>n


def actual(p,k,points,polys,deficient=False,has_flag=None):
    rows = b.c.rows_for(polys,points,p)
    n,s = len(rows),len(polys)
    need(n>k>=s and rank(rows,p)==s and all(any(row) for row in rows),"actual source")
    flats = {(0,()):()}
    for j in range(1,s-2):
        for indices in combinations(range(n),j):
            basis = [rows[i] for i in indices]
            if rank(basis,p)!=j:
                continue
            closure = tuple(i for i,row in enumerate(rows) if rank(basis+[row],p)==j)
            flats.setdefault((j,closure),indices)
    flags = set()
    checked = 0
    for (j,inside),indices in flats.items():
        basis = [rows[i] for i in indices]
        for x in range(n):
            if x in inside:
                continue
            t = j+1
            larger = tuple(i for i,row in enumerate(rows) if rank(basis+[rows[x],row],p)==t)
            a,z = len(inside),len(larger)
            need(a>=j and z<=k-s+t and set(inside)<=set(larger),"actual complete flag and root capacity")
            if excess(n,s,t,a,z):
                flags.add((j,inside,larger))
            checked += 1
    bases, product = b.c.basis_count(rows,p,s), b.product(n-k,k,s)
    need(bases>=product or flags,"deficient product has an actual flag")
    if deficient:
        need(bases<product and flags,"actual deficient control")
    if has_flag is not None:
        need(bool(flags)==has_flag,"declared flag control")
    print("PASS actual",(p,k,n,s),"bases",bases,"product",product,
          "flags",len(flags),"flag checks",checked)
    return bases>=product,bool(flags)


def main():
    mono=lambda k,powers:[tuple(int(i==v) for i in range(k)) for v in powers]
    actual(17,4,list(range(9)),mono(4,range(4)),has_flag=False)
    actual(23,7,[x%23 for x in range(-8,9) if x],mono(7,(0,2,4,6)),has_flag=False)
    loc=b.c.locator(range(10),17)
    p3=[[1]+[0]*11,loc+[0],[0]+loc]
    actual(17,12,list(range(13)),p3,True,True)
    p4=[[1]+[0]*12]+[[0]*i+loc+[0]*(2-i) for i in range(3)]
    actual(17,13,list(range(14)),p4,True,True)
    both=actual(17,12,list(range(13)),[p3[0],[0,1]+[0]*10,p3[1],p3[2]],has_flag=True)
    need(both==(True,True),"alternatives can overlap")
    need(not excess(13,4,2,1,7) and excess(13,4,2,1,8),"strict flag boundary")
    need(not excess(90466,11,7,6,22621) and excess(90466,11,7,6,22622),"finite boundary")
    need(not excess(10,2,1,0,10),"no rank-two flag")
    print("PASS strict boundaries and nonexclusive alternative; not an unsafe MCA construction")


if __name__ == "__main__":
    main()
