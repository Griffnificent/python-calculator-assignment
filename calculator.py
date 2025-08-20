def calculator():
    """
    A simple calculator program that performs a user-specified operation on two numbers.
    """
    try:
        # Get the first number from the user
        num1 = float(input("Enter the first number: "))
        
        # Get the second number from the user
        num2 = float(input("Enter the second number: "))
        
        # Get the operation from the user
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Perform the calculation based on the user's input
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            # Check for division by zero
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error! Division by zero is not allowed.")
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Run the calculator program
calculator()