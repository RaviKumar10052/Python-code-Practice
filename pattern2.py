def patterna(n,b):
    k = 2*n-1
    a=n
    i=1
    t=b
    while(i<=n):
        b=t
        while(b):
            if (i % 2 == 1):
                print(" " * (n - i), end="")
                m = i
                k = 1
                while (k <= 2 * m - 1):
                    if (k % 2 == 1):
                        print("*", end="")
                    else:
                        print(" ", end="")
                    k = k + 1
            else:
                print(" " * (n - i), end="")
                m = i
                k = 1
                while (k <= 2 * m - 1):
                    if (k % 2 == 1):
                        print("#", end="")
                    else:
                        print(" ", end="")
                    k = k + 1
            print(" " * (n - i), end="")
            b=b-1
        print(" " * (n - i))

        i=i+1
patterna(5,5)


