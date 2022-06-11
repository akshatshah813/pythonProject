x=int(input("Enter your number => \n"))
rev=0
n=x
while x>0:
    rem=x%10
    rev=rev+(rem*rem*rem)
    x=x//10
print(rev)

if rev==n:
    print("it's a armstrong number")
else:
    print("it's not a armstrong number")