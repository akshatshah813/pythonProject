g=['_','_','_','_','_','_','_','_','_']

t=1
p1=input("Enter player 1 name=>")
p2=input("Enter player 2 name=>")

while t<=9:

    if t%2==0:
        print("now ",p2,"'s turn")
        n=int(input("Enter your position =>"))
        if g[n - 1] == '_':
            g[n - 1] = "X"
        else:
            print("Position Already Filled, Choose other position")
            t = t - 1

    else:
        print("now ",p1,"'s turn")
        n=int(input( "Enter your position =>"))
        if g[n - 1] == '_':
            g[n - 1] ='O'
        else:
            print("Position Already Filled, Choose other position")
            t = t - 1



    print("After ",t,"turn")
    print(g[0],"|",g[1],"|",g[2])
    print("_"*10)
    print(g[3],"|",g[4],"|",g[5])
    print("_"*10)
    print(g[6],"|",g[7],"|",g[8])

    #logic
    if (g[0]=='X' and g[1]=='x' and g[2]=='x') or (g[3]=='X' and g[4]=='x' and g[5]=='x') or (g[6]=='X' and g[7]=='x' and g[8]=='x') or (g[0]=='X' and g[3]=='x' and g[6]=='x') or (g[1]=='X' and g[4]=='x' and g[7]=='x') or (g[2]=='X' and g[5]=='x' and g[8]=='x') or (g[0]=='X' and g[4]=='x' and g[8]=='x') or (g[2]=='X' and g[4]=='x' and g[6]=='x'):
        print("Player ",p2,"Won :)")
        t=12
    elif (g[0]=='O' and g[1]=='O' and g[2]=='O') or (g[3]=='O' and g[4]=='O' and g[5]=='O') or (g[6]=='O' and g[7]=='O' and g[8]=='O') or (g[0]=='O' and g[3]=='O' and g[6]=='O') or (g[1]=='O' and g[4]=='O' and g[7]=='O') or (g[2]=='O' and g[5]=='O' and g[8]=='O') or (g[0]=='O' and g[4]=='O' and g[8]=='O') or (g[2]=='O' and g[4]=='O' and g[6]=='O'):
        print("Player ",p1,"Won :)")
        t=12

    t=t+1

if t==10:
    print("It's a TIE")