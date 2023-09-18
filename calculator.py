# write a python code for creating a calculator.
# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main function to take user input and perform calculations
def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Take user input for operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the choice is valid
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice")
        return

    # Take user input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        result = divide(num1, num2)
        if result != "Cannot divide by zero":
            print("Result:", result)
        else:
            print(result)

# Run the calculator
if __name__ == "__main__":
    calculator()