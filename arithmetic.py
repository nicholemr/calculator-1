"""Math functions for calculator."""
# a_variable = input("type a function")

# num1 = a_variable[2]
# num2 = a_variable[4]



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

# if '+' in a_variable:
#     print(add(num1,num2))
