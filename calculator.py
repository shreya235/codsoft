# task calculator
# Take input from user
num1 =  int(input("enter first number here: "))
num2 = int(input("enter second number here: "))
# select operation
print ("press 1 for addition")
print("press 2 for substraction")
print("press 3 for multiplication")
print("press 4  for division")
 
# choice 

choice = int(input("Enter your choice from 1-4"))

if choice == 1:
    print ( "The addition of given two numbers is",num1 + num2)
elif choice == 2:
    print ("The substraction of given two numbers is",num1 - num2)
elif choice == 3:
    print("The multiplication of given two numbers is", num1 * num2)
elif choice == 4:
    print("The division of given two numbers is",num1 / num2)
else:
    print("Invalied Input")


