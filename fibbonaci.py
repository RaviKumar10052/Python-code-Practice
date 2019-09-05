def fibbonaci(n):
    f0=1
    f1=1
    print(f0)
    print(f1)
    while(n):
        f=f0+f1
        (f1,f0)=(f,f1)
        n=n-1
        print(f)
fibbonaci(15)
