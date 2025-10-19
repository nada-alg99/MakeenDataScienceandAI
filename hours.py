hr1=int(input("Enter hr1 "))
mn1=int(input("Enter mn1 "))
time1=hr1,":",mn1
print(time1)

hr2=int(input("Enter hr2 "))
mn2=int(input("Enter mn2 "))
time2=hr2,":",mn2
print(time2)

if hr1==hr2:
    if mn1==mn2:
        print("the time1 is as time2")

if hr1>hr2:
    print("time2 comes first")
if hr1<hr2:
    print("time1 comes first")
        
    


    
    


