# calculator.py
import math
def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        print("Invalid operation")
    else:
        return x/y
def power(x,y):
    return math.pow(x,y)
def square_root(x):
    return math.sqrt(x)
def logarithm(x,base):
    return math.log(x,base)
print("The choices are: 1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Power 6.Square Root 7.Logarithm")
choice=int(input("Select from the above choices: "))
if choice in [1,2,3,4,5]:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    match choice:
        case 1:
            print(f"Result: {addition(a,b)}")
        case 2:
            print(f"Result: {subtraction(a,b)}")
        case 3:
            print(f"Result: {multiply(a,b)}")
        case 4:
            print(f"Result: {divide(a,b)}")
        case 5:
            print(f"Result: {power(a,b)}")
elif choice==6:
    a=int(input("Enter number: "))
    print(f"Result: {square_root(a)}")
elif choice==7:
    a=int(input("Enter number: "))
    c=10
    print(f"Result: {logarithm(a,c)}")
print("Thank You")