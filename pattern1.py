def patterna(n):
    k = 2*n-1
    a=n
    i=1
    while(i<=n):
        if(i%2==1):
            print(" "*(n-i),end="")
            m=i
            k=1
            while(k<=2*m-1):
                if(k%2==1):
                    print("*",end="")
                else:
                    print(" ",end="")
                k=k+1
            print(" "*(n-i))
        else:
            print(" " * (n - i), end="")
            m = i
            k = 1
            while (k <= 2*m - 1):
                if (k % 2 == 1):
                    print("#", end="")
                else:
                    print(" ",end="")
                k = k + 1
            print(" "*(n-i))
        i=i+1
patterna(5)


