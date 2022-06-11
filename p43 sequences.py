n=int(input("enter your number"))

#1x2x3x4x5
s=1
for i in range(1,n+1):
    print(i,"x ",end="")
    s=s*i

print("\n sum =",s)



