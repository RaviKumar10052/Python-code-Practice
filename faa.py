def keys(i,n, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    p = tuple(i)
    n = len(p)
    if r ==0:
        return
    else:
        for i in range (0,n):
            del_list(p,i,new)
            x=keys(New,n-1,r-1)
l="bcdfghjklmnpqrstvwxyz"
keys(l,2)
