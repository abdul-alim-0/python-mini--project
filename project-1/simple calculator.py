# Function definitions for basic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def modulus(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Main function to run the calculator
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    
    try:
        choice = int(input("Enter choice (1/2/3/4/5): "))
        
        if choice in [1, 2, 3, 4, 5]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == 1:
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == 2:
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == 3:
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == 4:
                result = divide(num1, num2)
                if result != "Error: Division by zero is not allowed.":
                    print(f"{num1} / {num2} = {result:.2f}")
                else:
                    print(result)
            elif choice == 5:
                result = modulus(num1, num2)
                if result != "Error: Division by zero is not allowed.":
                    print(f"{num1} % {num2} = {result}")
                else:
                    print(result)
        else:
            print("Error: Invalid operation choice. Please select a valid option.")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
