f1=open("C:\\Users\\DELL\\PycharmProjects\\abcde.txt",'r')
s=0
while True:
    c=f1.read(1)
    if not c:
        break
    if (c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
        c=7
    print(c, end="")
f1.close()

#---------------------------------- raja r7j7
