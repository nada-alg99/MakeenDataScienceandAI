c=float(input("Enter temperature in celsius: "))
f=c*(9/5)+32
c1=(f-32)*(5/9)
if c==c1:
    print("Conversion is perfect")
    
else:
    print("Conversion is not exact, it is",c)


x= int(input("Enter a number: "))
if x >= 0:
    print("The number is positive")
    if x % 3 == 0:
        print("and divisible by 3")
    else:
        print("but not divisble by 3")
else:
    print("The number is negative")