import random
x=int(input("enter the limit for the list => "))
l1=[]
l2=[]
l3=[]
s=0
s1=0
c1=0
s2=0
c2=0
for x in range(1,x+1):
    a=int(input("Eneter your number => "))
    s=s+a
    l1.append(a)

print(l1)

print("sum of list =",s)

for a in l1:
    if a%2==0:
        print("Even numbers are")
        l2.append(a)
        print(l2)
        s1=s1+a
        c1=c1+1
print("Sum of even numbers => ",s1)
print("Count of even number => ",c1)

for a in l1:
    if a%7==0:
        l3.append(a)
        s2 = s2 + a
        c2 = c2 + 1
print(l3)
print("Sum of numbers divisible by 7=> ",s2)
print("Count of number divisible by 7=> ",c2)

