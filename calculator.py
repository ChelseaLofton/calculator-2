"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    input_string = input("Please provide an operator and the numbers to calculate: ")
    tokens = input_string.split(' ')

    if "q" in tokens:
        print("You will exit the calculator.")
        break
    
    operator = tokens[0]
    num1 = tokens[1]
    
    if len(tokens) < 3:
        num2 = 0
    else:
        num2 = tokens[2]
    
    result = None
    
    if operator == "+":
        result = add(float(num1), float(num2))
    elif operator == "-":
        result = subtract(float(num1), float(num2))
    elif operator == "*":
        result = multiply(float(num1), float(num2))
    elif operator == "/":
        result = divide(float(num1), float(num2))
    elif operator == "square":
        result = square(float(num1))
    elif operator == "cube":
        result = cube(float(num1))
    elif operator == "power":
        result = power(float(num1), float(num2))
    elif operator == "mod":
        result = mod(float(num1), float(num2))

    print(result)