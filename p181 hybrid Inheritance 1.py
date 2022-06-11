class stu:
    def __init__(self,no,name):
        self.no=no
        self.name=name
    def showstu(self):
        print("No=",self.no,"Name=",self.name)

class marks(stu):
    def __init__(self,eng,hindi):
        self.eng=eng
        self.hindi=hindi
    def showmarks(self):
        print("English =",self.eng,"Hindi =",self.hindi)

class sports(stu):
    def __init__(self,cricket):
        self.cricket=cricket
    def showsports(self):
        print("Cricket =",self.cricket)

class result(marks,sports):
    def __init__(self,no,name,eng,hindi,cricket):
        stu.__init__(self,no,name)
        marks.__init__(self,eng,hindi)
        sports.__init__(self,cricket)
    def showresult(self):
        print("Total =",(self.eng+self.hindi))

r1=result(11,"Ram",22,33,50)
r1.showstu()
r1.showmarks()
r1.showsports()
r1.showresult()