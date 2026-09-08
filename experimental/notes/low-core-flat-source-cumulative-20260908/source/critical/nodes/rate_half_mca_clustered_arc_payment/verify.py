"""Exact whole-interval envelope and compressed smooth-domain example."""

from fractions import Fraction
from math import comb, factorial, isqrt, prod

R,D,FIBERS,HEIGHT,LOW,HIGH = 1048576,67472,560,2048,20481,22999
TOTAL = 274545534639685994


def need(ok,why):
    if not ok:
        raise ValueError(why)


def low_cost(j):
    return 12*prod(D+j-1-i*HEIGHT for i in range(11))


def verify_total(claim=TOTAL):
    n0,n1 = R+LOW,R+HIGH
    resource = Fraction(prod(FIBERS-i for i in range(12))*n0**12,FIBERS**12)
    exception = n1*(HEIGHT-1)//2
    ratio = resource/low_cost(LOW)
    need(exception == 1096757012, "one exception budget including zero coordinates")
    need(D+LOW-10*HEIGHT == 67473 > 6000, "whole LOW raw-margin guard")
    need(5500*(D+LOW)*prod(D+i for i in range(1,11)) > low_cost(HIGH),
         "HIGH cost covers the whole LOW floor")
    need(11*n0-12*(D+HIGH-1) == 10673987 > 0, "whole-J derivative guard")
    floor = claim-exception-134944
    need(floor <= ratio < floor+1, "exact final floor with exceptions and near")
    need(2130706433**6//2**128-claim == 435193471709093, "original reserve")
    return ratio.__floor__(),exception


def main():
    print("ENVELOPE", verify_total(), "TOTAL", TOTAL)
    for wrong in (TOTAL-1,TOTAL+1):
        try:
            verify_total(wrong)
        except ValueError:
            pass
        else:
            raise ValueError("accepted adjacent wrong total")
    p,order = 2130706433,2**21
    need(all(p%i for i in range(2,isqrt(p)+1)), "printed base field is prime")
    omega = pow(3,(p-1)//order,p)
    need(omega == 1213133211 and pow(omega,order,p) == 1
         and pow(omega,order//2,p) == p-1, "exact smooth-domain generator")
    need(order//HEIGHT == 1024 and 522*HEIGHT+1 == R+LOW,
         "compressed nonempty source class")
    need(10*HEIGHT < LOW and 523 <= FIBERS, "actual carrier degree and fiber gates")
    resource = factorial(12)*(comb(522,12)*HEIGHT**12+comb(522,11)*HEIGHT**11)
    exception = 522*comb(HEIGHT,2)
    total = resource//low_cost(LOW)+exception+134944
    need(total == 272166503326104174, "exact-histogram source bound")
    coarse = prod(R+LOW-i for i in range(12))//low_cost(LOW)+134944
    need(coarse == 309119416238808494 > 2130706433**6//2**128,
         "this unfiltered bound does not already pay the source")
    controls = ((LOW,560,2048,True),(HIGH,560,2048,True),
                (LOW-1,560,2048,False),(HIGH+1,560,2048,False),
                (LOW,561,2048,False),(LOW,560,2049,False))
    for j,f,h,expected in controls:
        need((LOW<=j<=HIGH and f<=560 and h<=2048) == expected, "source-gate endpoint")
    print("EXAMPLE",total,"UNFILTERED_BOUND",coarse,"EXCEPTIONS",exception)
    print("PASS two wrong totals and six source gates; no source enumeration")


if __name__ == "__main__":
    main()
