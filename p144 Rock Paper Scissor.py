import random

l1=["Rock","Paper","Scissor"]

n1=input("Enter player's name => ")
n2=input("Enter player's name => ")
w1=0
w2=0
t=0
n=1

while n<=3:
    x=random.randint(1,3)
    y=random.randint(1,3)

    print("Round",n)
    print(n1,"=>",l1[x])
    print(n2, "=>", l1[y])

    if (x==1 and y==3) or (x==2 and y==1) or (x==3 and y==2):
        print(n1,"Won this round")
        w1=w1+1
    elif (y==1 and x==3) or (y==2 and x==1) or (y==3 and x==2):
        w2=w2+1
        print(n2,"Won this round")
    elif (x==1 and y==1) or (x==2 and y==2) or (x==3 and y==3):
        print("It's a Tie")
        t=t+1
        n=n-1
    n=n+1

if w1>w2:
    print("Total  rounds played ",(w1+w2+t))
    print("Tied Rounds ",t)
    print("Player ",n1,"won the Game :)")
else:
    print("Player ",n2,"won the Game :)")