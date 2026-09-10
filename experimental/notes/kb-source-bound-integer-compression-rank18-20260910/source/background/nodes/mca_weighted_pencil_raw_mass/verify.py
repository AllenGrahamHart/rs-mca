"""Tiny actual-label control; not a full Prize source or universal proof."""

def need(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    domain = range(9)
    v = {x: int(x >= 3) for x in domain}
    gamma_at = {3: 2, 4: 2, 5: 3, 6: 4, 7: 4, 8: 4}
    u = {x: -gamma_at.get(x, 0)*v[x] for x in domain}
    supports = {2: {0, 3, 4}, 3: {1, 5}, 4: {0, 6, 7, 8}}
    core = {x for x in domain if u[x] == v[x] == 0}
    defects = {}
    for gamma, support in supports.items():
        need(all(u[x]+gamma*v[x] == 0 for x in support), "actual scalar agreements")
        defects[gamma] = {x for x in support if v[x] != 0}
    need(core == {0, 1, 2} and [len(defects[g]) for g in (2, 3, 4)] == [2, 1, 3], "raw data")
    need(all(not defects[g].intersection(defects[h]) for g in defects for h in defects if g != h),
         "same-pair original defects are disjoint")
    need(sum(map(len, defects.values())) == 9-len(core), "sharp zero-dimensional weight cap")
    low_weight = sum(len(d) for d in defects.values() if len(d) <= 2)
    need(low_weight == 3 and 2 in core and all(2 not in a for a in supports.values()),
         "complete-core anchor keeps owners even when selected supports omit it")
    print("PASS actual-label raw weights and complete-core/selected-support distinction")
    print("A bounded lemma fixture only; no full-code-bad Prize source is claimed")


if __name__ == "__main__":
    main()
