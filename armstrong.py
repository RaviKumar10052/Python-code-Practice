def armstrong(n):
    p=1
    while(p<=n):
        a = p
        base = 10
        k = 0
        while (a):
            t = a % base
            a = a // base
            k = k + t ** 3
        if (k == p):
            print(p)
        p=p+1
armstrong(500)