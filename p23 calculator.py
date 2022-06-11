rint("Choose an option")
print("1 => Addition")
print("2 => Substraction")
print("3 => Multipplication")
print("4 => Division")
op=int(input("Choose a number =>"))


if op==1:
    x = float(input("Enter your number1 =>"))
    y = float(input("Enter your number2 =>"))
    print("Addition of ",x,"and ",y," is ",(x+y))
elif op==2:
    x = float(input("Enter your number1 =>"))
    y = float(input("Enter your number2 =>"))
    print("Substraction of ",x, "and ",y," is ", (x-y))
elif op==3:
    x = float(input("Enter your number1 =>"))
    y = float(input("Enter your number2 =>"))
    print("Multiplication of ",x, "and ",y," is ",(x*y))
elif op==4:
    x = float(input("Enter your number1 =>"))
    y = float(input("Enter your number2 =>"))
    print("Division of ",x,"and ",y," is ",(x/y))
else:
    print("Choose a valid option")