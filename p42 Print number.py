x=int(input("Enter your number => \n"))

s=0
for i in range(1,x+1):
    print(i," + ",end="")
    s=s+i

print("\nSum = ",s)