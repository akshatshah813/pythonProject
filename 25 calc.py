print("Choose an option")
print("Addition => + ")
print("Substraction => - ")
print("Multipplication => * ")
print("Division => / ")
op=input("Choose an option => ")


if op=='+':
    x = float(input("Enter your number1 =>"))
    y = float(input("Enter your number2 =>"))
    print("Addition of ",x,"and ",y," is ",(x+y))
elif op=='-':
    x = float(input("Enter your number1 =>"))
    y = float(input("Enter your number2 =>"))
    print("Substraction of ",x, "and ",y," is ", (x-y))
elif op=='*':
    x = float(input("Enter your number1 =>"))
    y = float(input("Enter your number2 =>"))
    print("Multiplication of ",x, "and ",y," is ",(x*y))
elif op=='/':
    x = float(input("Enter your number1 =>"))
    y = float(input("Enter your number2 =>"))
    print("Division of ",x,"and ",y," is ",(x/y))
else:
    print("Choose a valid option")