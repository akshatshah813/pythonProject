x=int(input("Enter no. =>"))

for i in range(1,x+1):
    print("")
    for j in range(1,x+1):
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
