fp = open("s.txt","w")
fp.write("Hello,\n   My Name is Ravi Kumar\n   I am in Upes\n Thank you")
fp.close()

fp=open("s.txt","r")
print(fp.readline(),fp.readline(),fp.readline())

for x in fp:
    print(x)
fp.close()
f=open("a.txt","w")
f.close()
import os
if os.path.exists("a.txt"):
    os.remove("a.txt")
    print("file removed")
else:
    print("file doesnot exists")