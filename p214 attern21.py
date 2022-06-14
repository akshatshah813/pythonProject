x=int(input("Enter no. =>"))
y=x

for i in range(1,x+1):
    print("")
    z = x
    for j in range(y+1,1,-1):
        if i%2==0:
            print("1",end="")
        else:
            print("0", end="")
    y=y-1