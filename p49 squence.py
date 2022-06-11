x=int(input("Enter your number => "))
s=0
for i in range(1,x+1,3):
    print(i,"+",end="")
    s=s+i

print("\nSum =",s)