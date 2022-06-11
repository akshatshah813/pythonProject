while True:
    print("Options:")
    print("1 => SQUARE")
    print("2 => CUBE")
    print("3 => Exit")
    x=int(input("Choose an option => \n"))
    if x==1:
        n = int(input("Enter your number => \n"))
        print(n," Square =>",(n*n))
    elif x==2:
        n = int(input("Enter your number => \n"))
        print(n, "Cube =>", (n*n*n))
    elif x==3:
        break
    else:
        print("Enter valid number!")