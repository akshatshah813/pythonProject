list=[11,44,500,22,99,77,200,66,2]

for x in list:
    if x%2==0:
        print(x)

print(list)
list.sort()
print("ascending",list)
list.reverse()
print("descending",list)

list.pop(0)
print(list)