name = "admin".upper()
realpassword=12345
username = input("Enter username: ").upper()
password=int(input("Enter password: "))

if name == username and realpassword == password:
    print("you can access")
else:
    print("you cant access")
    
    
  
x=int(input("Enter number: "))
c1=x % 3
c2=x % 5
if c1==0 or c2==0:
    print("the number is divisible by 3 or 5")
else:
    print(" the number is not divisible by 3 or 5")

