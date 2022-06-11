import random
n=int(input("Enter your number =>"))
l1=[]
l2=[]

for n in range(1,n+1):
    x=random.randint(1,30)
    l1.append(x)

    y=x*x
    l2.append(y)
print(l1)
print(l2)
