x=int(input("Enter your number => \n"))
i=1
s=1

while i<=x:
    print(i,"x",end="")
    s = s * i
    i=i+1

print("\nFactorial of ",x,"=",s)