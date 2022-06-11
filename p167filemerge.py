f1 = open("C:\\Users\\DELL\\PycharmProjects\\india.txt", 'r')
f2 = open("C:\\Users\\DELL\\PycharmProjects\\usa.txt", 'r')
f3 = open("C:\\Users\\DELL\\PycharmProjects\\russia.txt", 'w')

while True:
    c=f1.read(1)
    if not c:
        break
    f3.write(c)

while True:
    c=f2.read(1)
    if not c:
        break
    f3.write(c)

f1.close()
f2.close()
f3.close()
"""
2 while loops f1->f3 f2->f3
"""
print("Done")