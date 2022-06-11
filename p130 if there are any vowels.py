user=input("Enter your word =>")
v=['a','e','i','o','u']
c=0
for x in user:
    for y in v:
        if x==y:
            c=c+1
print(user)
print("total vowels => ",c)