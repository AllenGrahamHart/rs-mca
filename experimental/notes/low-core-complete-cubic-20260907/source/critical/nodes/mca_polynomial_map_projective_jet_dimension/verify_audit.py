"""Independent integer audit and tiny algebraic gate controls."""

from math import comb


def reject(call):
    try:
        call()
    except AssertionError:
        return
    raise AssertionError("invalid mutation accepted")


def rank(matrix, p):
    rows = [[entry % p for entry in row] for row in matrix]
    pivot = 0
    for column in range(len(rows[0])):
        found = next((i for i in range(pivot, len(rows)) if rows[i][column]), None)
        if found is None:
            continue
        rows[pivot], rows[found] = rows[found], rows[pivot]
        inverse = pow(rows[pivot][column], -1, p)
        rows[pivot] = [v * inverse % p for v in rows[pivot]]
        for i in range(len(rows)):
            if i != pivot:
                factor = rows[i][column]
                rows[i] = [(x-factor*y) % p for x, y in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def jets(degrees, points, order, p):
    return [[comb(d, j)*pow(x, d-j, p) % p if d >= j else 0
             for d in degrees] for x in points for j in range(order)]


def cap_gate(e, r, cap):
    assert r == 1 + 10 // e
    numerator, denominator = e**(11-r)*63**r, 4**r
    assert cap*denominator <= numerator < (cap+1)*denominator


def audit():
    for e, r, cap in ((2,6,488464861), (3,4,134577053),
                      (5,3,1526165771), (9,2,96104495052)):
        cap_gate(e, r, cap)
    reject(lambda: cap_gate(3, 3, 134577053))
    reject(lambda: cap_gate(9, 2, 96104495051))
    assert rank(jets((0,1,3,4), (1,2), 2, 101), 101) == 4
    assert rank(jets((0,2), (1,100), 1, 101), 101) == 1
    assert rank(jets((0,1,3), (1,), 3, 3), 3) == 2
    for c in range(3):
        for d in range(3):
            for x in range(3):
                assert (c+d*x)**3 % 3 == (c**3+d**3*x**3) % 3
    for c in range(1, 101):
        d = pow(2*c, -1, 101)
        assert 2*c*d % 101 == 1
    # Sharp family: h of degree <=3, h^3 of degree <=9, s=10.
    assert 1 + (10-1)//3 == 4 and 10//3 == 3
    base = 23067643444721720934//501 + 134944
    for k in (4801,169999):
        numerator = 132*comb(1048576+k,12)
        denominator = (67472+k)*comb(67482,10)
        assert numerator <= 23067643444721720934*denominator
    total = base + 981604*96104495052
    budget = pow(2130706433,6)//pow(2,128)
    assert total == 140379757249624860
    assert budget-total == 134600970861770227
    print("PASS: independent integer caps, jet ranks, characteristic and offset controls")
    print("Two invalid cap mutations rejected; finite tests do not prove dimension")


if __name__ == "__main__":
    audit()
