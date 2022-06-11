x=int(input("enter the number limit => \n"))
c=0
s=0
for i in range(1,x+1):
    if i%2==0:
        print(i," is even")
        c = c + 1
        s = s + i

print("Sum = ", s, " count = ", c)

c=0
s=0
for i in range(1,x+1):
    if i%2!=0:
        print(i," is odd")
        c = c + 1
        s = s + i


print("Sum = ", s, " count = ", c)
