def add():
    x = int(input("Enter value a =>"))
    y = int(input("Enter value b =>"))
    print("addition of the given number is ", (x + y))

def factorial():
    x = int(input("Enter the number =>"))
    f=1
    for i in range(1,x+1):
        print(i,"*",end="")
        f=f*i
    print("=",f)
    print("\nFactorial of ",x,"is ",f)

def table():
    x = int(input("Enter the table number =>\n"))
    for i in range(1,11):
        print(x,"*",i,"=",(x*i))

def areaoftrinagle():
    h=float(input("Enter the height of triangle =>"))
    b=float(input("Enter the base of triangle =>"))
    print("The area of triangle is ",(h*b*0.5))

def max2():
    n1=int(input("Enter number 1 =>"))
    n2=int(input("enter number 2 =>"))
    if n1>n2:
        print(n1,"is greater than ",n2)
    elif n2>n1:
        print(n2,"is greater than ",n1)
    else:
        print(n1,"=",n2)

def pn():
    n = int(input("Enter your number =>"))
    if n>=0:
        print(n1,"is positive.")
    else:
        print(n1,"is negative.")

def oe():
    n=int(input("Enter your number =>"))
    if n%2==0:
        print(n,"is even.")
    else:
        print(n,"is odd.")



add()
factorial()
table()
areaoftrinagle()
max2()
pn()
oe()