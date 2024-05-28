def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
       return "Error!,second input number can't be zero."
    else:
        return a / b
    
def calculator():
    print("Welcome to calculator!")
    print(" Select operation to be performed:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input( "Enter your choice (1/2/3/4):")

    num1 = float(input("Enter the first number:"))
    num2 = float (input("Enter second number:"))

    if choice == '1':
        print("Result:", add(num1,num2))
    elif choice =='2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1,num2))
    elif choice == '4':
        print("Result:", divide(num1,num2))
    else:
        print("Invalid input")
    
    again = input("want to perform another calculation? (y/n): ")
    if again.lower() == "y":
        calculator()
    else:
        print("Thank you for using calculator")

calculator()            