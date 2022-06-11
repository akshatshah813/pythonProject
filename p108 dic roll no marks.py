import random
marks={}

n=int(input("Enter limit =>"))

for i in range(1,n+1):
    x=random.randint(1,30)
    y=random.randint(10,50)
    marks[x]=y

print("Rollno\tMakrs")
print("*"*30)
for key,value in marks.items():
    print(key,"\t\t",value)
print("*"*30)