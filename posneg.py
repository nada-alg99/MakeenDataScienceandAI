poslist=[]
neglist=[]
while True:
    inputStr = input("Enter an element or q to exit")
    
    if inputStr.isdigit():
        poslist.append(int(inputStr))
        
    elif inputStr[0] == '-' :
        neglist.append(int(inputStr[1:])*-1)
        
    elif inputStr =='q':
        break
    
print(poslist)
print(neglist)


