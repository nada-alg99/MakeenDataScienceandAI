# Using String Modulo Operator (%)
price= 1.2199967
discount = 5
item = "Milk"
print("The price is: %8.2f and the discount is: %2d , The Item is: %5s" %(price,discount,item))

#---------------------------------------------------------------------------------------------------------------------------

# Using the format() Method
#The general syntax of format() method is:
print("The price is: {0:8.2f} and the discount is: {1:2d} , The Item is: {2:5s}".format(5.94204,6,"Rice"))

print("The price is: {0:8.2f} and the discount is: {1:2d} , The Item is: {2:5s}".format(4.532,9,"Egg"))

#Formatting Output using String Method  str.center()
cstr = "Hello"
print(cstr.center(30, '#'))
#left aligned
print(cstr.ljust(30, '-'))
#Right aligned
print(cstr.rjust(30, '-'))