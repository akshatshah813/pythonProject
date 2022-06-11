class a:
    def methodA(self):
        print("A class")

class b(a):
    def methodB(self):
        super().methodA()
        print("B class")

b=b()
b.methodB()