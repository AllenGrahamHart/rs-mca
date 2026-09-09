"""Independent polynomial and integer reconstruction; no primary imports."""

from fractions import Fraction as Q
from math import lcm, prod


def need(ok, message):
    if not ok:
        raise ValueError(message)


def add(a, b):
    return [(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


def mul(a, b):
    result = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def at(a, x):
    result = 0
    for coefficient in reversed(a):
        result = result*x+coefficient
    return result


def substitute(a, linear):
    result, power = [0], [1]
    for coefficient in a:
        result = add(result, [coefficient*x for x in power])
        power = mul(power, linear)
    return result


def basis_polynomial():
    D, end, x = 66972, 10000, 5000
    q = [value/Q(D+2) for value in mul([D, 1], [D+Q(1, 2), Q(1, 2)])]
    curvature = q[2]
    for rank in range(4, 12):
        H = D+rank-1
        need(q[1] >= D*q[2] >= 0, "input quadratic condition")
        spike = add(substitute(q, [-1, 1]), [-Q(rank-1, H)*at(q, rank-1), at(q, rank-1)/H])
        equal = [value/H for value in mul([D, 1], substitute(q, [Q(1, rank-1), Q(rank-2, rank-1)]))]
        residual = add(equal, [0, 0, -curvature])
        need(residual[2] >= 0 and residual[3] >= 0, "nonnegative convex residual")
        slope = at([i*residual[i] for i in range(1, len(residual))], x)
        tangent = [at(residual, x)-x*slope, slope]
        difference = add(tangent, [-spike[0], -spike[1]])
        shift = max(0, at(difference, rank), at(difference, end))
        q = [tangent[0]-shift, tangent[1], curvature]
        need(min(q) > 0 and q[1] >= D*q[2], "positive next coefficients")
        need(at(spike, rank) >= at(q, rank) and at(spike, end) >= at(q, end),
             "whole affine spike interval")
        actual = add(equal, [-value for value in q])
        expected = add([shift], mul([x*x, -2*x, 1],
                                   [residual[2]+2*x*residual[3], residual[3]]))
        need(actual == expected, "exact squared-factor identity")
    return q


def weighted_pairs(kernel, dim, height):
    top, bottom = 1048577-height, 67423-height
    return 2**kernel*3**(22-kernel-dim)*top**dim//bottom**dim


def main():
    q = basis_polynomial()
    denominator = lcm(*(value.denominator for value in q))
    a, b, c = [int(value*denominator) for value in q]
    need(all(Q(value, denominator) == old for value, old in zip((a, b, c), q)),
         "exact integer conversion")
    P, Pd = prod(range(66973, 66983)), prod(range(67473, 67483))
    W, near, budget = 646273487661620022, 134944, 2130706433**6//(1 << 128)
    maximum, previous, count = 0, None, 0
    for J in range(9941, 9965):
        numerator = prod(range(1048576+J-11, 1048576+J+1))*denominator
        div = 12*P*(a+b*J+c*J*J)
        value, rem = divmod(numerator, div)
        need(0 <= rem < div, "positive exact mass floor")
        need(5500*(67472+J)*Pd*denominator >= 51*div, "all actual-degree HIGH gates")
        need(previous is None or value <= previous, "integer monotonicity control")
        previous, maximum = value, max(maximum, value)
        degree, w = 2*(J+67422), J-1
        dimensions = [sum((i+1)*max(z-i*w, 0) for i in range(20))
                      for z in (degree, degree-4*w)]
        need((degree-1)//w == 15 and (degree-4*w-1)//w == 11, "both complete monomial lists")
        need(dimensions[0]-dimensions[1]-4*(1048576+J) == 3627124-364*J > 0,
             "literal full-kernel dimension sum")
        need((degree-1-3*w)//3 <= 41635, "actual primitive factor height")
        count += 1
    need(count == 24 and maximum == W, "whole interval mass maximum")
    degree, w = 2*(9965+67422), 9964
    difference = sum((i+1)*(max(degree-i*w, 0)-max(degree-(i+4)*w, 0)) for i in range(20))
    need(difference-4*(1048576+9965) == -136, "adjacent failed kernel, not unsafety")
    for raw in range(1, 502):
        correction = sum((Q(raw, t*(t+1)) for t in range(raw, 51)), Q(0))
        need(Q(min(raw, 51), 51)+correction == 1, "every cumulative raw coefficient")
    harmonic = sum((Q(1, t) for t in range(1, 52)), Q(0))
    exceptional = 256*(981104*Q(50, 51)+harmonic-1)
    curve = sum((Q(128*3**12*(981104+t)*1047027**3,
                   (65923-t)**3*t*(t+1)) for t in range(1, 51)), Q(0))
    amount = Q(W, 51)+curve+exceptional
    total = amount.numerator//amount.denominator+near
    need(total == 274861473951141154 and budget-total == 119254160253933,
         "independent harmonic exception split and final floor")
    for wrong in (total-1, total+1):
        need(not wrong-near <= amount < wrong-near+1, "wrong total rejected")
    base, labels = W//51+near, 981154
    need(base == 12672029169970630, "single raw-resource base")

    u, slots = [68973, 3], [2103354, 7]
    den = add(mul(u, u), [0]+[-v for v in slots])
    need(den == [68973**2, -1689516, 2], "component denominator polynomial")
    ell = (9964-1-1551)//3
    need(ell == 2804 and den[1]+2*den[2]*ell < 0 and at(den, ell) == 35596697 > 0,
         "entire component-degree interval")
    numerator = mul(slots, add(u, [0, -1]))
    need(all(value > 0 for value in numerator), "increasing component numerator")
    top = at(numerator, ell)//at(den, ell)
    lower = weighted_pairs(7, 2, 4981)
    need(top == 4448 and lower == 57002969822, "independent full component counts")
    high_total = base+labels*(3**16*top+lower+257)
    need(high_total == 256464058457221028 < total, "all components and exceptions")
    n, a1, collision = 1058540, 77363-21*996, 3*996
    gp = n*(a1-collision)//(a1*a1-n*collision)
    gp_lower = weighted_pairs(10, 3, 996)
    need((gp, gp_lower) == (2423, 79053330393), "independent GP alternatives")
    need(base+labels*(max(gp+1, gp_lower)+256) == 90235520749559576 < total,
         "singular and lower-dimensional GP loci")
    ordinary = [(0, 0, 0), (1, 1, 9963), (2, 1, 9963), (3, 1, 9963),
                (4, 2, 9963), (5, 2, 9963), (6, 2, 4981), (8, 3, 3321),
                (9, 3, 1992), (11, 4, 0)]
    totals = [base+labels*(weighted_pairs(e, r, h)+256) for e, r, h in ordinary]
    need(max(totals) == 269761880886747862 < total, "independent full kernel-dimension table")
    for pairs in (163774741769, 223154201664, 6):
        need(base+labels*(pairs+256) < total, "remaining cubic types")
    small_den = add([77363**2], [-v for v in mul([590000, 16], [9963, -1])])
    need(small_den == [106863769, 430592, 16], "small-line denominator identity")
    small = (590000+16*9963)*77363//small_den[0]
    need(small == 542 and 57460-9963 > 0 and 458576 < 8*57460,
         "line and complement exact endpoints")
    large = 255637082864553899+labels*(2*8**11+256)
    need(large == 272493180485087659 < total, "one coupled primary resource")
    need(11*51 > 501 and large+base > budget, "medium-raw and repeated-resource controls")
    for pairs in (3*small, 127031877504+small, 0):
        need(base+labels*(pairs+256) < total, "all smaller gcd patterns")
    need((1048576-9964, 1048576-9941) == (1038612, 1038635), "new original core interval")
    need(21499-9965+1 == 11535 and 11559-11535 == 24, "exact remaining degree count")
    print("PASS independent eight polynomial identities and all24 kernel/mass degrees")
    print("PASS501 cumulative coefficients, all factor prices, wrong totals and original-core endpoints")
    print("Universal source/geometry proofs are required; no full Prize closure")


if __name__ == "__main__":
    main()
