def rev1(s):
    lis1=s.split(" ")
    lis1.reverse()
    a=" "
    lis2=a.join(lis1)
    print(lis2)

def rev2(s):
    lis1=s.split(" ")
    lis2=""
    for i in lis1:
        lis2+=i[::-1]
        lis2+=" "
    print(lis2)

s="Welcome to bmsce"
rev1(s)
rev2(s)
