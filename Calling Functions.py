# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:58:30 2024

@author: noodl
"""
import math

#Question 1
print(round(9.50))

#Question 2
var = input("Enter a float value: ")
print(round(float(var)))

#Question 3
numOne = float(input("Enter the first number: "))
numTwo = float(input("Enter the second number: "))
numThree = float(input("Enter the third number: "))

print(pow(numOne, numThree))
print(pow(numOne, pow(numTwo, numThree)))
print(math.fabs(numTwo))
print(math.sqrt(pow((numOne * numTwo), numThree)))

#Question 4
numOne = int(input("Enter the first integer: "))
numTwo = int(input("Enter the second integer: "))

if numOne > numTwo:
    print(numOne, "is the maximum.")
    print(numTwo, "is the minimum.")
else:
    print(numTwo, "is the maximum.")
    print(numOne, "is the minimum.")
    