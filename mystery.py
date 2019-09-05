def mystery(l):
    if l == []:
        return (l)
    else:
        return (l[-1:] + mystery(l[:-1]))


print(mystery([13,23,17,81,15]))
pairs = [ (x,y) for x in range(4) for y in range(3) if (x+y)%3 == 0 ]
print(pairs)