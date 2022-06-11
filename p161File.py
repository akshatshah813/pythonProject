f1=open("C:\\Users\\DELL\\PycharmProjects\\abcde.txt",'r')
s=0
while True:
    c=f1.read(1)
    if not c:
        break
    if c==" ":
        s=s+1
f1.close()

print("Total spaces are ",s)