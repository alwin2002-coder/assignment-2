a=int(input("enter the number:"))
n= a-1


while a%n==0:
    n-=1
    if n==2:
     break 
if a%n==0:
    print("Given number is not a prime number")
else:    
    print("It's a prime number")








# if %n==0:
#     print("given number is not prime number")

# else:
#     print("its a prime number")  