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

l2=[]
for key,value in d1.items():
    total=sum(value)
    l2.append(total)

high=max(l2)


for key,value in d1.items():
    total=sum(value)
    if total==high:
        print(key,"\t",total)