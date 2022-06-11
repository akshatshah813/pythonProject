hey="Hey, How are you?"
c=0
s=0

for x in hey:
    if x.isupper():
        c=c+1
    else:
        s=s+1
print(hey)
print("total upper case =>",c)
print("total lower case =>",s)

heyy=hey.swapcase()
print(heyy)
s=0
c=0
for x in heyy:
    if x.isupper():
        c=c+1
    else:
        s=s+1
print("total upper case =>",c)
print("total lower case =>",s)
