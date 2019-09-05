class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def get_marks(self):
        return self.marks
    def get_name(self):
        return self.name


a=Student("Ravi",21,92)
b=Student("Atul",21,94)
c=Student("Ashish",21,96)
avg=(a.get_marks()+b.get_marks()+c.get_marks())/3
print(avg)
if(a.get_marks()>=b.get_marks()>c.get_marks()):
    print("Topper is ", a.get_name())
elif(b.get_marks()>=c.get_marks()):
    print("Topper is: ", b.get_name())
else:
    print("Topper is: ",c.get_name())
ls=[a.marks,b.marks,c.marks]
sum=0
for i in range(3):
    sum=sum+ls[0]
    del ls[0]
print(sum)
print(ls)



