email=input("Enter your Email Address =>")


y=email.count('.')
z=email.count('@')

if (y>=1 and y<3) and z==1:
    print("Enter valid email address")
else:
    print("Youer email address is VALID")