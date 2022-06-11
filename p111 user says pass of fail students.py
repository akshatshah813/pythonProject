import random
marks={}
c1=0
c2=0
n=int(input("Enter Number of students =>"))

for i in range(1,n+1):
    x=random.randint(1,30)
    y=random.randint(10,50)
    marks[x]=y
print("*"*40)
print("Options")
print("Passed Students => p")
print("Failled Students => f")
z=input("\nChoose an option =>\n")

print("*"*40)
print("roll no\t\tMarks")
print("*"*40)

for key,value in marks.items():
    if z=='p':
        if value>=18:
            print(key,value)
            c1=c1+1
    elif z=='f':
        if value<18:
            print(key,value)
            c2=c2+1
    else:
        print("Choose valid option!")
print("*"*40)
if z=='p':
    print("Toatal number of students passed =>", c1)
elif z=='f':
    print("Toatal number of students failed =>", c2)
