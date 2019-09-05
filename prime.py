def prime(n):
    if(n==1):
        print("not prime number ")
    elif(n==2):
        print(n)
    else:
       print("2")
       k=3
       while(k<=n):
           flag = 0
           for i in range(2,k-1):
               if(k%i==0):
                   flag=flag+1
           if(flag==0):
                print(k)
           k=k+1
prime(95)
