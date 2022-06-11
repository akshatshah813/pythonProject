def add(x,y):
    print("addition of the given number is ", (x + y))
def max2(x,y):

    if x > y:
        print(x, "is greater than ", y)
    elif y > x:
        print(y, "is greater than ", x)
    else:
        print(x, "=", y)


def cube(x):
    print("cube of the given number",x," is ", (x*x*x))


x = int(input("Enter number 1 =>"))
y = int(input("enter number 2 =>"))

add(x,y)
max2(x,y)
cube(x)
