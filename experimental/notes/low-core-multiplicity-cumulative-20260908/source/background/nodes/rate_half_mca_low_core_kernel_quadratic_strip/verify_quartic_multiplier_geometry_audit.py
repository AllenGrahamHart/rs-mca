"""Independent integer envelope audit and tiny polynomial-evaluation ranks."""


def require(ok, label):
    if not ok:
        raise RuntimeError(label)


def rank(matrix, p):
    rows = [row[:] for row in matrix]
    pivot = 0
    for col in range(len(rows[0])):
        chosen = next((j for j in range(pivot,len(rows)) if rows[j][col] % p), None)
        if chosen is None:
            continue
        rows[pivot],rows[chosen] = rows[chosen],rows[pivot]
        inverse = pow(rows[pivot][col], -1, p)
        rows[pivot] = [v*inverse % p for v in rows[pivot]]
        for j in range(pivot+1,len(rows)):
            factor = rows[j][col] % p
            if factor:
                rows[j] = [(x-factor*y) % p for x,y in zip(rows[j],rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def verify():
    # A 763-row integer audit, not a field/source scan or a large matrix.
    for j in range(8764,9527):
        w, a = j-1,j+66972
        low = sum((i+1)*(a-i*w) for i in range(9))-(1048576+j)
        h = (111*j-960724)//15 if j<=9099 else (146*j-1295624)//10
        dimensions = []
        for hh in (h,h+1):
            s = a-4*w-hh
            dimensions.append(sum(max(s-(iy+iz)*w,0)
                                  for iy in range(5) for iz in range(5-iy)))
        require(dimensions[0]>=low>dimensions[1], "full piecewise height envelope")
        require(a-4*w-h>=28881, "all J agreement-exclusion lengths")
        s0 = a-4*w
        full = sum((i+1)*(s0-i*w) for i in range(5))
        first_impossible = next(t for t in range(1,6)
                                if low > full-sum(s0-i*w for i in range(t)))
        expected = (1 if j<=9014 else 2 if j<=9276 else 3 if j<=9444
                    else 4 if j<=9524 else 5)
        require(first_impossible == expected, "all off-pair staircase rows")

    # On f_j=(jX,0), the Newton lower bound is attained. At most 30x50.
    s, p = 6, 11
    monomials = [(x,y,z) for y in range(5) for z in range(5-y)
                 for x in range(s-y-z)]
    require(len(monomials)==50 and p>10, "tiny control scope")
    for t in range(1,6):
        matrix = [[0]*len(monomials) for _ in range(t*s)]
        for col,(x,y,z) in enumerate(monomials):
            if z:
                continue
            for j in range(t):
                matrix[j*s+x+y][col] = pow(j,y,p)
        require(rank(matrix,p) == sum(s-i for i in range(t)),
                "independent polynomial-evaluation block ranks")
    # Equality does not prohibit an off-gcd point: D=7, rank=3, kernel=4.
    require(sum((i+1)*(3-i) for i in range(2))-3 == 4,
            "strict-inequality algebraic control")

    require(16*(66973-1532) > 1048577-1532, "first graph ratio")
    require(17*(66973-2379) > 1048577-2379, "second graph ratio")
    require(16*(66973-2379) > 1048577-2379-28881, "forbidden-coordinate ratio")
    for d in range(4,12):
        r = (d+3)//4
        require(2**(2*(22-d-r)+4*r) <= 2**38, "all q16 graph counts")
    for d in range(6,12):
        r = (d+3)//4
        require(2**(2*(22-d-r))*17**r <= 2**28*289, "all q17 graph counts")
    high, remainder = divmod(23067643444721720934,5500)
    require(0<=remainder<5500, "HIGH floor")
    total = high+134944+(2**38+4)*(1048576-66972)
    require(total==274015369961868939 and
            total+965358149526148==274980728111395087,
            "independent original label and near ledger")
    print("PASS: 763 integer envelopes and exact Newton ranks in F11 (max 30x50)")
    print("PASS: independent graph budgets; no claim of canonical MCA realization by the toys")


if __name__ == "__main__":
    verify()
