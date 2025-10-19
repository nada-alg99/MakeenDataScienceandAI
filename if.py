price = float(input("Enter the price: "))
if price >200:
    discount=price*0.05
    print("discount",discount)
else:
    print("no discount")
    if price <=10:
        print("Take it free")
    else:
        print("no discount")
        print("End")
        
        


price = float(input("Enter the price:"))
if price >200:
    disc="you have discount"
    print(disc)
else:
    disc="you do not have discount"
    print(disc)
   
    
    
    
age = 24
compare = 30
if age>=compare:
    print("you are senior")
    
else:
    print("you are still young")
    
    



name = "Ali".upper()
username = input("Enter username: ").upper()

if name == username:
    print("you can access")
else:
    print("you cant access")
#------------------------------------------------------
    
myage=20
yourage=int(input("Enter your age:"))
if myage > yourage:
    print("Iam older")
else:
    print("you are older")
    
              