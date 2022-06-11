#153= 1*1*1 + 5*5*5 + 3*3*3
x=int(input("Enter your number => \n"))
n=x%10
s=0
i=1
y=1
t=x
while x>0:
    rem=x%10
    y=rem**n
    i=i+1
    s=s+y
    x=x//10

if s==t:
    print("it's an armstrong number")
else:
    print("it's not an armstrong number")