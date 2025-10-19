numbers=[2,1,4,20,4]

for i in numbers:
    if i%2==0:
        print(i,"The number is even")
    else:
        print(i,"The number is odd")
        

numbers=[2,1,4,20,4]

for i in range(len(numbers)):
    if numbers[i]%2==0:
        print(numbers[i],"The number is even")
    else:
        print(numbers[i],"The number is odd")