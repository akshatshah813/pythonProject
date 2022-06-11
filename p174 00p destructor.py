class Student:
    def __init__(self,no,name):
        self.no=no
        self.name = name

    def __del__(self):
        print("Destructor started")

    def printdetails(self):
        print("no = ",self.no," name = ",self.name)

s1=Student(1,"Ram")
s2=Student(2,"Sita")
s1.printdetails()
s2.printdetails()
del s1
del s2
s1.printdetails()