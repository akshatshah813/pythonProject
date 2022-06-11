set1={11,22,33,44,55,66}
set2={11,55,66}
set3={11,20,30,90}
set4={5,6,7,8}

print(set1.intersection(set2))
print(set1.intersection(set3))
print(set1.intersection(set4),"\n")

print("*"*20)

print(set1.union(set2))
print(set1.union(set3))
print(set1.union(set4),"\n")

print("*"*20)

print(set1-set2)
print(set1-set3)
print(set1-set4)

print("*"*20)

print(set3-set1)
print(set2-set1)
print(set4-set1)

print("*"*20)

print(set1.issuperset(set2))
print(set1.issuperset(set3))
print(set1.issuperset(set4))

print("*"*20)

print(set4.issubset(set1))
print(set4.issubset(set2))
print(set4.issubset(set3))
