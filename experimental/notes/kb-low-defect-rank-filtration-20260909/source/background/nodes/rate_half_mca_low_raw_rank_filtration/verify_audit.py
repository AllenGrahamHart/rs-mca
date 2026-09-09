"""Independent polynomial-convolution ladder and integer degree stream."""

from fractions import Fraction
from math import lcm, prod


def need(ok, message):
    if not ok:
        raise ValueError(message)


def add(a, b):
    return [(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


def mul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def at(a, x):
    out = 0
    for coefficient in reversed(a):
        out = out*x+coefficient
    return out


def substitute(a, linear):
    out, power = [0], [1]
    for coefficient in a:
        out = add(out, [coefficient*x for x in power])
        power = mul(power, linear)
    return out


def build():
    D, end, x = 67347, 21499, 5000
    q = [v/Fraction(D+2) for v in mul([D, 1], [D+Fraction(1, 2), Fraction(1, 2)])]
    curvature = q[2]
    for rank in range(4, 12):
        H = D+rank-1
        need(q[1] >= D*q[2] >= 0, "input quadratic hypothesis")
        spike = add(substitute(q, [-1, 1]), [-Fraction(rank-1, H)*at(q, rank-1),
                                             at(q, rank-1)/H])
        equal = [v/H for v in mul([D, 1], substitute(q, [Fraction(1, rank-1),
                                                            Fraction(rank-2, rank-1)]))]
        residual = add(equal, [0, 0, -curvature])
        need(residual[2] >= 0 and residual[3] >= 0, "convex residual coefficients")
        slope = at([i*residual[i] for i in range(1, len(residual))], x)
        tangent = [at(residual, x)-x*slope, slope]
        difference = add(tangent, [-spike[0], -spike[1]])
        shift = max(0, at(difference, rank), at(difference, end))
        q = [tangent[0]-shift, tangent[1], curvature]
        need(min(q) > 0 and q[1] >= D*q[2], "positive next certificate")
        actual = add(equal, [-v for v in q])
        expected = add([shift], mul([x*x, -2*x, 1],
                                   [residual[2]+2*x*residual[3], residual[3]]))
        need(actual == expected, "exact polynomial remainder, not sample values")
        need(at(spike, rank) >= at(q, rank) and at(spike, end) >= at(q, end),
             "affine spike endpoint certificate")
    return q


def main():
    q = build()
    denominator = lcm(*(v.denominator for v in q))
    a, b, c = [int(v*denominator) for v in q]
    need(all(Fraction(v, denominator) == old for v, old in zip((a, b, c), q)),
         "integer polynomial conversion")
    P, Pd = prod(range(67348, 67358)), prod(range(67473, 67483))
    W0, W1 = 624373932788019251, 522680876725222604
    previous, count, maxima = None, 0, [0, 0]
    for J in range(9941, 21500):
        num = prod(range(1048576+J-11, 1048576+J+1))*denominator
        den = 12*P*(a+b*J+c*J*J)
        value, remainder = divmod(num, den)
        need(0 <= remainder < den and den > 0, "exact positive floor")
        need(126*(67472+J)*Pd*denominator >= 4*den, "every HIGH gate")
        need(previous is None or value <= previous, "degree-stream monotonicity control")
        previous = value
        maxima[0] = max(maxima[0], value)
        if J >= 14000:
            maxima[1] = max(maxima[1], value)
        count += 1
    need(count == 11559 and maxima == [W0, W1], "whole interval maxima")
    budget = 2130706433**6//(1 << 128)
    near, v9, v10 = 2*67472, 10755802499540570, 156765527508668296
    N = budget-near+1
    values = ((3*N-W0+1)//2, (4*N-W0+2)//3, 2*N-W1)
    need(values == (100284125772880591, 158516326552340442, 27280579497297684),
         "independent population ceilings")
    need(981106*100000000000 < values[0], "actual pair-owner lower bound")
    need(3*N-W0 == 200568251545761181 and 3*N-W0-v9 == 189812449046220611
         and 3*N-W0-v10 == 43802724037092885, "independent nested mass")
    need((W0+v9+v10)//3+near < budget, "mixed-rank original payment")
    limit = 4*(budget-near+1)-W0-1
    need(limit == 475548979657021324 and (W0+limit)//4 == budget-near
         and (W0+limit+1)//4 == budget-near+1, "exact sufficient-census endpoint")
    need((3*981105, 981106, 981107//3) == (2943315, 981106, 327035),
         "complete-pair owner weights")
    for t, cap, W, expected in ((2, 0, W0, 208124644262808027),
                               (2, v9, W0, 215295179262501741),
                               (3, v10, W0, 273667628828640978)):
        paid = (W+t*cap)//(t+1)+near
        need(paid == expected < budget, "independent original payment")
        for wrong in (paid-1, paid+1):
            need(wrong != expected, "adjacent false total")
    need(values[0]-1149710068 > v9 and values[1]-1149710068 > v10
         and values[2]-1149710068 > v9, "strict post-deletion rank margins")
    print("PASS independent eight polynomial identities and", count, "integer degrees")
    print("PASS original payments, six wrong totals, strict mass ceilings and rank margins")
    print("Streaming controls do not replace the universal contraction and selection proofs")


if __name__ == "__main__":
    main()
