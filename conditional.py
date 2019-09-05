n = int(input())
if(n%2==1):
    print("weird")
else:
    if(n<=5 and n>=2):
        print("not wierd")
    if(n>=6 and n<=20):
        print("weird")
    if(n>=20):
        print("Not weird")
