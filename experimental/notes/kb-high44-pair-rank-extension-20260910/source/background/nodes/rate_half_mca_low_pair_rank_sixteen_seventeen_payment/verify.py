"""Exact guarded descent and original-slope prices for two low-pair ranks."""

from fractions import Fraction as F
from math import prod

R, D, E, W = 1048576, 67472, 21499, 624373932788019251
BUDGET, NEAR, PENCIL = 274980728111395087, 134944, 261996525491320703


def need(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    expected = {7: (16, 192166560782635999), 23: (17, 270933399088173359)}
    for t, (rank, price) in expected.items():
        anchors, terminal = rank-11, 22-rank
        C, P, H = F(R-567500, D+1-t), max(F(9), F(607203, 67474-t)), F(R-E+2, D-E+2-t)
        need(1 <= C <= P and H <= P*P, "hereditary and determinant gates")
        stages = []
        for i in range(anchors):
            r, s = rank-2*i, 11-i
            need(s < r <= 2*s, "guarded rank-two anchor")
            need(D+9965-t > 9965+s-r, "positive agreement after bad anchors")
            stages.append((r, s, r-s))
        need((rank-2*anchors, 11-anchors) == (terminal, terminal), "equality child")
        one, two = C**terminal, H*P**(terminal-2)
        need((two > one) == (t == 7), "different dominant terminal types")
        count = prod(F(R+c, D-t+c) for c in range(1, anchors+1))*max(one, two)
        total = int(F(W, t+1)+F(t, t+1)*(R-D+t)*count)+NEAR
        need(total == price and max(total, PENCIL) < BUDGET, "whole original source price")
        need(t+1 <= 44 and 2130706433**6//2**128 == BUDGET, "unchanged HIGH and field")
        print("PASS P", t, "rank", rank, "stages", stages, "PAIR_FLOOR", int(count))
        print("BRANCH", total, "WHOLE_SOURCE", max(total, PENCIL), "RESERVE", BUDGET-max(total, PENCIL))
    need(22-17 == 5 and 22-18 == 4, "surviving regular projection exceptions")
    print("P7 rank17..22 and P23 rank18..22 remain; no full J, higher source rank or Prize closure")


if __name__ == "__main__":
    main()
