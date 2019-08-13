def fib(n):
    i=0
    j=1
    if n==1:
        print("[0]")
    elif n==2:
        print("[0,1]")
    else:
        print("0")
        print("1")
        for c in range(n-2):
            s=i+j
            print(s)
            i=j
            j=s
x=int(input("enter the number of fib to generate"))
fib(x)
