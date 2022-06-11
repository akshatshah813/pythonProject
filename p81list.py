import random
n=int(input("Enter limit =>"))
list1=[]
c=0
for i in range(1,n+1):
    x=random.randint(1,30)
    list1.append(x)

print(list1)