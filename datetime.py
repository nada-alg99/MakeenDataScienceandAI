from datetime import datetime

timeFormat="%H:%M"

time1 = datetime.strptime(input("Enter time1: "), timeFormat)
time2 = datetime.strptime(input("Enter time2: "), timeFormat)

if time1==time2:
        print("the time1 is as time2")
elif time1>time2:
    print("time2 comes first")
else:
    print("time1 comes first")