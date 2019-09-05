import random


def scramble(word):
    ws = word.split()
    l = len(ws)
    t=[]
    while (l):
        k = random.randint(0, l-1)
        t.append(ws[k])
        del ws[k]
        l = l - 1
    return t


scramble('kumar')
paragraph = input("Enter Paragraph\n")
ls = paragraph.split(" ")
print(ls)
s = [] * len(ls)
for i in ls:
    k = len(i)
    if k < 4:
        s.append(i)
    else:
        if (i[k - 1] != '[^a-zA-Z]'):
            p = str(scramble(i[1:k - 3]))
            t = i[0] + p + i[k - 2]+i[k-1]
            s.append(t)
        else:
            p = str(scramble(i[1:k - 2]))
            t = i[0] + p + i[k - 1]
            s.append(t)

print(s)
