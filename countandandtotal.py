count=0
inputStr = input("Enter value: ")
total=0
while inputStr!="":
    value=int(inputStr)
    if value<0:
        count=count+1
        total=total+value
    inputStr = input("Enter value: ")
print(count,total)


    
