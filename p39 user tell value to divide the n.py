
x=int(input("choose your divider => \n"))
n=int(input("enter the number limit => \n"))
c=0
s=0
for i in range(1,n):
    if i%x==0:
        print(i)
        c=c+1
        s=s+i

print("Sum =",s," count = ",c)