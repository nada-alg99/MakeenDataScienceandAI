def factorial(number):
    result=1
    if number==0:
        return 1
    while number>=1:
        result=result *number
        number=number-1
    return result
print(factorial(4))