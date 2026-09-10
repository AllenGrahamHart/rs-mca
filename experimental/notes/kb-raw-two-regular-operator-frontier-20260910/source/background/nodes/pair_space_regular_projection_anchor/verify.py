"""Small exact controls for the strict regular-anchor and finite-chart guards."""


def need(ok, why):
    if not ok:
        raise ValueError(why)


def rref(matrix, prime):
    a = [[x % prime for x in row] for row in matrix]
    pivots, row = [], 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inverse = pow(a[row][col], -1, prime)
        a[row] = [v*inverse % prime for v in a[row]]
        for i in range(len(a)):
            if i != row:
                coefficient = a[i][col]
                a[i] = [(x-coefficient*y) % prime for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, pivots


def kernel(matrix, prime):
    reduced, pivots = rref(matrix, prime)
    result = []
    for free in range(len(matrix[0])):
        if free in pivots:
            continue
        vector = [0]*len(matrix[0])
        vector[free] = 1
        for i, pivot in enumerate(pivots):
            vector[pivot] = -reduced[i][free] % prime
        result.append(vector)
    return result


def main():
    prime, losses = 101, []
    # Coefficients are for (1,X,X^2); W has columns (1,0),(X,1),(X^2,0),(0,X^2).
    for x in range(prime):
        evaluation = [[1, x, x*x, 0], [0, 1, 0, x*x]]
        need(len(rref(evaluation, prime)[1]) == 2, "ordinary joint-good coordinate")
        section = kernel(evaluation, prime)
        need(len(section) == 2, "pair section dimension")
        projected_zero = [[v[i] for v in section] for i in range(3)]
        projected_rank = len(rref(projected_zero, prime)[1])
        if x == 0:
            need(projected_rank == 1, "joint-good does not imply regular-preserving")
            # Both projected columns stay multiples of X^2 for EVERY formal z.
            need(all(v[0] == v[1] == 0 for v in section), "formal loss, not one bad finite chart")
            losses.append(x)
        else:
            need(projected_rank == 2, "a finite full-rank chart proves generic fullness")
    need(losses == [0] and len(losses) <= 3+3-4, "repaired root bound")
    for z in range(prime):
        projection = [[1, z, 0, 0], [0, 1, 0, 0], [0, 0, 1, z]]
        need(len(rref(projection, prime)[1]) == 3, "initial constant determinant-one minor")
    # At x=1 the operator sends (X^2-1) to0 and (1-X) to(X^2-1).
    operator = [[0, 1], [0, 0]]
    need(any(any(row) for row in operator), "nonzero nilpotent retained")
    need(all(sum(operator[i][k]*operator[k][j] for k in range(2)) == 0
             for i in range(2) for j in range(2)), "operator square is zero")
    need(all((z*z+2) % prime != 0 for z in range(prime)), "nonsplit quadratic operator control")
    # diag(z,1+z) is formally regular but has no invertible chart in F2.
    need(all(z*(1+z) % 2 == 0 for z in range(2)), "small-field finite-chart obstruction")
    print("PASS 101 joint-good coordinates; one formal-regularity loss; repaired set {0}")
    print("PASS nilpotent/nonsplit controls and the necessary finite-field chart guard")
    print("Linear-algebra fixtures only, not full-code-bad MCA sources or universal proofs by sampling")


if __name__ == "__main__":
    main()
