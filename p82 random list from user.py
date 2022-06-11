import random
n=int(input("Enter limit =>"))
list1=[]
c1=0
c2=0
s1=0
s2=0
for i in range(1,n+1):
    x=random.randint(1,30)
    list1.append(x)

    if x%2==0:
        #print(x,"is even.")
        c1=c1+1
        s1=s1+x
    else:
        #print(x, "is odd.")
        c2=c2+1
        s2=s2+x
print(list1)
print("\neven numbers=>",c1,"\nodd numbers=>",c2)
print("\nSum of even numbers=>",s1,"\nSum of odd numbers=>",s2)