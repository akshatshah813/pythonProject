# 12 hour format

import time
import pyttsx3
engine = pyttsx3.init()


current=time.localtime(time.time())

x=current.tm_hour
y=current.tm_min

if x==13:
    z=x-1
    time=(z,"o'clock", y,"minutes")
elif x>=14:
    z=x-12
    time=(z,"o'clock", y,"minutes")


engine.say(time)
engine.runAndWait()