f=open("st.txt","w")
f.write("Ravi R1 95 92 65 85 67 \n")
f.write("Aniket R2 95 91 69 87 97 \n")
f.write("Samarth R3 95 90 68 89 67 \n")
f.write("kundan R4 95 92 69 84 67 \n")
f.write("Rahul R5 94 92 67 89 78 \n")
f.close()

f=open("st.txt","r")
for x in f:
    print(x)
f.close()

f=open("st.txt","r")
l1=f.readline()
l2=f.readline()
l3=f.readline()
l4=f.readline()
l5=f.readline()
print(l1,l2,l3,l4,l5)
f.close()
s1=l1.split(" ")
s2=l2.split(" ")
s3=l3.split(" ")
s4=l4.split(" ")
s5=l5.split(" ")
print(s1,s2,s3,s4,s5)
sl1=s1[2:7]
sl2=s2[2:7]
sl3=s3[2:7]
sl4=s4[2:7]
sl5=s5[2:7]
print(sl1,sl2,sl3,sl4,sl5)
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
for i in sl1:
    sum1=sum1+int(i)
for i in sl2:
    sum2=sum2+int(i)
for i in sl3:
    sum3=sum3+int(i)
for i in sl4:
    sum4=sum4+int(i)
for i in sl5:
    sum5=sum5+int(i)
print(sum1,sum2,sum3,sum4,sum5)
list=[sum1,sum2,sum3,sum4,sum5]
key=list[0]
index=0
list1=[s1[0],s2[0],s3[0],s4[0],s5[0]]
print(list1)
for i in list:
    if(i>key):
        key=i
        index=index+1
print("topper is ",list1[index])

