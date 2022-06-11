A={111,22,33,44,55,66}

for i in range(3,8):
    A.add(i)

print(A)

A={1,2,3,4,5}
B={4,5,6,7,8}
c=A|B
print(c)
print(A.union(B))

c=A&B
print(A.intersection(B))

c=A-B
print(c)

A={1,2,3}
B={4,5,6}
print(A.isdisjoint(B))

A={1,2,3}
B={1,2,3,4,5}
C={1,2,4,5}
print(A.issubset(B))
print(A<B)
print(C.issubset(B))
print(C<B)
print(A.issubset(C))
print(A<C)

print("*"*20)

print(A.issuperset(B))
print(A>B)
print(C.issuperset(B))
print(C>B)
print(A.issuperset(C))
print(A>C)

