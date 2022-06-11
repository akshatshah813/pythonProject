f1=open("C:\\Users\\DELL\\PycharmProjects\\abcde.txt",'r')

while True:
    c=f1.read(1)

    if not c:
        break
    print(c,end="")

f1.close()