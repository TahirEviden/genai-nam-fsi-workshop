# Defining functions for arithmetic operations
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Result will be zero, becuase value is Division by zero"

while True:
    print("Select arthimatic operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
# Getting user input for choice
    choice = input("Enter choice (1/2/3/4/5): ")
# Check if the user wants to exit
    if choice == '5':
        print("Exit the calculator.")
        break
# Check if the user input is a valid operation
    if choice in ('1', '2', '3', '4'):
 # Get user input for two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
# Perion and display the result
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {sub(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {mult(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {div(num1, num2)}")
# Displaying an error message for invalid input
    else:
        print("Invalid input. Please enter a valid choice.")