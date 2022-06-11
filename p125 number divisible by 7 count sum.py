t1=(88,7,1,14,22,91)
l1=list(t1)
s=0
c=0
for i in l1:
    if i%7==0:
        print(i)
        s=s+i
        c=c+1
print("sum = ",s)
print("count = ",c)