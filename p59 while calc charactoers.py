while True:
    print("***Calculator***")
    print("Addition => + ")
    print("Substraction => -")
    print("Multiplication => *")
    print("Division => /")
    print("Exit => ^")
    x=input("Choos an option => \n")

    if x=='+':
        n1=float(input("Enter number 1 => \n"))
        n2=float(input("Enter number 2 => \n"))
        print("Addition => ",n1,"+",n2,"=",(n1+n2))
    elif x=='-':
        n1=float(input("Enter number 1 => \n"))
        n2=float(input("Enter number 2 => \n"))
        print("Substraction => ",n1,"-",n2,"=",(n1-n2))
    elif x=='*':
        n1=float(input("Enter number 1 => \n"))
        n2=float(input("Enter number 2 => \n"))
        print("Multiplication => ",n1,"x",n2,"=",(n1*n2))
    elif x=='/':
        n1=float(input("Enter number 1 => \n"))
        n2=float(input("Enter number 2 => \n"))
        print("Division => ",n1,"/",n2,"=",(n1/n2))
    elif x=='^':
        break
    else:
        print("Choose a valid option!")