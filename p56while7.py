x=int(input("Enter your number => "))
s=1
i=x

while i>0:
    print(i,"x",end="")
    s=s*i
    i=i-1

print("\nFactorial of",x,"=",s)
