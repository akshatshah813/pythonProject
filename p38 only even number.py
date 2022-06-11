print("Options:")
print("1 => Even")
print("2 => Odd")
y=int(input("choose your option => "))

x=int(input("enter the number limit => \n"))

if y==1:
    for i in range(1,x+1):
        if i%2==0:
            print(i," is even")
elif y==2:
    for i in range(1,x+1):
        if i%2!=0:
            print(i," is odd")
else:
    print("Enter valid option")
