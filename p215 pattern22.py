x=int(input("Enter no. =>"))
y=x

for i in range(1,x+1):
    print("")
    k = 0
    for j in range(y+1,1,-1):
        if k%2==0:
            print("0",end="")
        else:
            print("1", end="")
        k=k+1
    y=y-1