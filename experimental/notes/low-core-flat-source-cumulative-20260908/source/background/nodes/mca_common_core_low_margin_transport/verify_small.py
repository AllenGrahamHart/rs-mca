"""Actual F_17 cancellation, minimizer, kernel and reselection controls."""

from itertools import product

P = 17


def eval_poly(coefficients, x):
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % P
    return value


def rref(matrix):
    rows = [list(map(lambda x: x % P, row)) for row in matrix]
    if not rows:
        return ()
    pivot = 0
    for column in range(len(rows[0])):
        selected = next((i for i in range(pivot, len(rows)) if rows[i][column]), None)
        if selected is None:
            continue
        rows[pivot], rows[selected] = rows[selected], rows[pivot]
        inverse = pow(rows[pivot][column], -1, P)
        rows[pivot] = [value * inverse % P for value in rows[pivot]]
        for i in range(len(rows)):
            if i != pivot:
                multiple = rows[i][column]
                rows[i] = [(a - multiple * b) % P for a, b in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return tuple(tuple(row) for row in rows if any(row))


def interpolate(points, values):
    rows = [[pow(x, j, P) for j in range(len(points))] + [value % P]
            for x, value in zip(points, values)]
    reduced = rref(rows)
    assert len(reduced) == len(points)
    return tuple(row[-1] for row in reduced)


def relation_constraints(points, u, v, ell, threshold):
    columns = []
    for received in (u, v):
        for power in range(ell + 1):
            columns.append(interpolate(points, [received[x] * pow(x, power, P) % P for x in points])[threshold:])
    return rref(list(zip(*columns)))


def minimizers(support, v, factor):
    scores = [(sum(v[x] != factor(x) * eval_poly(b, x) % P for x in support), b)
              for b in product(range(P), repeat=2)]
    raw = min(score for score, _ in scores)
    return raw, {b for score, b in scores if score == raw}


def is_polynomial(support, values, degree_bound):
    fit = interpolate(support[:degree_bound], [values[x] for x in support[:degree_bound]])
    return all(eval_poly(fit, x) == values[x] for x in support)


def verify():
    domain = list(range(14))
    lifted_domain = domain + [15]
    factor = lambda x: (x - 15) % P
    gauge = lambda x: (1 + x * x) % P
    u = {x: 0 if x < 6 else x for x in range(12)}
    v = {x: 0 if x < 6 else 16 for x in range(12)}
    u.update({12: 4, 13: 8})
    v.update({12: 1, 13: 2})
    lifted_u = {x: (gauge(x) + factor(x) * u.get(x, 0)) % P for x in lifted_domain}
    lifted_v = {x: factor(x) * v.get(x, 0) % P for x in lifted_domain}
    records = []
    for gamma in range(12):
        h = ((-gamma) % P, 1) if gamma < 6 else (0, 0)
        support = list(range(6, 12)) + [gamma] if gamma < 6 else list(range(6)) + [gamma]
        records.append((gamma, h, support))
    records.append((13, (0, 0), list(range(6)) + [12]))
    child_union, lifted_union = set(), set()
    shared = set(lifted_domain)
    for gamma, h, support in records:
        saturated = support + [15]
        assert len(set(support)) == 7 and len(set(saturated)) == 8
        assert all((u[x] + gamma * v[x] - eval_poly(h, x)) % P == 0 for x in support)
        assert not is_polynomial(support, v, 3)
        assert not is_polynomial(saturated, lifted_v, 4)
        raw, choices = minimizers(support, v, lambda x: 1)
        assert (raw, choices) == minimizers(saturated, lifted_v, factor)
        assert raw == 1 and len(choices) == 1
        b = next(iter(choices))
        child_core = {x for x in domain if v[x] == eval_poly(b, x)
                      and u[x] == (eval_poly(h, x) - gamma * eval_poly(b, x)) % P}
        original_core = {x for x in lifted_domain if lifted_v[x] == factor(x) * eval_poly(b, x) % P
                         and lifted_u[x] == (gauge(x) + factor(x) * (eval_poly(h, x) - gamma * eval_poly(b, x))) % P}
        assert original_core == child_core | {15}
        child_union |= child_core
        lifted_union |= original_core
        shared &= {x for x in lifted_domain
                   if (lifted_u[x] + gamma * lifted_v[x] - gauge(x) - factor(x) * eval_poly(h, x)) % P == 0}
    assert shared == {15}
    assert child_union == set(range(12)) and lifted_union == child_union | {15}
    for ell in (0, 1, 2, 3):
        assert relation_constraints(sorted(child_union), u, v, ell, 3 + ell) == relation_constraints(sorted(lifted_union), lifted_u, lifted_v, ell, 4 + ell)
    # The row (1,X) survives a nonzero polynomial gauge and locator division.
    assert all((u[x] + x * v[x]) % P == 0 for x in child_union)
    old_support = list(range(6)) + [12, 13]
    saturated = list(range(6)) + [12, 15]
    assert not is_polynomial(old_support, lifted_v, 4)
    assert minimizers(old_support, lifted_v, factor) == (2, {(0, 0)})
    assert minimizers(saturated, lifted_v, factor) == (1, {(0, 0)})
    print("PASS: 13 saturated bad records, all minimizers, complete cores and four relation spaces")
    print("Unsaturated-selection control: raw changes from 2 to 1 on reselection")


if __name__ == "__main__":
    verify()
