class bank:
    def __init__(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance

    def printdata(self):
        print("Account Number =",self.acno,"Name =",self.cname,"Balance =",self.balance)

    def deposit(self):
        amt=int(input("Enter the deposit => "))
        self.balance=self.balance + amt
        print("Account Number =", self.acno, "Name =", self.cname, "Balance =", self.balance)

    def withdrawn(self):
        amt=int(input("Enter the widthdraw amount =>"))
        self.balance = self.balance - amt
        print("Account Number =", self.acno, "Name =", self.cname, "Balance =", self.balance)

b1=bank(1,"Ram",20000)
b1.printdata()
b1.deposit()
b1.printdata()
b1.withdrawn()
b1.printdata()
