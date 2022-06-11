import random

import colorama
from colorama import Fore

l1={1:38,4:14,9:31,21:42,28:84,51:67,72:91,80:99}
s1={17:7,54:34,62:19,64:60,87:36,93:73,95:75,98:79}

g=[]
for i in range(1,101):
   g.append(i)

n1=input("Enter player 1 name=>")
n2=input("Enter player 2 name=>\n")
t=1
p1=0
p2=0
while t<=100:

   if t%2!=0:
      print("Now player",n1,"'s turn")
      x=random.randint(1,6)
      print("Dice =>", x)
      p1=p1+x
   #ladder
      for key,value in l1.items():
         if key==p1:
            p1=value
   #snake
      for key,value in s1.items():
         if key==p1:
            p1=value

      print("position =>",p1)
   #win

      g = []
      for i in range(1, 101):
         g.append(i)

      y1=p1-1
      if y1<99:
         g[y1] = "X"
      else:
         y1=99
         g[y1] =Fore.GREEN + "X"
         print("player",n1,"Won :)")
         t=110

   else:
      print("Now player", n2, "'s turn")
      x = random.randint(1, 6)
      print("Dice =>",x)
      p2=p2+x
      for key,value in l1.items():
         if key==p2:
            p2=value
      for key,value in s1.items():
         if key==p2:
            p2=value
      print("position =>", p2)


      g = []
      for i in range(1, 101):
         g.append(i)

      y2=p2-1
      if y2<99:
         g[y2]="Y"
      else:
         y2=99
         g[y2] =Fore.BLUE + "Y"
         print("player",n2,"Won :)")
         t=110


   print("_" * 50)
   print(g[99], "|", g[98], "|", g[97], "|", g[96], "|", g[95], "|", g[94], "|", g[93], "|", g[92], "|", g[91], "|",
         g[90], "|")
   print("_" * 50)
   print(g[80], "|", g[81], "|", g[82], "|", g[83], "|", g[84], "|", g[85], "|", g[86], "|", g[87], "|", g[88], "|",
         g[89], "|")
   print("_" * 50)
   print(g[79], "|", g[78], "|", g[77], "|", g[76], "|", g[75], "|", g[74], "|", g[73], "|", g[72], "|", g[71], "|",
         g[70], "|")
   print("_" * 50)
   print(g[60], "|", g[61], "|", g[62], "|", g[63], "|", g[64], "|", g[65], "|", g[66], "|", g[67], "|", g[68], "|",
         g[69], "|")
   print("_" * 50)
   print(g[59], "|", g[58], "|", g[57], "|", g[56], "|", g[55], "|", g[54], "|", g[53], "|", g[52], "|", g[51], "|",
         g[50], "|")
   print("_" * 50)
   print(g[40], "|", g[41], "|", g[42], "|", g[43], "|", g[44], "|", g[45], "|", g[46], "|", g[47], "|", g[48], "|",
         g[49], "|")
   print("_" * 50)
   print(g[39], "|", g[38], "|", g[37], "|", g[36], "|", g[35], "|", g[34], "|", g[33], "|", g[32], "|", g[31], "|",
         g[30], "|")
   print("_" * 50)
   print(g[20], "|", g[21], "|", g[22], "|", g[23], "|", g[24], "|", g[25], "|", g[26], "|", g[27], "|", g[28], "|",
         g[29], "|")
   print("_" * 50)
   print(g[19], "|", g[18], "|", g[17], "|", g[16], "|", g[15], "|", g[14], "|", g[13], "|", g[12], "|", g[11], "|",
         g[10], "|")
   print("_" * 50)
   print(g[0], "|", g[1], "|", g[2], "|", g[3], "|", g[4], "|", g[5], "|", g[6], "|", g[7], "|", g[8], "|", g[9], "|")
   print("_" * 50)

   t = t + 1














