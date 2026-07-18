# Fast Python Calculator
# Extended version with power and square root operations.

import math  # math library is needed for square root

# Ask the user to enter the first number.
number1 = float(input("Enter the first number: "))

# Ask the user to enter the second number.
number2 = float(input("Enter the second number: "))

# Ask the user to choose an operation.
operation = input("Choose operation (+, -, *, /, ^, sqrt): ")

# Decide which operation to perform based on the user's choice.
if operation == "+":
    print("Result:", number1 + number2)
elif operation == "-":
    print("Result:", number1 - number2)
elif operation == "*":
    print("Result:", number1 * number2)
elif operation == "/":
    if number2 != 0:
        print("Result:", number1 / number2)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == "^":
    # Power operation: number1 raised to number2
    print("Result:", number1 ** number2)
elif operation == "sqrt":
    # Square root operation: only uses number1
    if number1 >= 0:
        print("Result:", math.sqrt(number1))
    else:
        print("Error: Cannot calculate square root of a negative number.")
else:
    print("Unknown operation.")
