def search(a,k):
    if k in a:
        print("present in the list!")
    else:
        print("not present in the list")
lis=[]
n=int(input("enter the size"))
for i in range(n):
    c=int(input("enter element"))
    lis.append(c)
s=int(input("enter elemnent to search"))
search(lis,s)

