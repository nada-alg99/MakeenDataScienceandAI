total=0.0
salary= 0.0
count=0

while salary>=0.0:
    salary= float(input("Plese Enter the salary or -1 to end"))
    if salary >=0.0:
        total=total+salary
        count=count+1
        
    
avg=total/count
print(avg)
print(count)
print(total)