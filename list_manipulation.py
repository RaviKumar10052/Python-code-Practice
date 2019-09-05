n = int(input())
list=[]
l=[]
for i in range (0,n):
    x= input().split()
    l.append(x)

for y in l:
    x=y[0]
    if (x=="insert"):
        list.insert(int(y[1]),int(y[2]))
    elif(x=="remove"):
        list.remove(int(y[1]))
    elif(x=="print"):
        print(list)
    elif(x=="append"):
        list.append(int(y[1]))
    elif(x=="sort"):
        list.sort()
    elif(x=="pop"):
        list.pop()
    elif(x=="reverse"):
        list.reverse()
