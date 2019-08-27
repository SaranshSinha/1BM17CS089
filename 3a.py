def allDivisors(n):
    li=[]
    for i in range(1,n+1):
        if n%i==0:
            li.append(i)

    return li
l2=[]
n=int(input("enter the number"))
print("The lis of divisors are: ")
l2=allDivisors(n)
print(l2)
