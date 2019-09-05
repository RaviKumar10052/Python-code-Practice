def addpoly(p1,p2):
    if p1[0][1] > p2[0][1]:
        t = p1[0][1]
    else:
        t = p2[0][1]
    k = t
    ls = [(0,0)]*(t+1)
    a=0
    for j in p1:
        for l in p2:
            if t == j[1] and t == l[1]:
                if (j[0] + l[0]) != 0:
                    ls[a][0] = j[0] + l[0]
                    ls[a][1] = t
                    t=t-1
                    a=a+1
            elif t == j[1]:
                ls[a][0] = j[0]
                ls[a][1] = t
                t=t-1
                a=a+1
            elif t == l[1]:
                ls[a][0] = l[0]
                ls[a][1] = t
                t = t - 1
                a = a + 1
            else:
                t = t - 1
                a = a + 1

    return ls


addpoly([(4,3),(3,0)],[(-4,3),(2,1)])