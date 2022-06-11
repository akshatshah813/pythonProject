while True:
    print("***Calculator***")
    print("1=>Addition")
    print("2=>Substraction")
    print("3=>Multiplication")
    print("4=>Division")
    print("5=>Exit")
    x=int(input("Choos an option => \n"))

    if x==1:
        n1=float(input("Enter number 1 => \n"))
        n2=float(input("Enter number 2 => \n"))
        print("Addition => ",n1,"+",n2,"=",(n1+n2))
    elif x==2:
        n1=float(input("Enter number 1 => \n"))
        n2=float(input("Enter number 2 => \n"))
        print("Substraction => ",n1,"-",n2,"=",(n1-n2))
    elif x==3:
        n1=float(input("Enter number 1 => \n"))
        n2=float(input("Enter number 2 => \n"))
        print("Multiplication => ",n1,"x",n2,"=",(n1*n2))
    elif x==4:
        n1=float(input("Enter number 1 => \n"))
        n2=float(input("Enter number 2 => \n"))
        print("Division => ",n1,"/",n2,"=",(n1/n2))
    elif x==5:
        break
    else:
        print("Choose a valid option!")