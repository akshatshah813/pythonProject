import random
x=random.randint(1,30)
print("x=>",x)
y=random.randint(1,30)
print("y=>",y)

c=x+y
n=int(input("enter addition of the given x and y => \n"))

if n==c:
    print("Addition of ",x,"and ",y,"is",n)
    print("Your answer is correct :)")
else:
    print("Your answer is wrong :( ")
