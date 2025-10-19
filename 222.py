price=input("Enter the total price")
price=float(price)
persent= price*0.05
discount=price-persent

if price>=200:
    print("the price after discount is:", discount)
    
else:
    print("the discount not valid the price:" ,price)
    