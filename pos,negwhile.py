positive=[]
negative=[]

while True:
    inputStr = input("Enter an element or q to exit")
    if inputStr =='q':
        break
    else:
        inputStr =int(inputStr)
        if inputStr >= 0:
            positive.append(inputStr)
        else:
            negative.append(inputStr)
            
print(positive,negative)
    