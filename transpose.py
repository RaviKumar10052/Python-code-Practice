def transpose(l):
    m=l
    t = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return t


transpose([[1, 3],[2, 5]])