x=float(input("Enter marks of maths => "))
y=float(input("Enter marks of english => "))
z=float(input("Enter marks of science => "))

c=x+y+z

if c<100:
    if c>=50:
        print("your Grade is B")
    else:
        print("your Grade is C")
else:
    print("your Grade is A")
