s=input()
l=s.split(" ")
n=len(l)
l2=[]
print(l2)
l3=[]
for i in range (0,n):
    l2.append(l[n-(i+1)])
print(l2)
for i in range(0,n):
    if(i%2==0):
        print(l2[i][::-1],end=' ')
        l3.append(l2[i][::-1])
    else:
        print(l2[i],end=' ')
        l3.append(l2[i])
print("")

#print(l3)

