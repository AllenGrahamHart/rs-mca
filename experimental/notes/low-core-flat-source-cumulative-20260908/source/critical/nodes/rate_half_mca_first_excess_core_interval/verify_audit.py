"""Independent integer audit with explicit derivatives and full tangent vectors."""

import hashlib
import importlib.util
from math import comb, gcd, prod
from pathlib import Path

path = Path(__file__).resolve().parents[1]/"rate_half_mca_quotient_density_interval/verify_audit.py"
spec = importlib.util.spec_from_file_location("independent_quotient", path)
q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)
D, R, GAP, ADD = 67466, 1048576, 67472, 134944
TOTAL = 273019482620216244
EXPECTED = "a34884087a5dd4e1ddfabb9413b89f4bfa4fc02dd6dc7389ed8e5bea6c5f3dc9"


def check(ok, why):
    if not ok:
        raise ValueError(why)


def reduced(n, d):
    check(n > 0 and d > 0, "positive rational count")
    g = gcd(n, d)
    return n//g, d//g


def balanced(rank, degree):
    scale = rank-1
    return prod(scale*(D+degree)-i*(degree-1) for i in range(rank)), scale**rank


def value_and_derivative(factors, point):
    terms = [x-point for x in factors]
    return prod(terms), sum(prod(terms[:i]+terms[i+1:]) for i in range(len(terms)))


def inner(factors, first, last, caps):
    t = len(factors)
    check(t <= first <= last < min(factors), "positive complete-flat box")
    points, selected = {}, comb(11, t)
    for i in reversed(range(1, t)):
        lower, upper = max(first-caps[i-1], 0), last-i
        check(0 <= lower <= upper < min(factors), "tangent hull")
        weight = comb(11, i)

        def candidate(z):
            value, derivative = value_and_derivative(factors[:t-i], z)
            tail = selected-weight*derivative
            return weight*(value+z*derivative)+tail*(lower if tail >= 0 else upper), tail

        # Locate the first nonnegative tail; optimality is not a proof premise.
        a, b = lower, upper+1
        while a < b:
            mid = (a+b)//2
            if candidate(mid)[1] < 0:
                a = mid+1
            else:
                b = mid
        candidates = {min(a, upper), max(lower, a-1)}
        chosen = max(candidates, key=lambda z: (candidate(z)[0], -z))
        points[i] = chosen
        selected = candidate(chosen)[0]

    coefficients, previous = [], 0
    for i in range(1, t+1):
        z = points.get(i, 0)
        value, derivative = value_and_derivative(factors[:t-i], z)
        coefficients.append(comb(11, i)*(value+z*derivative)-previous)
        previous = comb(11, i)*derivative
    tail = coefficients[-1]
    for i in reversed(range(1, t)):
        multiplier = max(first-caps[i-1], 0) if tail >= 0 else last-i
        tail = coefficients[i-1]+tail*multiplier
    check(tail == selected, "independent full coefficient-vector elimination")
    base = prod(x-last for x in factors)
    return max(base, base+tail*(first if tail >= 0 else last))


def quotient(rank, minimum, maximum, greedy):
    minimum = max(rank, minimum)
    check(rank <= minimum <= maximum <= D and greedy > 0, "actual quotient hull")
    count = max(greedy, q.quotient_basis(rank, D, maximum, minimum))
    num, den = count, 1
    f = rank*rank//4
    if f*(maximum-rank+1) <= D+maximum:
        bn, bd = balanced(rank, minimum)
        if bn > num*bd:
            num, den = bn, bd
    return num, den


def flat_cap(J, r, first_excess_rank):
    choices = [J-11+r, r*(J-5)//6]
    if r < first_excess_rank:
        choices.append((J+D)//(11-r))
    return min(choices)


def cost(kind, left, right, t, lo, hi):
    ell = 11-t
    if kind == "L":
        first, last = lo, hi
        ds = [D+left-flat_cap(left, r, t) for r in range(10, ell-1, -1)]
        caps = [flat_cap(right, r, t) for r in range(1, t)]
        greedy = (D+left-last)*prod(D+left-flat_cap(left, r, t) for r in range(t+1, 11))
        qn, qd = quotient(ell, left-last, right-first, greedy)
    else:
        first, last = left-hi, right-lo
        ds = [max(D+11-r, D+right-r*last//t) for r in range(10, ell-1, -1)]
        caps = [r*last//t for r in range(1, t)]
        greedy = (D+lo)*prod(max(D+ell-i, D+lo-i*last//t) for i in range(1, ell))
        qn, qd = quotient(ell, lo, hi, greedy)
    return reduced(12*qn*inner(ds, first, last, caps), qd)


def partition(start, end, count, extra=()):
    if start > end:
        return
    width = (end-start+count)//count
    cuts = [start]
    while cuts[-1]+width <= end:
        cuts.append(cuts[-1]+width)
    cuts = sorted(set(cuts+[end+1]+[v for v in extra if start < v <= end]))
    check(cuts[0] == start and cuts[-1] == end+1, "size endpoints")
    for a, b in zip(cuts, cuts[1:]):
        check(a < b, "nonempty size bin")
        yield a, b-1


def main():
    digest = hashlib.sha256()
    counts, peak, floors, blocks = {"L": 0, "H": 0}, 0, 0, 0
    left = 28000
    while left < 30000:
        right = min(left+31, 29999)
        resource = prod(range(R+right-11, R+right+1))
        ln, ld = balanced(11, left)
        ln *= 12
        hn, hd = 10488*(GAP+left)*prod(range(GAP+1, GAP+11)), 125
        if hn*ld < ln*hd:
            ln, ld = hn, hd
        bn, bd = reduced(resource*ld, ln)
        digest.update(f"B:{left},{right}:{bn}/{bd}\n".encode())
        peak = max(peak, bn//bd+ADD)
        for kind, ranks in (("L", range(1, 8)), ("H", range(1, 6))):
            for t in ranks:
                if kind == "L":
                    lower = (left+D)//(11-t)+1
                    upper = min(right-11+t, t*(right-5)//6)
                    bins = partition(lower, upper, 256 if left < 28256 and t >= 6 else 128)
                else:
                    ell = 11-t
                    f = ell*ell//4
                    extra = [(D+f*(ell-1))//(f-1)+1]
                    if t == 1:
                        extra.extend(2001+32*i for i in range(16))
                    bins = partition(2001 if t == 1 else ell,
                                     right-t*(right-5)//6-1, 64, extra)
                for a, b in bins:
                    cn, cd = cost(kind, left, right, t, a, b)
                    num, den = resource*cd, cn
                    floor = num//den
                    check(floor*den <= num < (floor+1)*den, "exact floor")
                    for wrong in (floor-1, floor+1):
                        check(not wrong*den <= num < (wrong+1)*den, "wrong floor fails")
                        floors += 1
                    cap = floor+ADD
                    digest.update(f"{kind}:{left},{right},{t},{a},{b}:{cn}/{cd}:{cap}\n".encode())
                    check(cap <= TOTAL, "all parameter boxes paid")
                    peak = max(peak, cap)
                    counts[kind] += 1
        blocks += 1
        left = right+1
    check(blocks == 63 and left == 30000 and counts == {"L": 41957, "H": 21355}, "entire cover")
    check(floors == 126624 and peak == TOTAL, "independent maximum")
    check(digest.hexdigest() == EXPECTED, "every independent rational cost")
    check(248408859318207582 < TOTAL < 274929007493481160, "source alternatives included")
    check(2130706433**6//2**128-TOTAL == 1961245491178843, "reserve")
    print("PASS independent integers: 63312 boxes; 63 degree blocks; 126624 wrong floors")
    print("Full tangent vectors independently reconstructed on every box")
    print("MAX", peak, "DIGEST", digest.hexdigest())
    print("Every carrier on J=28000..29999 paid; unrestricted endpoint remains OPEN")


if __name__ == "__main__":
    main()
