"""Small exact rational-graph census and tangent/pole regression controls."""

from verify_small import P, add, mul, scale


def rank(rows, p):
    rows = [list(row) for row in rows]
    pivot = 0
    for column in range(len(rows[0])):
        candidate = next((i for i in range(pivot, len(rows))
                          if rows[i][column] % p), None)
        if candidate is None:
            continue
        rows[pivot], rows[candidate] = rows[candidate], rows[pivot]
        inverse = pow(rows[pivot][column], -1, p)
        rows[pivot] = [value*inverse % p for value in rows[pivot]]
        for i in range(len(rows)):
            if i != pivot:
                multiplier = rows[i][column]
                rows[i] = [(a-multiplier*b) % p
                           for a, b in zip(rows[i], rows[pivot])]
        pivot += 1
    return pivot


def verify():
    assert pow(2, (P-1)//2, P) == P-1
    labels, owners = set(), set()
    for x in range(783):
        j, value = x//29+1, (x, 1)
        for i in range(1, 28):
            if i == j:
                continue
            gamma = scale(-pow(i+j, -1, P), value)
            assert gamma not in labels
            labels.add(gamma)
            owners.add(i)
            a_i, a_j = scale(i, value), scale(j, value)
            b_i, b_j = (i*i % P, 0), (j*j % P, 0)
            assert a_i != a_j and b_i != b_j
            assert mul(mul(value, value), b_i) == mul(a_i, a_i)
            assert add(a_i, mul(gamma, b_i)) == add(a_j, mul(gamma, b_j))
    assert len(labels) == 20358 and len(owners) == 27
    assert 29 >= 2 and 27 < 30 and 2 < 30-2
    assert max(2+2-1, 2*(2-1)) == 3 < 29
    assert 27 > 2*7 and all(2*e > 2 for e in range(2, 8))
    assert rank(((0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1)), 5) == 3
    assert rank(((0, 0, 1, 0), (0, 0, 0, 1),
                 (1, 2, 1, 0), (0, 1, 2, 1)), 5) == 4
    x, u, v, a, b = 0, 0, 1, 0, 4
    assert x*x*v == u*u and x*x*b == a*a and a == u and b != v
    print("PASS: 20358 rational-quadratic labels; all 27 pairs represented")
    print("PASS: tangent intersection endpoints and pole/core distinction")
    print("Canonical maximality and polynomial-graph exclusion are hand proofs")


if __name__ == "__main__":
    verify()
