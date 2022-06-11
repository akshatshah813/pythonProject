import random
marks={}
c1=0
c2=0
n=int(input("Enter limit =>"))

for i in range(1,n+1):
    x=random.randint(1,30)
    y=random.randint(10,50)
    marks[x]=y


print("\nRollno\tMakrs\t\t:)/:(")
print("*"*40)

for key,value in marks.items():
    if value>=18:
        print(key,"\t\t",value,"\t\tPass :)")
        c1=c1+1
    else:
        print(key,"\t\t",value,"\t\tFail :(")
        c2=c2+1
print("*"*40)
print("Toatal number of students passed =>",c1)
print("Toatal number of students failed =>",c2)
print("*"*40)