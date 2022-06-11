f1=open("C:\\Users\\DELL\\PycharmProjects\\abcde.txt",'r')
s=0
while True:
    c=f1.read(1)
    if not c:
        break
    if c==" ":
        c=''
    print(c,end="")
f1.close()

#---------------------------------- raja rani -> rajarani