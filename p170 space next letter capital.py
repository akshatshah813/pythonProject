f1= open("C:\\Users\\DELL\\PycharmProjects\\india.txt",'r')
f2= open("C:\\Users\\DELL\\PycharmProjects\\firstLetterCapital.txt",'w')

while True:
    c=f1.read(1)
    if not c:
        break
    s = 0
    if c == " ":
        s=s+1
        if s==1:
            c=c.upper()


f1.close()
f2.close()
print("Done")