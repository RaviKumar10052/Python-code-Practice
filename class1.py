def maximum(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    elif b>c:
        if b>a:
            return b
        else:
            return a
print(maximum(15,12,27))
print(maximum(15,29,27))
print(maximum(35,29,27))
