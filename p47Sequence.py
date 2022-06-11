x=int(input("Enter your number =>"))
s=0
c=0

for i in range(1,x+1):
    print(" 1/",i,"+",end="")
    c=c+1
    s=s+(1/i)

print("\nSum =",s," Count =",c)