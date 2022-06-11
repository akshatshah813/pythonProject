class stu:
    def __init__(self,no,name):
        self.no=no
        self.name=name

    def showstu(self):
        print("No=",self.no,"Name=",self.name)

class marks:
    def __init__(self,eng,hindi):
        self.eng=eng
        self.hindi=hindi

    def showmarks(self):
        print("English=",self.eng,"Hindi=",self.hindi)

class result(stu,marks):
    def __init__(self,no,name,eng,hindi):
        stu.__init__(self,no,name)
        marks.__init__(self,eng,hindi)

    def showresult(self):
        print("Total=",(self.eng+self.hindi))

r1=result(1,"Ram",22,33)
r1.showstu()
r1.showmarks()
r1.showresult()