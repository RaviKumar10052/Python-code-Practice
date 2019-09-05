import time
from threading import Thread
class newthread(Thread):
    def __init__(self,n):
        Thread.__init__(self)
        self.x=n

    def run(self,m):
        self.x=m
        print("Hello my name is",self.getName())
        for i in range(1,11):
            time.sleep(5)
            print(self.x," * ", i," = ",self.x*i)


t1=newthread(10)
t2=newthread(20)
t1.run(20)
t2.run(30)
