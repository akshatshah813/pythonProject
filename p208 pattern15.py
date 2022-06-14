x=int(input("Enter no. =>"))

for i in range(1,x+1):
    print("")
    k = x
    for j in range(1,i+1):
        print(k,"",end="")
        k = k - 1