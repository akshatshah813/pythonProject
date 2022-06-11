space=" "
str=input("Enter your sentence => ")

for s in str:
    if s!=" ":
        print(s,end="")
        c=0
    else:
        c=c+1
        if c==1:
            print(s,end="")
