#AM PM

import time

current=time.localtime(time.time())
x= current.tm_hour
y= current.tm_min

if x<12:
    print("Current time => ", x, ":", y)
    print("AM")
else:
    print("Current time => ", x, ":", y)
    print("PM")