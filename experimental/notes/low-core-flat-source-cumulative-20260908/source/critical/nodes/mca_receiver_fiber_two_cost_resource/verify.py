"""Tiny exact resource controls and actual full-fiber core basis counts."""

from fractions import Fraction as F
import importlib.util
from itertools import combinations
from pathlib import Path


def need(ok,why):
    if not ok:
        raise ValueError(why)


def bound(resource,light,heavy,cap):
    need(resource>=0 and light>0 and heavy>=0 and cap>=0,"cost domain")
    return F(resource)/light+max(F(0),1-F(heavy)/light)*cap


def main():
    count=0
    for light in range(1,7):
        for heavy in range(0,7):
            for h in range(0,8):
                for l in range(0,8):
                    resource=light*l+heavy*h
                    for cap in (h,h+3):
                        need(l+h<=bound(resource,light,heavy,cap),"two-cost resource")
                        count+=1
    need(5>F(10,2)+(1-F(4,2))*3,"negative coefficient must not use upper H")
    need(bound(10,2,4,3)==5,"positive-part correction")
    path=Path(__file__).resolve().parents[1]/"mca_fiber_contraction_core_basis_resource/verify.py"
    spec=importlib.util.spec_from_file_location("actual_controls",path)
    old=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    p,k,s,M=17,7,3,8
    A=tuple(range(5))
    loc=old.locator(A,p)
    polys=[[1]+[0]*6,loc+[0],[0]+loc]
    points=tuple(range(13))
    rows=old.rows_for(polys,points,p)
    need(old.rank(rows,p)==s,"actual carrier")
    controls=0
    for t in range(6):
        core=A[:t]+points[5:5+M-t]
        need(len(core)==M and len(set(core)&set(A))==t,"full heavy color retained")
        selected=[rows[i] for i in core]
        exact=6*sum(old.rank([selected[i] for i in indices],p)==s
                    for indices in combinations(range(M),s))
        lower=(M-t)*(M-t-1)*(s*t+max(2-t,0))
        need(exact>=lower,"actual F_A(t) basis lower count")
        controls+=1
    for args in ((1,0,1,1),(1,1,-1,1),(1,1,1,-1)):
        try:
            bound(*args)
        except ValueError:
            pass
        else:
            raise ValueError("invalid cost accepted")
    print("PASS",count,"two-cost cases;",controls,"actual polynomial cores; three guards")
    print("Negative-coefficient mutation rejected; universal source proof is separate")


if __name__=="__main__":
    main()
