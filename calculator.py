"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    addition = a + b
    return addition
def subtract(a,b):
    subtraction = a - b
def multiply(a,b):
    multiplication = a*b
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
def exponent(a,b):
    expontential = a**b
    return expontential


