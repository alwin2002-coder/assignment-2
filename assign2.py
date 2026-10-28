print("-----easy calculator-----")

while True:
    
    number1=int(input("enter the first number:"))
    number2=int(input("enter the second number:"))

    print("examble=","+","or","-","or","*","or","/","or","%","or","//")
    opt=input("enter the operator:")

    if opt=="+":
        print(number1+number2)
    elif opt=="-":
        print(number1-number2)   
    elif opt=="*":
        print(number1*number2)
    elif opt=="/":
        print(number1/number2)
    elif opt=="%":
        print(number1%number2)
    elif opt=="//":
        print(number1//number2)
    else:
        print("invalid operator")    


    again=input("do again?  enter yes or no:")  

    if again !="yes": 
        break 

print("thank you")
 

