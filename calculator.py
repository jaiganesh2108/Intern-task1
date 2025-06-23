# Calculator CLI App

# Functions for operations like add, sub, mul, div.
def addition(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "Error: Division by zero"
    return x/y

# claculation stuff's
def calculator():
    print("Welcome to the CLI Calculator!")
    print("operations: '+' for addition, '-' for subtraction, '*' for multiplication, '/' for divition")
# looping
    while True:
        try:
            num1 = float(input("Enter the first number:"))
            operator = input("Enter the oprator( +, -, *, /): ").strip()
            num2 = float(input("Enter the second number:"))

            if operator == '+':
                result = addition(num1,num2)
            elif operator == '-':
                result = subtract(num1,num2)
            elif operator == '*':
                result = multiply(num1,num2)
            elif operator == '/':
                result = divide(num1,num2)
            else:
                print("Invalid operator. Try again.")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

# for performing another operation
        choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            print("Continuing.....")
        else:
            print("Thank you for using the calculator!")
            break

# program starts from here!
if __name__ == "__main__":
    calculator()