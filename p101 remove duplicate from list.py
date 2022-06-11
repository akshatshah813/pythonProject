list=[11,44,500,22,99,77,200,66,2,11,22]

for i in list:
    x=list.count(i)
    if x>1:
        list.remove(i)

print(list)

