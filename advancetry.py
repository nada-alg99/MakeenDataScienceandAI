pin=""
mypin=1234
attempte=0
maximpt=3
balance=100
while pin!="q":
    attempte=attempte+1
    pin=int(input("inter your PIN"))
    if attempte==maximpt:
        print("Account locked")
    
    if pin == mypin:
        print("Welcome")
        print("1- checkBalance 2-deposit money 3-withdraw money 4-exit")
        choose=input("choose an option: ")
        if choose=="1":
            print("Your balance is", balance,"OMR")
        elif choose=="2":
            deposit=int(input("Enter deposit amount"))
            total=balance+deposit
            print("Deposit successful! new balance is",total,"OMR")
        elif choose=="3":
            withdraw=int(input("Enter withdraw amount: "))
            if withdraw>total:
                print("Insufficient balance")
            else:
                print("sufficient balance")
    elif pin != mypin:
        print("Incorrect PIN")        
        


    
