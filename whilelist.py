lis = []
while True:
    inputStr = input("Enter an element or q to exit")
    
    if inputStr.isdigit():
        lis.append(int(inputStr))
        
    elif inputStr[0] == '-' and inputStr[1:].isdigit():
        lis.append(int(inputStr[1:])*-1)
        
    
    
    elif inputStr =='q':
        break
    else:
        lis.append(inputStr)
        
print(lis)