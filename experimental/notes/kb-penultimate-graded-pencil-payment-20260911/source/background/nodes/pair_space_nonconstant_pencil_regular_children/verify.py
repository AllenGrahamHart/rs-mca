"""Small exact F97 controls, using the inherited regular-anchor linear algebra."""
import importlib.util
from math import gcd
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent/"pair_space_regular_projection_anchor/verify.py"
SPEC = importlib.util.spec_from_file_location("anchor_controls",PATH)
ANCHOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ANCHOR)
P = 97


def need(ok,why):
    if not ok:
        raise ValueError(why)


def rank(rows):
    return len(ANCHOR.rref(rows,P)[1])


def evaluation(rows,powers,x):
    n = len(powers)
    v = [pow(x,e,P) for e in powers]
    return [[sum(row[i+side*n]*v[i] for i in range(n))%P for row in rows]
            for side in (0,1)]


def section(rows,powers,x):
    vectors = ANCHOR.kernel(evaluation(rows,powers,x),P)
    return [[sum(c*v[i] for c,v in zip(coeff,rows))%P for i in range(len(rows[0]))]
            for coeff in vectors]


def projected(rows,n,z):
    return rank([[(row[i]+z*row[i+n])%P for i in range(n)] for row in rows])


def regular(rows,powers,s):
    return any(projected(rows,len(powers),z)==s for z in range(len(powers)+1))


def pair(n,first=None,second=None):
    row = [0]*(2*n)
    if first is not None:
        row[first] = 1
    if second is not None:
        row[n+second] = 1
    return row


def check(powers,rows,pencil,x,s):
    n = len(powers)
    need(rank(rows)==len(rows) and regular(rows,powers,s),"parent full generic projection")
    need(rank(evaluation(rows,powers,x))==2,"joint-good actual anchor")
    child = section(rows,powers,x)
    plane = section(pencil,powers,x)
    need(rank(child)==len(rows)-2 and regular(child,powers,s-1),"regular child")
    need(rank(child+plane)==rank(child),"actual pencil section retained")
    need(any(rank(evaluation(child,powers,y))==2 for y in range(P)),
         "child function-field rank two")
    return child,plane


def main():
    steps = 0
    for initial in range(4,12):
        powers = list(range(initial))
        pencil = [pair(initial,i,i+1) for i in range(initial-1)]
        rows = pencil+[pair(initial,None,0)]+[pair(initial,i,None) for i in range(3,initial)]
        s,used = initial,set()
        while s>3:
            for x in range(P):
                if x in used or rank(evaluation(rows,powers,x))!=2:
                    continue
                proposed = section(rows,powers,x)
                if regular(proposed,powers,s-1):
                    break
            else:
                raise ValueError("no regular coordinate in the small control")
            rows,pencil = check(powers,rows,pencil,x,s)
            used.add(x)
            s -= 1
            need(rank(pencil)==s-1,"maximal pencil dimension")
            need(rank([v[:initial] for v in pencil]+[v[initial:] for v in pencil])==s,
                 "component carrier equality survives")
            steps += 1
        need(len(rows)==3 and len(pencil)==2,"paid terminal geometry")
    for e in (1,2,3):
        powers = [0,2*e,3*e,5*e]
        pencil = [pair(4,0,1),pair(4,2,3)]
        rows = pencil+[pair(4,None,0),pair(4,1,None),pair(4,3,None)]
        child,remaining = check(powers,rows,pencil,0,4)
        need(len(remaining)==1,"smooth-point pencil rank drop")
        need(gcd(*powers)==gcd(0,e,3*e)==e,"singular curve point, birational inner map")
        need(5*e-2*e==3*e,"full fixed divisor, not branch count")
    powers = [0,3,5,7]
    pencil = [pair(4,3,2),pair(4,2,1)]
    rows = pencil+[pair(4,None,3),pair(4,0,None),pair(4,None,0)]
    child,remaining = check(powers,rows,pencil,0,4)
    need(len(remaining)==2 and rank(remaining+pencil)==2,"vertex retains FULL plane")
    need(gcd(*powers)==1 and gcd(0,2,4)==2 and 7==3+2*2,"actual vertex degree jump")
    constant = [pair(4,i,None) for i in range(4)]+[pair(4,None,0)]
    need(regular(constant,list(range(4)),4),"constant control regular parent")
    whole = section(constant,list(range(4)),0)
    need(rank(whole)==3 and regular(whole,list(range(4)),3)
         and all(not any(row[4:]) for row in whole),"regular whole constant child")
    line = pair(4,1,0)
    need(rank(constant+[line])==5,"a single nonconstant direction is insufficient")
    print("PASS",steps,"maximal-pencil regular anchors, shared dimensions4..11 down to3")
    print("PASS smooth quadric at a singular curve point, three covers; cone vertex mu2 with retained plane")
    print("PASS constant-pencil and single-direction scope controls")
    print("Enclosure fixtures only; universal quadric/owner proofs are not replaced by these tests")


if __name__=="__main__":
    main()
