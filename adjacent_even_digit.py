number=str(input())
k=0
#print(number)
n=len(number)
#print(n)
if int(number[1])%2==0 :
    print(number[0],end='')
    k=k+1

for i in range (1,n-1):
    if int(number[i-1])%2==0 and int(number[i+1])%2==0 :
        print(number[i],end='')
        k=k+1
if int(number[n-2])%2==0 :
    print(number[n-1],end='')

if(k==0):
    print(-1)


