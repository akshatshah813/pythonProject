x=int(input("Enter no. =>"))
y=x
k=0
for i in range(1,x+1):
    print("")
    for j in range(y+1,1,-1):
        k = k + 1
        if k%2==0:
            print("1",end="")
        else:
            print("0", end="")
    y=y-1