pin=int(input("inter your PIN"))
mypin=1234
attempte=1
maximpt=3

while attempte<maximpt:
    attempte=attempte+1
    if pin != mypin:
        print("Incorrect PIN")
        pin=int(input("inter your PIN"))
        continue

    elif pin == mypin:
        print("Welcome")
        
        while pin!="q":
            
            print("1- checkBalance 2-deposit money 3-withdraw money 4-exit")
            choose=input("choose an option: ")
            balance=100
            
            
            if choose=="1":
                print("Your balance is", balance,"OMR")
            
            elif choose=="2":
                deposit=int(input("Enter deposit amount"))
                total=balance+deposit
                print("Deposit successful! new balance is",total,"OMR",deposit)
            
            elif choose=="3":
                withdraw=int(input("Enter withdraw amount: "))
                if withdraw>total:
                    print("Insufficient balance")
                else:
                    print("sufficient balance")
                    
            if choose=="4":
                print("Thank you for using our ATM do you want to continue enter number please")
                
                
print("Account locked.Try again later")     
            
    
        

        

