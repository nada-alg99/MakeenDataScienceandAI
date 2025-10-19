balance = 10000
target=20000
rate=0.05
year=0
while balance<=target:
    year=year+1
    interest=balance*rate
    balance=balance+interest
    print(year)
    

