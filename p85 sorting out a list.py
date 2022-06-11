import random
n=int(input("Enter limit for your list => "))
l1=[]
l2=[]
l3=[]
c=0
c1=0
c2=0
for i in range(1,n+1):
    x=random.randint(1,30)
    l1.append(x)
    c=c+1

    if x%2==0:
        l2.append(x)
        c1=c1+1
    else:
        l3.append(x)
        c2=c2+1

print(l1)

print("Even List =>",l2)
print("Odd List =>",l3)
print("\nl1 count => ",c)
print("even number list count=> ",c1)
print("odd number list count=> ",c2)