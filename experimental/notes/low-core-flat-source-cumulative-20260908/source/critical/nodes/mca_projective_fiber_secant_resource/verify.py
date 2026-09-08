"""Actual small-field secant, zero-coordinate and distinct-fiber controls."""

from itertools import combinations, product
from math import factorial, prod

P = 17


def need(ok, why):
    if not ok:
        raise ValueError(why)


def rank(rows):
    a = [[x % P for x in row] for row in rows]
    if not a:
        return 0
    r = 0
    for c in range(len(a[0])):
        pivot = next((j for j in range(r, len(a)) if a[j][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inverse = pow(a[r][c], -1, P)
        a[r] = [v * inverse % P for v in a[r]]
        for j in range(r + 1, len(a)):
            scale = a[j][c]
            a[j] = [(x - scale * y) % P for x, y in zip(a[j], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def det(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])) % P


def fixture(shared):
    core, defect = ({1,16,2,3,4},15) if shared else ({1,16,2,15,3},4)
    u, v = {0:1}, {0:1}
    for x in range(1,P):
        alpha = 0 if x in core or x == defect else pow(x,3,P)
        beta = 0 if x in core else 1 if x == defect else pow(x,4,P)
        u[x], v[x] = (x*x+x*alpha) % P, x*beta % P
    return u,v


def exceptions(u,v):
    need(v[0] or u[0] != 0, "empty universal carrier core")
    exceptional = {(-u[0]*pow(v[0],-1,P)) % P} if v[0] else set()
    fibers = {}
    for x in range(1,P):
        fibers.setdefault(x*x % P, []).append(x)
    for fiber in fibers.values():
        for x,y in combinations(fiber,2):
            ax,bx = ((u[x]-x*x)*pow(x,-1,P)) % P, v[x]*pow(x,-1,P) % P
            ay,by = ((u[y]-y*y)*pow(y,-1,P)) % P, v[y]*pow(y,-1,P) % P
            if bx != by:
                exceptional.add((ay-ax)*pow((bx-by)%P,-1,P) % P)
    return exceptional, fibers


def source_control(shared):
    u,v = fixture(shared)
    exceptional, fibers = exceptions(u,v)
    need((0 in exceptional) == shared and 16 in exceptional, "defect/zero labels")
    sizes = [len(a) for a in fibers.values()]
    resource = 6*sum(prod(a) for a in combinations(sizes,3))
    need(resource == 2688 and len(exceptional) <= 9, "explicit resource/exception cap")
    normals = {x:[v[x],-x,-pow(x,3,P)] for x in range(P)}
    independent = forced = 0
    for xs in combinations(range(P),3):
        rows = [normals[x] for x in xs]
        denominator = det(rows)
        if not denominator:
            continue
        independent += 1
        gamma = det([[ (x*x-u[x]) % P, *normals[x][1:]] for x in xs])
        gamma = gamma*pow(denominator,-1,P) % P
        if 0 in xs or len({x*x % P for x in xs}) < 3:
            need(gamma in exceptional, "every non-distinct-fiber tuple is exceptional")
            forced += 1
    need(forced > 0, "exception charge is necessary")

    records = {}
    for gamma in range(P):
        for a,b in product(range(P),repeat=2):
            agreement = [x for x in range(P)
                         if (u[x]+gamma*v[x]-x*x-a*x-b*x**3) % P == 0]
            support = agreement[:6]
            if len(support) < 6:
                continue
            full = [[pow(x,i,P) for i in range(4)]+[v[x]] for x in support]
            if rank(full) == 5:
                records[gamma] = agreement
                break
    need(0 in records, "actual full-code-bad witness exists")
    owned, costs = set(), []
    for gamma, agreement in records.items():
        if gamma in exceptional:
            continue
        count = 0
        for xs in combinations(agreement,3):
            if not det([normals[x] for x in xs]):
                continue
            need(0 not in xs and len({x*x % P for x in xs}) == 3,
                 "surviving witness tuple has distinct nonzero fibers")
            need(xs not in owned, "distinct selected labels have disjoint tuples")
            owned.add(xs)
            count += 6
        need(count > 0, "full-rank bad support")
        costs.append(count)
    need(sum(costs) <= resource, "filtered summed resource")
    if costs:
        need(len(records) <= len(exceptional)+resource//min(costs), "whole label bound")
    if not shared:
        need(costs, "a surviving bad record is actually tested")
    broken = dict(v)
    broken[0] = 0
    wrong_u = dict(u)
    wrong_u[0] = 0
    try:
        exceptions(wrong_u,broken)
    except ValueError:
        pass
    else:
        raise ValueError("accepted a nonempty universal core")
    return len(records),len(costs),independent,forced


def histogram_controls():
    count = 0
    for length in range(1,6):
        for weights in product(range(1,5),repeat=length):
            exact = factorial(3)*sum(prod(xs) for xs in combinations(weights,3))
            slots,n = max(3,length),sum(weights)
            need(exact*slots**3 <= prod(slots-i for i in range(3))*n**3,
                 "whole histogram balance envelope")
            need(exact <= n*(n-1)*(n-2), "filtered count below whole-domain tuples")
            count += 1
    return count


def main():
    for shared in (True,False):
        print("SOURCE",shared,"records/survivors/independent/forced",source_control(shared))
    print("PASS",histogram_controls(),"exact fiber histograms; actual normalized F17 sources")
    print("Hand proof supplies generality; no original-field enumeration or Prize closure")


if __name__ == "__main__":
    main()
