# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:23:55 2024
def addition(x, y):
    returns sum of x and y
    
def subtraction(x, y):
    returns the result of x - y
    
def multiplication(x, y):
    returns the product of x and y
    
def division(x, y):
    if the denominator is 0
        raise ZeroDivisionError
    returns the quotient of x and y
@author: noodl
"""

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return x / y