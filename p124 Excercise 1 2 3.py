#1
tupleD=(11,22,33,44,55)
print(tupleD)
print("#"*20)
#2
print(sum(tupleD))
print("#"*20)
#3
list1=list(tupleD)
for i in list1:
    if i%2==0:
        print(i)

print("#"*20)