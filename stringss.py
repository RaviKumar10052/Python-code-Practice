str=input()
#print(str.isupper())
c=0
l=0
#if(str.isupper()==False):
   # print(str.upper())
for i in str:
    if i.isupper():
        c=c+1
        print(i.lower(),end="")
    else:
        l=l+1
        print(i.upper(),end="")
print()
print("upper count:",c," lowercount: ",l)
