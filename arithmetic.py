"""Math functions for calculator."""
def add(num1, num2):
    """Return the sum of the two inputs."""
    summation = num1 + num2
    return summation


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    minus = num1 - num2
    return minus

def multiply(num1, num2):
    """Multiply the two inputs together."""
    times = num1 * num2
    return times

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    division = num1 / num2
    return division  


def square(num1):
    """Return the square of the input."""
    squared = num1 ** 2
    return squared

def cube(num1):
    """Return the cube of the input."""
    cubed = num1 ** 3
    return cubed

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    powered = num1 ** num2
    return powered

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    mody = num1 % num2
    return mody

while True:

    input_string = input(">")
    input_list = input_string.split(" ")

    if input_string == 'q':   
        print("Program quit!")
        break
    
    math_symbol = input_list[0]
    num1 = int(input_list[1])
    
    try: 
        num2 = int(input_list[2])
    except: IndexError     

    if math_symbol == '+':
        print(add(num1, num2))

    elif math_symbol == '-':

        print(subtract(num1, num2))

    elif math_symbol == '*':
        print(multiply(num1, num2))

    elif math_symbol == '/':
        print(divide(num1, num2))

    elif math_symbol == 'square':
        print(square(num1))

    elif math_symbol == 'cube':
        print(cube(num1))

    elif math_symbol == 'power':
        print(power(num1, num2))

    elif math_symbol == 'mod':
        print(mod(num1, num2))


