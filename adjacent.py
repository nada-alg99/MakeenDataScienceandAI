inputStr = input("Enter value: ")

while inputStr!="":
    previous=inputStr
    inputStr = input("Enter value: ")
    if inputStr ==previous:
        print("same number")
    inputStr = input("Enter value: ")

