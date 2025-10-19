#Q1
name=input("Enter your name: ")
age=input("Enter your age: ")
print("Hello",name,",","you are",age,"years old")

#Q2
first=int(input("Enter first number: "))
second=int(input("Enter second number: "))
add=first+second
print("The sum is",add)

#Q3
firstnum=int(input("Enter first number: "))
secondnum=int(input("Enter second number: "))
right=firstnum>secondnum
print("Is the first number greater?",right)

#Q4
age=int(input("Enter your age: "))
nationality=input("Enter second number: ").upper()
if age>=18 and nationality=="omani".upper():
    print("You are aligible to vote")
else:
    print("you are not eligible to vote")
    
#Q5
num=int(input("Enter a number: "))
if num>=0:
    print("The number is positive")
else:
    print("The number is not positive")

#Q6
x= int(input("Enter a number: "))
if x % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
    
#Q7
marks=int(input("Enter marks: " ))
if marks >=90:
    print("Excellent")
elif 70<=marks<90:
    print("Good")
elif 50<=marks<70:
    print("pass")
else:
    print("Fail")
    
#Q8
age=int(input("Enter your age: "))
license=input("Do you have a driving licence? ")
if age>=18:
    if license=="yes":
        print("you can drive")
    elif license=="no":
        print("you need a licence to drive")
else:
    print("You are yoo young to drive")
    
#Q9
counter=1
while counter <=5:
    print(counter)
    counter = counter + 1

    
#Q10
    
y=int(input("Enter a number: "))
counter=0


while counter <=y:
    counter=counter+1
    if counter % 2 == 0:
        print(counter)
    
    
    
