print("Choose an option: ")
print("SQUARE => s")
print("CUBE => c")
x=input("Enter Your Option => ").lower()

if x=='s':
    n1=float(input("Enter your number => "))
    print("Square of ",n1," is",(n1*n1))
elif x=='c':
    n1=float(input("Enter your number => "))
    print("Square of ",n1," is",(n1*n1*n1))
else:
    print("Choose valid Option")