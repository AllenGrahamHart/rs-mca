"""Small exact sextic-field controls for the three full-row-space branches."""

P, DEGREE = 13, 6
ORDER = P**DEGREE
BETA = P


def digits(x):
    out = []
    for _ in range(DEGREE):
        out.append(x % P)
        x //= P
    return out


def pack(values):
    return sum((value % P)*P**i for i, value in enumerate(values))


def add(x, y):
    return pack([a+b for a, b in zip(digits(x), digits(y))])


def neg(x):
    return pack([-a for a in digits(x)])


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    a, b = digits(x), digits(y)
    result = [0]*DEGREE
    for i, c in enumerate(a):
        if c:
            for j, d in enumerate(b):
                result[(i+j) % DEGREE] += c*d*(2 if i+j >= DEGREE else 1)
    return pack(result)


def power(x, exponent):
    result = 1
    while exponent:
        if exponent & 1:
            result = mul(result, x)
        x = mul(x, x)
        exponent //= 2
    return result


def inverse(x):
    assert x
    result = power(x, ORDER-2)
    assert mul(x, result) == 1
    return result


def rank_prime(matrix):
    matrix = [row[:] for row in matrix]
    pivot = 0
    for col in range(len(matrix[0])):
        found = next((i for i in range(pivot, len(matrix)) if matrix[i][col] % P), None)
        if found is None:
            continue
        matrix[pivot], matrix[found] = matrix[found], matrix[pivot]
        scale = pow(matrix[pivot][col] % P, -1, P)
        matrix[pivot] = [value*scale % P for value in matrix[pivot]]
        for i in range(len(matrix)):
            if i != pivot:
                scale = matrix[i][col] % P
                matrix[i] = [(a-scale*b) % P for a, b in zip(matrix[i], matrix[pivot])]
        pivot += 1
        if pivot == len(matrix):
            break
    return pivot


def evaluate(poly, x):
    return add(poly[0], mul(poly[1], x))


def row_constraints(row, pairs):
    a, b, c, d = row
    values = []
    for (u0, u1), (v0, v1) in pairs[1:]:
        product = [add(mul(a, u0), mul(c, v0)),
                   add(add(mul(a, u1), mul(b, u0)), add(mul(c, v1), mul(d, v0))),
                   add(mul(b, u1), mul(d, v1))]
        values.extend(coefficient for value in product for coefficient in digits(value)[1:])
    return values


def audit_case(name, pairs, basis_indices, expected_labels):
    columns = []
    for position in range(24):
        row = [0]*4
        row[position//6] = P**(position % 6)
        columns.append(row_constraints(row, pairs))
    matrix = [list(row) for row in zip(*columns)]
    dimension = 24-rank_prime(matrix)
    assert dimension == len(basis_indices)
    basis = []
    for position in basis_indices:
        row = [0]*4
        row[position] = 1
        assert not any(row_constraints(row, pairs))
        basis.append(row)
    receiver = [tuple(evaluate(poly, x) for poly in pairs[x//3]) for x in range(9)]
    cores = [{x for x in range(9) if receiver[x] == tuple(evaluate(poly, x) for poly in pair)}
             for pair in pairs]
    assert cores == [set(range(3)), set(range(3, 6)), set(range(6, 9))]
    records = {}
    for owner, pair in enumerate(pairs):
        for x in set(range(9))-cores[owner]:
            du, dv = (sub(receiver[x][i], evaluate(pair[i], x)) for i in range(2))
            if dv:
                gamma = mul(neg(du), inverse(dv))
                records.setdefault(gamma, (owner, sorted(cores[owner])+[x]))
    assert len(records) == expected_labels
    for gamma, (owner, support) in records.items():
        a, b = pairs[owner]
        h = [add(a[i], mul(gamma, b[i])) for i in range(2)]
        assert all(add(receiver[x][0], mul(gamma, receiver[x][1])) == evaluate(h, x)
                   for x in support)
        assert sum(receiver[x][1] != evaluate(b, x) for x in support) == 1
        assert all(receiver[x] == tuple(evaluate(poly, x) for poly in pairs[owner])
                   for x in support[:3])
        assert receiver[support[-1]] != tuple(evaluate(poly, support[-1]) for poly in pairs[owner])
    expected_rank = {"ZERO": 0, "CYCLIC": 1, "RICH": 2}[name]
    for x in range(9):
        evaluations = [digits(add(row[0], mul(x, row[1])))+
                       digits(add(row[2], mul(x, row[3]))) for row in basis]
        assert (rank_prime(evaluations) if evaluations else 0) == expected_rank
    print(name, "full row-space dimension", dimension, "point rank", expected_rank,
          "actual distinct finite low-core labels", len(records))


def verify():
    assert power(BETA, 6) == 2 and power(BETA, P) == mul(4, BETA)
    assert power(BETA, P**6) == BETA
    assert all(power(BETA, P**d) != BETA for d in (1, 2, 3))
    beta2, beta3 = power(BETA, 2), power(BETA, 3)
    zero = [([0, 0], [0, 0]), ([BETA, 0], [0, 1]), ([0, beta2], [beta3, 0])]
    cyclic = [([0, 0], [0, 0]), ([1, 0], [0, BETA]), ([0, 1], [beta2, 0])]
    rich = [([0, 0], [0, 0]), ([1, 0], [1, 0]), ([1, 0], [2, 0])]
    audit_case("ZERO", zero, [], 17)
    audit_case("CYCLIC", cyclic, [0, 1], 17)
    audit_case("RICH", rich, [0, 1, 2, 3], 3)
    source = [BETA, 0, 0]
    assert all(mul(x, value) == 0 for x, value in enumerate(source))
    # E-values of Q at 1,2 determine every possible degree-<2 offset candidate.
    for value1 in range(P):
        for value2 in range(P):
            q0 = (2*value1-value2) % P
            assert sub(source[0], q0) >= P
    print("PASS: admissible row X and failure of its quotient at an uncovered point")
    print("PASS: explicit degree-six field and all full-row-space controls; no deployed upper inferred")


if __name__ == "__main__":
    verify()
