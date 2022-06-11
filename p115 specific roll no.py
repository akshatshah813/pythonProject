import random
d1={}
l1={}
d=int(input("enter number of students =>"))


for i in range(1,d+1):
    r=random.randint(1,30)
    l1=[]
    for c in range(1,4):
        m=random.randint(10,50)
        l1.append(m)
    d1[r]=l1

print(d1)
x=int(input("\nEnter the Roll no. =>"))
f=0
for key,value in d1.items():
    if x==key:
        m1,m2,m3=value
        total=sum(value)
        print("\nroll no.\tm1\t\tm2\t\tm3\ttotal")
        print(key,"\t\t\t",m1,"\t",m2,"\t",m3,"\t",total)
        f=1

if f==0:
    print("No Data Found ")