#1, 2, 145, and 40585

x=int(input("Enter your number => \n"))
s=0
i=1
f=1
t=x
while x>0:
    rem=x%10
    f=1
    i=1
    while i <= rem:
        f = f * i
        i= i+1
    s=s+f
    x=x//10

if s==t:
    print(t,"is a Krishnamurty Number")
else:
    print(t, "is not a Krishnamurty Number")