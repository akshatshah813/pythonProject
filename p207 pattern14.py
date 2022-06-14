x=int(input("Enter no. =>"))
k=0
for i in range(1,x+1):
    print("")
    for j in range(1,i+1):
        k=k+1
        if k%2==0:
            print("0",end="")
        else:
            print("1",end="")
