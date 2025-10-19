
time1=input()
print(time1.split(":"))
time2=input()
print(time2.split(":"))

hr1=time1.split(":",1)
print(hr1)
    

    

        
if hr1<hr2:
    print("time1 comes first")
elif hr1>hr2:
    print("time2 comes first")
    
elif hr1==hr2:
    if mn1>mn2:
        print("time2 comes first")
    elif m1<m2:
        print("time1 comes first")
    else:
        print("time1 same as time2")
        
        
        
            