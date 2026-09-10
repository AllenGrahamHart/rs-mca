"""F101 exterior-product and divided-kernel controls; universal proof is separate."""

P = 101


def need(ok, why):
    if not ok:
        raise ValueError(why)


def pluecker(first, second):
    return {(i, j): (first[i]*second[j]-first[j]*second[i]) % P
            for i in range(4) for j in range(i+1, 4)}


def wedge(a, b):
    return (a[0, 1]*b[2, 3]-a[0, 2]*b[1, 3]+a[0, 3]*b[1, 2]
            +a[2, 3]*b[0, 1]-a[1, 3]*b[0, 2]+a[1, 2]*b[0, 3]) % P


def main():
    points = range(41)
    for compression in (False, True):
        exterior = {}
        for x in points:
            first, second = (([1, x, x*x, 0], [0, 0, 0, 1]) if compression else
                             ([1, x, 0, 0], [0, 1, x, x*x]))
            exterior[x] = pluecker(first, second)
            need(any(exterior[x].values()), "every evaluation is good")
        rank_one = []
        for x in points:
            relation = all(wedge(exterior[x], exterior[y]) == 0 for y in points)
            determinant_values = [0 if compression else -x*y % P for y in points]
            need(relation == all(v == 0 for v in determinant_values), "whole-kernel exterior criterion")
            if relation:
                rank_one.append(x)
            if not compression:
                for y in points:
                    first = ((x*x-x*y) % P, (y-x) % P)
                    second = ((x**3-x*x*y) % P, (y*y-x*x) % P)
                    need(first == ((y-x)*(-x) % P, (y-x) % P), "first divided kernel vector")
                    need(second == ((y-x)*(-x*x) % P, (y-x)*(y+x) % P), "second divided vector")
                    need((-x*(y+x)+x*x) % P == determinant_values[y], "divided determinant")
        need(rank_one == (list(points) if compression else [0]), "distinct exhaustive mechanisms")
    print("PASS compression and sparse F101 controls; actual sparse rank-one child set {0}")
    print("41 evaluation points exceed the degree-four witness bound; universal theorem is hand-proved")


if __name__ == "__main__":
    main()
