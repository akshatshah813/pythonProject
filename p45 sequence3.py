# +1-2+3-4+5-

x=int(input("enter the number limit => \n"))
s=0
for i in range(1,x+1):
    if i%2==0:
        print(i," +",end="")
        s = s - i
    else:
        print(i, " -", end="")
        s = s + i

print("sum =",s)