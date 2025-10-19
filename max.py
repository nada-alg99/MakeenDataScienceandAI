inputStr = input("Enter value: ")
maxm=0

while inputStr!="":
    value=int(inputStr)
    if value>maxm:
        maxm=value
    inputStr = input("Enter value: ")
print("The biggest number is: ",maxm)