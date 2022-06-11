print("Press 1 for square")
print("Press 2 for cube")
op=int(input("Enter opt =>"))

if op==1:
    x=float(input("Enetr a number => "))
    print("Square of ",x," is ",(x*x))
elif op==2:
    x=float(input("Enetr a number => "))
    print("Cube of",y," is ",(x*x*x))
else:
    print("Wrong opt")