price= 1.2199967
discount = 5
item = "Milk"
print("The price is: %10.5f and the discount is %d ,Item is %5s" %(price,discount,item))


greet = "Good morning"
print(greet.upper())
print(greet.lower())


title ="python for everyone Python for everyone"
title = title.replace("everyone", "Everyone",2) 
print(title)


quote = 'Let it be, let it be, let it be'

result1 = quote.find('let it')
result2 = quote.find('small')
result3 = quote.find('let it',12,14)
r4= quote.find('let it',12)

print(result1)
print(result2)
print(result3)
print(r4)

floor = input("Enter the floor number: ")
floor =int(floor)

if floor ==13:
    print("Invalid input please enter floor again")
    

floor = input("Enter the floor number: ")
floor =int(floor)

if floor>13:
    actualFloor = floor - 1
else:
    actualFloor = floor
    
print("The actual floor is:",actualFloor)



















