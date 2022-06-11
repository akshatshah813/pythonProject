class poly:
    def __init__(self,h,w):
        self.h=h
        self.w=w

class tri(poly):
    def __init__(self,h,w):
        poly.__init__(self,h,w)
    def printarea(self):
        print("Area of triangle=",self,self.h*self.w*0.5)

class rect(poly):
    def __init__(self,h,w):
        poly.__init__(self,h,w)
    def printarea(self):
        print("Area of rectangle=",self,self.h*self.w)

t1=tri(100,200)
r1=rect(100,200)
t1.printarea()
r1.printarea()