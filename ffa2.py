def keys(i, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    p = tuple(i)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(p[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(p[i] for i in indices)
l="bcdfghjklmnpqrstvwxyz"
keys('abcd',2)
