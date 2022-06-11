#1+4+9+16+25
n=int(input("enter your number"))
s=0
for i in range(1,n+1):
    print((i*i),"+ ",end="")
    s=s+(i*i)
print("\n sum =",s)
