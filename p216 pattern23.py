x=int(input("Enter no. =>"))
y=x
k=1
for i in range(1,x+1):
    print("")

    for j in range(y+1,1,-1):
        print(k,"",end="")
        k=k+1
    y=y-1