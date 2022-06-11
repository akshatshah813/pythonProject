list1=[11,-22,+33,-44,55,-66]
c1=0
c2=0
for x in list1:

    if x<0:
        print(x,"is negative")
        c1=c1+1
    else:
        print(x,"is positive")
        c2=c2+1

print("\n+ve count=",c1,"\n-ve count=",c2)