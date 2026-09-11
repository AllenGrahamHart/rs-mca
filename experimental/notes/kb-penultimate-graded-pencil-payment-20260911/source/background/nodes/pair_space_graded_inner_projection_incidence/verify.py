"""Small exact ledger controls; no claim of realized MCA sources."""
from fractions import Fraction as Q
from math import comb


def need(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    d,nu = 9,3
    degree,genus = nu*d,comb(d-2,2)
    entries = ((5,2,2,30),(1,4,2,30))
    charges = [comb(m+mu-1,2) for m,mu,eta,excess in entries]
    need(sum(charges)==genus, "one shared budget")
    extra = sum(nu*m*excess for m,mu,eta,excess in entries)
    theta = max((eta-1)*excess for m,mu,eta,excess in entries)
    need(all(m+mu*eta==d for m,mu,eta,excess in entries), "same parent degree")
    need(extra==540<=degree*theta==810, "graded total")
    checked = 0
    for n,a,c,b0 in ((200,40,7,4),(200,200,1,0),(90,30,3,5)):
        need(n>=a>degree, "positive denominator contract")
        final = c*Q((n-degree)*b0+degree*theta,a-degree)
        previous = None
        for bad in range(degree+1):
            actual = c*Q((n-bad)*b0+extra,a-bad)
            bound = c*Q((n-bad)*b0+degree*theta,a-bad)
            need(actual<=bound<=final, "incidence transport")
            need(previous is None or previous<=bound, "bad-coordinate monotonicity")
            previous = bound
            checked += 1
    need(comb(3-2,2)==0 and all(1+mu*2>3 for mu in range(2,10)),
         "minimal-degree G=0 has no nonbirational child")
    # The N>=A guard prevents a negative proposed bound even for an empty family.
    need(Q((0-3)*1,4-3)<0, "N>=A cannot be omitted from the abstract contract")
    print("PASS",checked,"graded-ledger transports; G=0 and N>=A contract controls")
    print("Synthetic ledgers are not official-source witnesses; universal incidence is a written proof")


if __name__ == "__main__":
    main()
