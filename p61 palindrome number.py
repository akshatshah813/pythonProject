x=int(input("Enter your number => \n"))
rev=0
n=x
while x>0:
    rem=x%10
    rev=(rev*10)+rem
    x=x//10
print(rev)

if rev==n:
    print("its a palindrome number")
else:
    print("it's not a palindrome number")