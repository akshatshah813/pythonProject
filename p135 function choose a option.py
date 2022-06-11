def add():
    x = int(input("Enter value a =>"))
    y = int(input("Enter value b =>"))
    print("addition of the given number is ", (x + y))


def factorial():
    x = int(input("Enter the number =>"))
    f = 1
    for i in range(1, x + 1):
        print(i, "*", end="")
        f = f * i
    print("=", f)
    print("\nFactorial of ", x, "is ", f)


def table():
    x = int(input("Enter the table number =>\n"))
    for i in range(1, 11):
        print(x, "*", i, "=", (x * i))


def areaoftrinagle():
    h = float(input("Enter the height of triangle =>"))
    b = float(input("Enter the base of triangle =>"))
    print("The area of triangle is ", (h * b * 0.5))


def max2():
    n1 = int(input("Enter number 1 =>"))
    n2 = int(input("enter number 2 =>"))
    if n1 > n2:
        print(n1, "is greater than ", n2)
    elif n2 > n1:
        print(n2, "is greater than ", n1)
    else:
        print(n1, "=", n2)


def pn():
    n = int(input("Enter your number =>"))
    if n >= 0:
        print(n1, "is positive.")
    else:
        print(n1, "is negative.")


def oe():
    n = int(input("Enter your number =>"))
    if n % 2 == 0:
        print(n, "is even.")
    else:
        print(n, "is odd.")

print("*"*20)
print("Options")
print("*"*20)
print("Addition of two number => 1")
print("Factorial => 2")
print("Table =>3")
print("Area of Triangle =>4")
print("Maximum of 2 numbers =>5")
print("To check number is positive/negative => 6")
print("To Check if number is odd/even => 7")
print("*"*20)
n=int(input("CHOOSE AN OPTION"))
print("*"*20)

if n==1:
    add()
elif n==2:
    factorial()
elif n==3:
    table()
elif n ==4:
    areaoftrinagle()
elif n ==5:
    max2()
elif n ==6:
    pn()
elif n ==7:
    oe()
else:
    print("Choose a valid option!!!!")


