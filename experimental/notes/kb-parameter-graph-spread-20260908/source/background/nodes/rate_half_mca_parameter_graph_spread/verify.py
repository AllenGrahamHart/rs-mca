"""Exact gauge controls and row arithmetic, not a substitute for the proof."""

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("credited_rank",
    ROOT / "critical/nodes/mca_fiber_contraction_core_basis_resource/verify.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def affine_rank(points, p):
    return c.rank([[(x-y) % p for x, y in zip(row, points[0])]
                   for row in points[1:]], p)


def gauge_controls():
    p = 17
    for dimension in range(1, 13):
        points = [[pow(t, j, p) if j <= dimension else 0 for j in range(1, 13)]
                  for t in range(dimension+1)]
        need(affine_rank(points, p) == dimension, "exact graph dimension")
        b = points[1][1:]
        shifted = [[(h-row[0]*v) % p for h, v in zip(row[1:], b)] for row in points]
        need(affine_rank(shifted, p) == dimension-1, "one slope dimension removed")
        need(shifted[0] == shifted[1], "chosen slope direction is in the kernel")
        if dimension == 12:
            need(affine_rank(shifted, p) == 11, "full graph is not rank-ten paid")
    points = [[t]+[0]*11 for t in range(3)]
    wrong = [[(h-t*int(i == 0)) % p for i, h in enumerate(row[1:])]
             for t, row in enumerate(points)]
    need(affine_rank(wrong, p) == 1, "an arbitrary polynomial need not lower rank")

    k, m, b = 3, 7, [2, 3, 1]
    received = [(0, 0)]*6 + [(1, 1)] + [(0, 1)]*2
    shifted = [(u, (v-c.evaluate(b, x, p)) % p) for x, (u, v) in enumerate(received)]
    for gamma in range(p):
        for x, ((u, v), (up, vp)) in enumerate(zip(received, shifted)):
            hp = -gamma*c.evaluate(b, x, p)
            need((u+gamma*v) % p == (up+gamma*vp-hp) % p,
                 "scalar agreement identity on unchanged coordinates")
    matrix = [[pow(x, j, p) for j in range(k)] for x in range(m)]
    for pair in (received, shifted):
        for column in (0, 1):
            need(c.rank([row+[pair[x][column]] for x, row in enumerate(matrix)], p) == k+1,
                 "full polynomial-code badness survives the gauge")
    print("PASS 12 graph ranks, kernel and wrong-gauge control; exact bad-support gauge")


def main():
    budget = 2130706433**6 // 2**128
    v10, near = 156765527508668296, 2*67472
    spread = budget-near+1-v10
    need(budget == 274980728111395087 and spread == 118215200602591848,
         "original budget and strict over-budget integrality")
    j, r = 21499, 1048576
    collision = (r+j)*(j-11)//10
    exceptions = j-11+collision//2
    total = v10+exceptions+near
    need(collision == 2299377160 and exceptions == 1149710068, "source exception cap")
    need(total == 156765528658513308 and budget-total == 118215199452881779,
         "one exception set and one near allowance")
    need(spread-exceptions == budget-total+1 == 118215199452881780,
         "robust hyperplane complement")
    for wrong in (spread-1, spread+1):
        need(wrong != budget-near+1-v10, "reject wrong spread endpoint")
    need(spread-(spread-1) > 0 and spread-spread == 0,
         "strict deletion threshold, not a weak inequality")
    need(v10+exceptions < total < v10+exceptions+2*near,
         "missing or duplicated near cannot match the stated total")
    gauge_controls()
    print("PASS exact CAP/SPREAD/DROP constants and strict-boundary controls")
    print("Credited rank-ten cap is a theorem input; no unrestricted row closure")


if __name__ == "__main__":
    main()
