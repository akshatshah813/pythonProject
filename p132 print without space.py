space=" "
stat=input("Enter your sentence => ")
l1=list(stat)

for i in l1:
    print(i,end="")
print("\n")

for x in stat:
    if x==space:
        l1.remove(x)

for i in l1:
    print(i,end="")