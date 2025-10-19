name='Muna'
for i in name:
    print(i)
    

name="Ahmed"
for i in range(5):
    print(i,name[i])
    
name=input("Enter your name")
n=len(name)
for i in range(n):
    print(i,name[i],end="")
    


for i in range(10,1,-2):
    print(i)
    
balance = 10000
years=5
rate= 0.05
for i in range(1,years+1):
    balance=balance+(balance*rate)
    print(i,balance)
    
    
    
    
