x=int(input("Enter your number => "))
s=1
c=0

for i in range(x,0,-1):
    print(i,"x",end="")
    s=s*i

print("\nFactorial =",s)