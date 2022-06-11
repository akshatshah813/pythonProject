import random

d1={}
l1=[]

n=int(input("Enter number of students =>"))
m=int(input("\nenter number of subjects =>\n"))
for i in range(1,n+1):
    r=random.randint(1,30)
    l1=[]

    for j in range(1,m+1):
        x=random.randint(10,50)
        l1.append(x)
        d1[r]=l1
print("*"*70)
print("Rool no.\tmaths\tscience\tcomp.\tenglish\t\ttotal")
print("*"*70)
for key,value in d1.items():
    m1,m2,m3,m4=value
    total=sum( value)
    print(key,"\t\t\t",m1,"\t",m2,"\t",m3,"\t",m4,"\t\t",total)