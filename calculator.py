# Fast Python Calculator
# Extended version with power, square root, and trigonometric functions.

import math  # math library is needed for square root and trigonometry

# Ask the user to enter the first number.
number1 = float(input("Enter the first number: "))

# Ask the user to enter the second number.
number2 = float(input("Enter the second number: "))

# Ask the user to choose an operation.
operation = input("Choose operation (+, -, *, /, ^, sqrt, sin, cos, tan): ")

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
    print("Result:", number1 ** number2)
elif operation == "sqrt":
    if number1 >= 0:
        print("Result:", math.sqrt(number1))
    else:
        print("Error: Cannot calculate square root of a negative number.")
elif operation == "sin":
    # Convert degrees to radians before using math.sin
    print("Result:", math.sin(math.radians(number1)))
elif operation == "cos":
    print("Result:", math.cos(math.radians(number1)))
elif operation == "tan":
    print("Result:", math.tan(math.radians(number1)))
else:
    print("Unknown operation.")
