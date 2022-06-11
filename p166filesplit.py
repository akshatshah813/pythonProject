f1=open("C:\\Users\\DELL\\PycharmProjects\\abcde.txt",'r')
f2=open("C:\\Users\\DELL\\PycharmProjects\\vowel.txt",'w')
f3=open("C:\\Users\\DELL\\PycharmProjects\\conso.txt",'w')

while True:
    c=f1.read(1)
    if not c:
        break
    if (c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
        f2.write(c)
    else:
        f3.write(c)
f1.close()
f2.close()
f3.close()
print("Done")