"""Independent partition and polynomial-coefficient audit of the endpoint step."""

from fractions import Fraction as Q


def need(ok, message):
    if not ok:
        raise ValueError(message)


def partitions(total, limit=None):
    if total == 0:
        yield ()
        return
    for first in range(min(total, limit or total), 0, -1):
        for tail in partitions(total-first, first):
            yield (first,)+tail


def add(a, b):
    return [(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


def scale(a, s):
    return [s*x for x in a]


def multiply(a, b):
    out = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def substitute(f, a):
    out, power = [Q(0)], [Q(1)]
    for c in f:
        out = add(out, scale(power, c))
        power = multiply(power, a)
    return out


def main():
    counts, derivative_cases, tight = 0, 0, 0
    for r in range(4, 7):
        t = r-2
        for k in range(r, 9):
            for d in (k, k+1):
                n = d+k
                for c in (Q(0), Q(1), Q(3)):
                    a, b = Q(-2), d*c+2
                    f = lambda x: a+b*x+c*x*x
                    spike = (k-r+1)*f(r-1)+(d+r-1)*f(k-1)
                    equal = n*f(Q((r-2)*k+1, r-1))
                    polynomial = add(multiply([k-1, -t], substitute([a, b, c], [1, t])),
                                     multiply([d+1, t], substitute([a, b, c], [k, -1])))
                    second = [2*polynomial[2], 6*polynomial[3]]
                    expected = [2*(-b*t*(t+1)+c*(d+t*(t-2)*k-3*t*t+1)),
                                -6*c*t*(t*t-1)]
                    need(second == expected, "derivative coefficient identity")
                    need(second[0]+second[1] <= 0 and second[1] <= 0, "global b concavity")
                    derivative_cases += 1
                    for sizes in partitions(n):
                        if len(sizes) < r or sum(sizes[:r-1]) > k-1:
                            continue
                        moment = sum(s*s for s in sizes)
                        bound = max(Q(n*(k-1), r-1), n+(k-r+1)*(k-r))
                        need(moment <= bound, "fiber second moment")
                        value = sum(s*f(k-s) for s in sizes)
                        need(value >= min(spike, equal), "quadratic endpoint lower bound")
                        tight += value == min(spike, equal)
                        counts += 1
    need(tight > 0 and counts > 100 and derivative_cases == 72, "nonvacuous census")
    print("PASS:", counts, "partition inequalities;", derivative_cases,
          "independent derivative identities;", tight, "tight endpoint controls")
    print("Partition realizability is not assumed or established by this relaxation audit")


if __name__ == "__main__":
    main()
