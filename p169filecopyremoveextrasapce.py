f1 = open("C:\\Users\\DELL\\PycharmProjects\\india.txt",'r')
f3 = open("C:\\Users\\DELL\\PycharmProjects\\INDIA2.txt",'w')
s=0
while True:
    c=f1.read(1)
    if not c:
        break
    if c!=" ":
        f3.write(c)
        s=0
    else:
        s=s+1
        if s==1:
           f3.write(c)

f1.close()
f3.close()
print("Done")

#raja     rani      adsfdsa  esdfsd      sdafdasf        sadfdsaf
#raja rani ad

