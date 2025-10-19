first = float(input("Enter first number:  "))
operator =input("The operator: ")
second = float(input("Enter second number:  "))

while operator!="q":
  
    if operator == "*":
        print("the answer is", (first) * (second))
    
    elif operator == "-":
        print("the answer is", (first) - (second))
    elif operator == "+":
        print("the answer is", (first) + (second))
    
    elif operator == "/":
        print("the answer is", (first) / (second))
    
    elif operator == "*0.5":
        print("the answer is", (first) *0.5)
    
    

    operator= input("please enter the operator or q to stop  ")
    if operator != "q":
        first= float(input ("please enter the first number:  "))
        secand=float(input ("please enter the first number:  "))


    