class sheru:
    def show(self):
        print("hi I am Sheru. I am Parent ")

class monty(sheru):
    def display(self):
        print("Hi I am Monty. I am Child")

m1=monty()
m1.display()
m1.show()
