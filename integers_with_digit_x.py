n,x= input().split()
l=[]
k=0
for i in range (1,int(n)+1):
    a=str(i)
    if(x in a):
        l.append(a)
        k=k+1
if(k==0):
    print(-1)
else:
    for x in l:
        print(x,end=" ")

