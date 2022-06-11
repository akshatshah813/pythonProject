f1=open("C:\\Users\\DELL\\PycharmProjects\\abcde.txt",'r')
f2=open("C:\\Users\\DELL\\PycharmProjects\\pqr.txt",'w')
while True:
    c=f1.read(1)
    if not c:
        break
    f2.write(c)
f1.close()
f2.close()

print("Copied")
