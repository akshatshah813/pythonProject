import random
x=random.randint(1,30)
t=0
y=0
while x!=y:
    y=int(input("Enter your number => \n"))
    if y==x:
        print("congrats you won!!!")
    elif y>x:
        print("Please think a lower than that")
    elif y<x:
        print("Please think a greater than that")
    t=t+1

print("Trial =",t)