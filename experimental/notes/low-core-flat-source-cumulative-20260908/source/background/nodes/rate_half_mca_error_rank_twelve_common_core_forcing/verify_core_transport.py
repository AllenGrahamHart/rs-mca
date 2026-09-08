"""One bounded actual rank-twelve family, including a nonuniversal common zero."""

import importlib.util
from itertools import combinations
from pathlib import Path


P = 23


def polynomial(roots):
    coefficients = [1]
    for root in roots:
        new = [0] * (len(coefficients) + 1)
        for i, value in enumerate(coefficients):
            new[i] = (new[i] - root * value) % P
            new[i + 1] = (new[i + 1] + value) % P
        coefficients = new
    return coefficients


def evaluate(coefficients, x):
    result = 0
    for value in reversed(coefficients):
        result = (result * x + value) % P
    return result


def rank(rows):
    if not rows:
        return 0
    rows = [list(row) for row in rows]
    pivot_row = 0
    for col in range(len(rows[0])):
        found = next((i for i in range(pivot_row, len(rows)) if rows[i][col]), None)
        if found is None:
            continue
        rows[pivot_row], rows[found] = rows[found], rows[pivot_row]
        inv = pow(rows[pivot_row][col], -1, P)
        rows[pivot_row] = [value * inv % P for value in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row:
                factor = rows[i][col]
                rows[i] = [(a - factor*b) % P for a, b in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def affine_rank(rows):
    return rank([[(a-b) % P for a, b in zip(row, rows[0])] for row in rows[1:]])


def main():
    helper_path = Path(__file__).parents[1] / 'mca_scalar_agreement_dimension_descent/verify.py'
    spec = importlib.util.spec_from_file_location('support_checks', helper_path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    helper.P = P
    domain, tail, zeros, good = list(range(20)), list(range(3, 20)), [0, 1, 2], [0, 1]
    k, m = 14, 15
    common_locator = polynomial(zeros)
    bins = {}
    for support in combinations(tail, 13):
        coeff = polynomial(support)
        bins.setdefault(coeff[11], {}).setdefault(coeff[12], []).append(coeff)
    checked = 0
    for fixed in sorted(bins):
        by_slope = bins[fixed]
        # Choose independent lifted explanation directions with distinct labels.
        selected, directions = [], []
        base_gamma = min(by_slope)
        base = by_slope[base_gamma][0]
        selected.append((base_gamma, base))
        for gamma in sorted(by_slope):
            if gamma == base_gamma:
                continue
            candidates = by_slope[gamma]
            chosen = candidates[gamma % len(candidates)]
            for coeff in candidates:
                direction = [(gamma-base_gamma) % P] + [(base[i]-coeff[i]) % P for i in range(11)]
                if rank(directions + [direction]) > len(directions):
                    directions.append(direction)
                    chosen = coeff
                    break
            selected.append((gamma, chosen))
        if len(directions) != 12:
            continue
        exception = base_gamma
        r0 = [evaluate(common_locator, x) * (x**13 + fixed*x**11) % P for x in domain]
        r1 = [evaluate(common_locator, x) * x**12 % P for x in domain]
        r0[2], r1[2] = (-exception) % P, 1
        records = []
        for gamma, coeff in selected:
            h = [evaluate(common_locator, x) * evaluate([(-v) % P for v in coeff[:11]], x) % P for x in domain]
            agreement = [x for x in domain if (r0[x]+gamma*r1[x]-h[x]) % P == 0]
            support = helper.bad_subset(agreement, r1, k, m)
            if support is not None:
                assert helper.contained(domain, h, k)
                records.append((gamma, h, agreement, support))
        errors = [[(r0[x]+gamma*r1[x]-h[x]) % P for x in domain] for gamma, h, _, _ in records]
        if not records or affine_rank(errors) != 12 or exception not in {row[0] for row in records}:
            continue
        gamma0, h0 = records[0][:2]
        gamma1, h1 = records[1][:2]
        b = [(v-u) * pow((gamma1-gamma0) % P, -1, P) % P for u, v in zip(h0, h1)]
        hstar = [(h0[x]-gamma0*b[x]) % P for x in domain]
        gauged = [[(h[x]-gamma*b[x]) % P for x in domain] for gamma, h, _, _ in records]
        assert affine_rank(gauged) == 11
        tset = [x for x in domain if all(row[x] == hstar[x] for row in gauged)]
        global_core = [x for x in domain if all(row[x] == 0 for row in errors)]
        good_zeros = [x for x in tset if r0[x] == hstar[x] and r1[x] == b[x]]
        assert tset == zeros and global_core == good_zeros == good
        assert sum(r1[x] != b[x] for x in tset) == 1
        # Normalize all common evaluation zeros, removing the one exceptional slope.
        child_r1 = [0] * 20
        for x in tail:
            child_r1[x] = (r1[x]-b[x]) * pow(evaluate(common_locator, x), -1, P) % P
        retained = 0
        for (gamma, _, agreement, _), hg in zip(records, gauged):
            if gamma == exception:
                continue
            assert [x for x in agreement if x in zeros] == good
            child_h = [(hg[x]-hstar[x]) * pow(evaluate(common_locator, x), -1, P) % P for x in tail]
            assert helper.contained(tail, child_h, 11)
            support = helper.bad_subset([x for x in agreement if x in tail], child_r1, 11, 13)
            assert support is not None and len(support) == 13
            retained += 1
        assert retained == len(records)-1
        # Cancel only the actual shared core: keep EVERY slope and error rank.
        remaining = [x for x in domain if x not in good]
        locator_good = polynomial(good)
        shortened_errors = [[row[x] * pow(evaluate(locator_good, x), -1, P) % P for x in remaining] for row in errors]
        assert affine_rank(shortened_errors) == 12
        assert not any(all(row[i] == 0 for row in shortened_errors) for i in range(len(remaining)))
        for (gamma, _, agreement, _), hg in zip(records, gauged):
            values = [0]*20
            for x in remaining:
                values[x] = (r1[x]-b[x]) * pow(evaluate(locator_good, x), -1, P) % P
            support = helper.bad_subset([x for x in agreement if x in remaining], values, 12, 13)
            assert support is not None
        checked = len(records)
        print(f'PASS: actual affine error rank 12 on F_23; {checked} selected slopes; '
              'explanation rank 11; common evaluation zeros 3, shared complete core 2; '
              'one exceptional slope removed in zero normalization; all slopes and rank '
              'preserved by shared-core cancellation')
        break
    assert checked, 'No full-rank control was obtained; this is not a passing test.'


if __name__ == '__main__':
    main()
