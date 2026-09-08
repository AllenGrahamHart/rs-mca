"""Independent integer-scaled certificate; imports neither primary nor Fraction."""

import hashlib
from math import comb, gcd, prod

D, R, d, ADD = 67466, 1048576, 67472, 134944
TOTAL = 274977202549132026
EXPECTED_DIGEST = "aa67aff314740d5cebcbd03b85dec7e136cea67b009740ad1bdc28ee4dde05d7"


def require(ok, why):
    if not ok:
        raise ValueError(why)


def reduce_pair(n, q):
    require(q > 0, "positive denominator")
    g = gcd(n, q)
    return n//g, q//g


def balanced(rank, degree):
    m = rank-1
    return prod(m*(D+degree)-i*(degree-1) for i in range(rank)), m**rank


def cost(left, right, rank, amin, amax):
    r = 11-rank
    kmin, kmax = left-amax, right-amin
    density8 = min(8*(kmax-r+1), (rank+1)*(right-3)-8*amin)
    require(r <= kmin <= kmax, "actual quotient degree hull")
    require((r*r//4)*density8 <= 8*(D+kmin), "balanced quotient density gate")
    coefficients = []
    for i in range(rank):
        coefficients.append(max(D+1+i, D+left-((10-i)*(left-3)//8)))
    require(min(coefficients) > amax, "all completion factors positive")
    qnum, qden = balanced(r, kmin)
    greedy = D+left-amax
    for i in range(1, r):
        greedy *= max(D+r-i, D+left-((rank+i)*(left-3)//8))
    qnum = max(qnum, qden*greedy)
    scale = 4**rank
    baseline = scale*prod(c-amax for c in coefficients)
    best = baseline
    for mode in range(6):
        terms, last_derivative = [], 0
        for order in range(1, rank+1):
            z = (4*max(amin-(order*(right-3)//8), 0) if mode == 5
                 else mode*amax)
            value, derivative = 1, 0
            for c in coefficients[:rank-order]:
                factor = 4*c-z
                derivative, value = derivative*factor+value, value*factor
            tangent = (value+z*derivative)*4**order
            terms.append(comb(11, order)*tangent-last_derivative)
            last_derivative = comb(11, order)*derivative*4**(order+1)
        tail = terms[-1]
        for order in reversed(range(1, rank)):
            extension = (max(amin-(order*(right-3)//8), 0) if tail >= 0
                         else amax-order)
            tail = terms[order-1]+tail*extension
        best = max(best, baseline+tail*(amin if tail >= 0 else amax))
    require(qnum > 0 and best > 0, "positive basis count")
    return reduce_pair(12*qnum*best, qden*scale)


def main():
    ranges = []
    for a, b, width in ((24538,26998,128), (26999,27015,1),
                        (27016,27199,16), (27200,27999,64), (28000,29999,128)):
        while a <= b:
            endpoint = min(a+width-1, b)
            ranges.append((a, endpoint))
            a = endpoint+1
    require(len(ranges) == 78 and ranges[0][0] == 24538
            and ranges[-1][1] == 29999, "full degree endpoints")
    require(all(ranges[i-1][1]+1 == ranges[i][0] for i in range(1,78)),
            "complete disjoint integer degree cover")
    digest, peak, count, wrong_floors = hashlib.sha256(), 0, 0, 0
    for start, end in ranges:
        resource = prod(R+end-i for i in range(12))
        lo_num, lo_den = balanced(11, start)
        lo_num *= 12
        hi_num, hi_den = 10488*(d+start)*prod(d+i for i in range(1,11)), 125
        if hi_num*lo_den < lo_num*hi_den:
            lo_num, lo_den = hi_num, hi_den
        qn, qd = reduce_pair(resource*lo_den, lo_num)
        digest.update(f"B:{start},{end}:{qn}/{qd}\n".encode())
        peak = max(peak, qn//qd+ADD)
        for t in range(1,8):
            divisor = t*(11-t)-8
            onset = (8*D+8*(10-t)*(t-1)+3*t*(11-t))//divisor+1
            left = max(start, onset)
            if left > end:
                continue
            lower = (left+D+(10-t)*(t-1))//(11-t)+1
            upper = min(end-11+t, t*(end-3)//8)
            if lower > upper:
                continue
            width = max(1, -(-(upper-lower+1)//8))
            first = lower
            while first <= upper:
                last = min(upper, first+width-1)
                cn, cd = cost(left, end, t, first, last)
                nn, dd = resource*cd, cn
                rounded = nn//dd
                require(rounded*dd <= nn < (rounded+1)*dd, "exact floor")
                for false in (rounded-1, rounded+1):
                    require(not false*dd <= nn < (false+1)*dd, "wrong floor rejected")
                    wrong_floors += 1
                cap = rounded+ADD
                digest.update(f"C:{left},{end},{t},{first},{last}:{cn}/{cd}:{cap}\n".encode())
                peak = max(peak, cap)
                count += 1
                first = last+1
            require(first == upper+1, "complete size partition")
    require(count == 2038 and wrong_floors == 4076 and peak == TOTAL,
            "entire independent certificate")
    require(digest.hexdigest() == EXPECTED_DIGEST, "all independently computed box values")
    require(2130706433**6//2**128-peak == 3525562263061, "original finite reserve")
    print("PASS independent integers: 78 blocks, 2038 flag boxes, 4076 wrong floors")
    print("MAX", peak, "DIGEST", digest.hexdigest())
    print("No unqualified product, exceptional-label upper census or unrestricted row claimed")


if __name__ == "__main__":
    main()
