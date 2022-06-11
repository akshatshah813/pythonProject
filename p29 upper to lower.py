x=input("Enter your Letter => ")

if x.islower():
    print("It's a Lower Case.")
    y=x.upper()
    print(x,"to upper case is",y)
elif x.isupper():
    print("It's a Upper Case")
    y = x.lower()
    print(x, "to lower case is ", y)
elif x.isdigit():
    print("It's a digit")
else:
    print("Invalid")


