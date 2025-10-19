string=input("enter: ")
uppercase=0
for char in string:
    if char.isupper():
        uppercase = uppercase +1
print(uppercase)
#-----------------------------------
word=input("enter the word")
vowels=0
for char in word:
    if char.lower() in "aeiou":
        vowels = vowels +1
print(vowels)
#-----------------------------------
sentence = input("Enter a sentence: ")
for i in range(len(sentence)):
    if sentence[i].isupper():
        print(i)
#-----------------------------------
string=input("Enter " )
found=False
position = 0
while not found and position < len(string):
    if string[position].isdigit():
        found=True
    else:
        position = position +1
if found:
    print("First digit occurs at position",position)
else:
        print("The string does not contain a digit.")


#-------------------------------------------------------
string=input("Enter")
found=False
position=len(string)-1
while not found and position >=0:
    if string[position].isdigit():
        found = True
    else:
        position = position - 1
        
#------------------------------------------------------
string=input("Enter phone in the format (XXX)XXX-XXXX:")
valid=len(string)==13
position=0
while valid and position <len(string):
    
    if position == 0:
        valid = string[position] =="("
    elif position == 4:
        valid = string[position] == ")"
    elif position ==8:
        valid = string[position] =="-"
    else:
        valid = string[position].isdigit()
    position = position+1
    
    
if valid :
    print("The string contains a valid phone number.")
else:
    print("The string does not contain a valid phone number.")
#---------------------------------------------------------
userInput = input("Enter a credit card number: ")
creditCardNumber=""
for char in userInput:
    if char !=" " and char !="-":
        creditCardNumber = creditCardNumber + char
print(creditCardNumber)
   

