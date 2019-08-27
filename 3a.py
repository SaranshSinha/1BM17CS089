import string
import random
from random import randint
while True:
    s=string.printable

    n=input("\nenter anything")
    x=random.choice([10,11,12,13,14,15])
    print(s[randint(0,10)],end="")
    print(s[randint(11,37)],end="")
    print(s[randint(63,89)],end="")
    #print(s[randint(90,99)],end="")
    for i in range(x-3):
        print(s[randint(0,99)],end="")
