z=int(input("Enter the number of questions you want to answer => \n"))
i=1
count=0
Truecount=0
Falsecount=0
while i<=z:
    import random
    x=random.randint(1,30)
    print("x=>",x)
    y=random.randint(1,30)
    print("y=>",y)

    c=x+y
    n=int(input("enter addition of the given x and y => \n"))



    if n==c:
        print("Addition of ",x,"and ",y,"is",n)
        print("Your answer is correct :)")
        Truecount=Truecount+1
    else:
        print("Your answer is wrong :( ")
        Falsecount=Falsecount+1


    i=i+1

    count=count+1
    print("*************")
    print("Question's Answered=>",count)
    print("Truecount=",Truecount,"\nFalsecount",Falsecount)
    print("*************")


