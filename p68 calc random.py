print("calculator")
print("Addition => 1")
print("Substraction => 2")
print("Multiplication => 3")
print("Division => 4")
k=int(input("Choose an option => \n"))

if k==1:
    z = int(input("Enter the number of questions you want to answer => \n"))
    i = 1
    count = 0
    Truecount = 0
    Falsecount = 0
    while i <= z:
        import random

        x = random.randint(1, 30)
        print("x=>", x)
        y = random.randint(1, 30)
        print("y=>", y)

        c = x + y
        n = int(input("enter addition of the given x and y => \n"))

        if n == c:
            print("Addition of ", x, "and ", y, "is", n)
            print("Your answer is correct :)")
            Truecount = Truecount + 1
        else:
            print("Your answer is wrong :( ")
            Falsecount = Falsecount + 1

        i = i + 1
        count = count + 1
        print("_______________________________________________________")
        print("Question's Answered=>", count)
        print("Truecount=", Truecount, "\nFalsecount", Falsecount)
        print("_______________________________________________________")
elif k==2:
    z = int(input("Enter the number of questions you want to answer => \n"))
    i = 1
    count = 0
    Truecount = 0
    Falsecount = 0
    while i <= z:
        import random

        x = random.randint(1, 30)
        print("x=>", x)
        y = random.randint(1, 30)
        print("y=>", y)

        c = x - y
        n = int(input("enter Substraction of the given x and y => \n"))

        if n == c:
            print("Substraction of ", x, "and ", y, "is", n)
            print("Your answer is correct :)")
            Truecount = Truecount + 1
        else:
            print("Your answer is wrong :( ")
            Falsecount = Falsecount + 1

        i = i + 1
        count = count + 1
        print("_______________________________________________________")
        print("Question's Answered=>", count)
        print("Truecount=", Truecount, "\nFalsecount", Falsecount)
        print("_______________________________________________________")
elif k==3:
    z = int(input("Enter the number of questions you want to answer => \n"))
    i = 1
    count = 0
    Truecount = 0
    Falsecount = 0
    while i <= z:
        import random

        x = random.randint(1, 30)
        print("x=>", x)
        y = random.randint(1, 30)
        print("y=>", y)

        c = x * y
        n = int(input("enter Multiplication of the given x and y => \n"))

        if n == c:
            print("Multiplication of ", x, "and ", y, "is", n)
            print("Your answer is correct :)")
            Truecount = Truecount + 1
        else:
            print("Your answer is wrong :( ")
            Falsecount = Falsecount + 1

        i = i + 1
        count = count + 1
        print("_______________________________________________________")
        print("Question's Answered=>", count)
        print("Truecount=", Truecount, "\nFalsecount", Falsecount)
        print("_______________________________________________________")
elif k==4:
    z = int(input("Enter the number of questions you want to answer => \n"))
    i = 1
    count = 0
    Truecount = 0
    Falsecount = 0
    while i <= z:
        import random

        x = random.randint(1, 30)
        print("x=>", x)
        y = random.randint(1, 30)
        print("y=>", y)

        c = x / y
        n = int(input("enter Division of the given x and y => \n"))

        if n == c:
            print("Division of ", x, "and ", y, "is", n)
            print("Your answer is correct :)")
            Truecount = Truecount + 1
        else:
            print("Your answer is wrong :( ")
            Falsecount = Falsecount + 1

        i = i + 1
        count = count + 1
        print("_______________________________________________________")
        print("Question's Answered=>", count)
        print("Truecount=", Truecount, "\nFalsecount", Falsecount)
        print("_______________________________________________________")
else:
    print("Choose a valid option!")