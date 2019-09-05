s=input()
k=0
for i in range (0, len(s)):
    l=s.count(s[i])
    if(l==1):
        print(s[i],end='')
        k=k+1;

if(k==0):
    print(-1)