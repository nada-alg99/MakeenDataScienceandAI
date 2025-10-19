sum1=[]
thesum=0
counter=0
while True:
    inputStr = input("Enter an element or q to exit")
    
    
    if inputStr.isdigit() :
        sum1.append(int(inputStr))
        
    elif inputStr[0] == '-' :
        sum1.append(int(inputStr[1:])*-1)
        
    elif inputStr =='q':
        break
    
    thesum=sum(sum1)
    counter=counter+1
print(sum1)  
print("the sum is",thesum)

