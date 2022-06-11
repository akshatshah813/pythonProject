class stu:
    def __init__(self):
        self.no=5
        self.name="ram"

    def showstu(self):
        print("No =",self.no,"Name =",self.name)

class marks(stu):
    def __init__(self):
        stu.__init__(self)
        self.eng=50
        self.hindi=30

    def showmarks(self):
        print("English =",self.eng,"Hindi =",self.hindi)

class result(marks):
    def __init__(self):
        marks.__init__(self)

    def showresult(self):
        print("Total=",(self.eng+self.hindi))

r1=result()
r1.showstu()
r1.showmarks()
r1.showresult()