class student:
    def __int__(self):
        self.s_no=0
        self.s_name=0

    def data_input(self):
        self.s_no=input("Enter roll number =>")
        self.s_name=input("Enter Student name =>\n")
        print("*"*30)


    def p_data(self):
        print("roll no. =",self.s_no,"\tname =",self.s_name)

    def comp(self,x):
        z=self.s_no
        print(z,x,z==x)


a1=int(input("Enter number of students =>"))
l1=[]

for i in range(1,a1+1):
    s1=student()
    s1.data_input()
    l1.append(s1)
x=int(input("Enter the roll number ==>"))

for y in l1:
    if y.s_no==x:
        y.p_data()