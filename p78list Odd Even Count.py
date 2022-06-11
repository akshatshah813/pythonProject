list1=[11,22,33,44,55,66]
c=0
for x in list1:

    if x%2==0:
        print(x,"is even")
        c=c+1
    else:
        print(x,"is odd")
        c=c+1
print(c)