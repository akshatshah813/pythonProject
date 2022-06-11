a=1
b=30
import random
x=random.randint(a,b)
t = 0
y = 0
while x!=y:
    while x!=y:
        print("You can select a number between", a, "-", b)
        y=int(input("Enter your number => \n"))
        if y==x:
            print("congrats you won!!!")
        elif y>x:
            print("Please think a number lower than that")
            b=y
        elif y<x:
            print("Please think a number greater than that")
            a=y
        t=t+1

print("Trial =",t)