import time

current=time.localtime(time.time())

x= current.tm_hour
y= current.tm_min
if (x>=5 and x<=8):
    print("Current time => ",x,":",y)
    print("Good Morning")
elif (x>=13 and x<17):
    print("Current time => ", x,":",y)
    print("good Afternoon")
elif (x>=17 and x<=19):
    print("Current time => ", x,":",y)
    print("Good Evening")
elif (x>=21 and x<=4):
    print("Current time => ", x,":",y)
    print("Good Night")