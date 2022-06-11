print("Choose an option")
print("1 => area of a triangle")
print("2 => Cube")
print("3 => maximum of two number")
x=int(input("Choose an option from above =>"))

if x==1:
    h=float(input("Enter Height => "))
    b=float(input("Enter base => "))
    print("The area of triangle with height ",h," and base ",b," is ",(h*b*0.5))
elif x==2:
    n=float(input("Enter the number => "))
    print("The Cube of ",n," is ",(n*n*n))
elif x==3:
    n1=float(input("Enter the number1 => "))
    n2=float(input("Enter the number2 => "))
    if n1==n2:
        print("numbers are equal")
    elif n1>n2:
        print(n1," is the greater number.")
    else:
        print(n2, " is the greater number.")
else:
    print("Choose a valid option.")

