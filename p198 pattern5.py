x=int(input("Enter no. =>"))

for i in range(1,x+1):
    if i%2==0:
        print("")
        for j in range(1,x+1):
            print("0",end="")

    else:
        print("")
        for j in range(1,x+1):
            print("1",end="")
