class student:
    def __int__(self):
        self.s_no=0
        self.s_name=0
        self.s_maths=0
        self.s_english=0

    def datainput(self):
        self.s_no=int(input("Enter student number => "))
        self.s_name = input("Enter student name => ")
        self.s_maths= int(input("Enter maths marks=> "))
        self.s_english= int(input("Enter english marks => "))
        print("*"*40)

    def pdata(self):
        print("roll no.=", self.s_no, "Name =", self.s_name, " maths marks = ", self.s_maths, " english marks =",self.s_english)

    def code(self):
        tt=self.s_maths+self.s_english
        if z==1:
            print("roll no.=", self.s_no, "Name =", self.s_name, " maths marks = ", self.s_maths, " english marks =",
                  self.s_english,"total marks=",tt)
        elif z==2:
            if tt>=20:
                print("*"*40)
                print("Passed students")
                print("roll no.=", self.s_no, "Name =", self.s_name, " maths marks = ", self.s_maths,
                      " english marks =",
                      self.s_english, "total marks=", tt)
        elif z==3:
            if tt < 20:
                print("*" * 40)
                print("Failed students")
                print("roll no.=", self.s_no, "Name =", self.s_name, " maths marks = ", self.s_maths," english marks =",self.s_english, "total marks=", tt)
        else:
            print("Choose a valid option")

# 1=total marks 2= pass students 3= fail students
a1=int(input("Number of students=>"))
l1=[]

for i in range(1,a1+1):
    s1=student()
    s1.datainput()
    l1.append(s1)


while True:
    print("Choose an option:")
    print("1 => All students")
    print("2 => Passed Students")
    print("3 => Failed students")
    print("4 => exit")
    z=int(input("Enter your option => "))

    if z == 4:
        break

    for x in l1:
        x.code()