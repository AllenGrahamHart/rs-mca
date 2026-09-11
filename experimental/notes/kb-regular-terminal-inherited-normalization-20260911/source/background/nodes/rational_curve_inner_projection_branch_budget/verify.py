"""Exact singular-fibre and positive-characteristic scope controls."""
from fractions import Fraction as Q
from math import comb,gcd

from bounds import coordinate_bound


def need(ok,why):
    if not ok:
        raise ValueError(why)


def main():
    checked = 0
    for h in range(2,35):
        for b in range(1,50):
            charge = comb(b+h-1,2)
            need(charge-(2*h-3)*b==(b-h+1)*(b-h+2)//2>=0,"integer branch price")
            checked += 1
        for maximum in range(1,35):
            b0 = min(maximum,max(1,h-2))
            need(Q(comb(b0+h-1,2),b0)==min(Q(comb(b+h-1,2),b) for b in range(1,maximum+1)),
                 "refined integer ratio minimum")
    roots = [x for x in range(97) if pow(x,12,97)==1]
    actual = [x for x in roots if x not in range(7)]
    genus = comb(36-3+1,2)
    need(genus==561 and comb(12+12-1,2)==253<=genus,"singular centre charge")
    wrong = genus//comb(12,2)
    correct = coordinate_bound(36,3,1,12)
    need(wrong==8<len(actual)==10<=correct==26,"centre count is NOT a coordinate count")
    # For U=(1,X,X^3,X^9) in characteristic3, all finite inner maps have degree2.
    for degree in (3,9):
        need(all(comb(degree,j) % 3==0 for j in range(1,degree)),"Frobenius identity")
    need(gcd(3-1,9-1)==2,"nonbirational generic inner projection in small characteristic")
    need(coordinate_bound(10,10,1,2)==0,"minimal-degree curve has no such centres")
    print("PASS",checked,"branch prices and all bounded integer ratio minima")
    print("PASS actual singular centre: naive coordinate cap8 fails on10 surviving coordinates; branch cap26")
    print("PASS characteristic3 degree9 control: generic inner degree2; p>d guard cannot be omitted")
    print("The low-degree trisecant and genus arguments are written proofs, not finite-field census claims")


if __name__ == "__main__":
    main()
