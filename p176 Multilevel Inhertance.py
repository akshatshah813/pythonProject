class sheru:
    def show(self):
        print("hi I am Sheru. I am Parent ")

class monty(sheru):
    def display(self):
        print("Hi I am Monty. I am Child")

class romeo(monty):
    def printdata(self):
        print("Hi I am Romeo. I am Child of Monty")

r1=romeo()
r1.show()
r1.display()
r1.printdata()
