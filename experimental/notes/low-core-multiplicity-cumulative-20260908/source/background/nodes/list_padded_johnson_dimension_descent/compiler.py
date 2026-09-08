"""Exact, constant-memory certificate selection for ordinary affine LIST."""


def compile_cap(r, w, k_max, dimension):
    assert 1 <= w <= r and 0 <= dimension <= k_max
    coefficient = r - 2 * w - 1
    limit = k_max
    if coefficient > 0:
        limit = min(limit, (w * w + r - 1) // coefficient)
    assert 1 <= limit <= k_max

    def johnson(k):
        denominator = (w + k) ** 2 - (r + k) * (k - 1)
        assert denominator > 0
        return (r + k) * (w + 1) // denominator

    upper = 1
    trace = []
    for rank in range(1, dimension + 1):
        def endpoint(k):
            return (r + k + 1) * upper // (w + k + 1)

        low, high = 1, limit
        while high - low > 1:
            middle = (low + high) // 2
            if johnson(middle) >= endpoint(middle):
                high = middle
            else:
                low = middle
        options = [((r + rank) * upper // (w + rank), 0)]
        for degree in (low, high):
            bound = johnson(degree)
            if degree < k_max:
                bound = max(bound, endpoint(degree))
            options.append((bound, degree))
        upper, degree = min(options)
        trace.append((rank, degree, upper))
    return upper, trace
