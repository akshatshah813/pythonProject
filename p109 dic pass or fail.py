import random
marks={}

n=int(input("Enter limit =>"))

for i in range(1,n+1):
    x=random.randint(1,30)
    y=random.randint(10,50)
    marks[x]=y


print("\nRollno\tMakrs\t\t:)/:(")
print("*"*30)

for key,value in marks.items():
    if value>=18:
        print(key,"\t\t",value,"\t\tPass :)")
    else:
        print(key,"\t\t",value,"\t\tFail :(")
print("*"*30)