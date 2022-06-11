# +1+4+27+16+125+
x=int(input("enter the number limit => \n"))
s=0
s1=0
s2=0
for i in range(1,x+1):
    if i%2==0:
        print((i*i)," +",end="")
        s=s+(i*i)
    else:
        print((i*i*i), " +", end="")
        s=s+(i*i*i)

print("\n sum =",s)