x=int(input("Enter no. =>"))
y=x

for i in range(1,x+1):
    print("")
    z = x
    for j in range(y+1,1,-1):
        print(z,end="")
        z=z-1
    y=y-1