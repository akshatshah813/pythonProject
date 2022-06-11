# 12 hour format

import time

current=time.localtime(time.time())

x=current.tm_hour
y=current.tm_min

if x==13:
    z=x-1
    print("Current time => ", z, ":", y)
elif x>=14:
    z=x-12
    print("Current time => ", z, ":", y)