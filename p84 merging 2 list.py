import random
x=int(input("Enter your limit for list1 =>"))
y=int(input("Enter your limit for list2 =>"))
l1=[]
l2=[]
l3=[]
c1=0
c2=0
c=0
for x in range(1,x+1):
    a=random.randint(1,30)
    l1.append(a)
    l3.append(a)
    c1=c1+1
print(l1)

for y in range(1,y+1):
    b=random.randint(1,30)
    l2.append(b)
    l3.append(b)
    c2=c2+1
print(l2)


c=c1+c2

print(l3)

print("\ncount of l1=>",c1,"\ncount of l2=>",c2,"\nCount of l3 =>",c)
