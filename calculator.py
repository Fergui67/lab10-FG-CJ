"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def square_root(a):
    if a >= 0:
        math.sqrt(a)
    else:
        raise ValueError
def hypotenuse(a,b):
    math.hypot(a,b)
def add(a, b): 
    result = a + b
    return result
def subtract(a,b):
    subtraction = a - b
    return subtraction
def multiply(a,b):
    multiplication = a*b
    return multiplication
def divide(a,b):
    if a != 0:
        division = b/a
        return division
    else:
        raise ZeroDivisionError
def logarithm(a,b):
    if a < 1:
        raise ValueError
    else:
        log = math.log(b,a)
        return log
def exponent(a,b):
    expontential = a**b
    return expontential


def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    if a == 0:
        raise ValueError("Cannot divide by zero")
    result = b / a
    return result

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm base and argument must be positive")
    result = math.log(a, b)
    return result

def power(a, b):
    result = a ** b
    return result