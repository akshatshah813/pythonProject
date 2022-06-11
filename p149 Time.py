import time

current=time.localtime(time.time())

print("Year:",current.tm_year)
print("month:",current.tm_mon)
print("day:",current.tm_mday)
print("weekday:",current.tm_wday)
print("Yearday:",current.tm_yday)
print("Hour:",current.tm_hour)
print("Minutes:",current.tm_min)
print("Seconds:",current.tm_sec)