f1=open("C:\\Users\\DELL\\PycharmProjects\\abcde.txt",'r')
s=0
while True:
    c=f1.read(1)
    if not c:
        break
    if (c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
        s=s+1
f1.close()

#----------------------------------
print("Total Vowels are ",s)