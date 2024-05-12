# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:10:18 2024

@author: noodl
"""

#Question 1
message = "Hello World"
print(message)      #NameError - mesage is not defined

#Question 2
numStd = 1 + 4      #SyntaxError - cannot assign to this expression

#Question 3
name = input("Enter your Name:")
age = int(input("Enter your Age:"))
print(name, age)    #TypeError - cannot concatenate string and int

#Question 4
print(numStd)       #NameError - mesage is not defined

#Question 5
number = int(input("Enter a number:"))
print(number, "\0")     #ZeroDivisionError - division by zero

#Question 6
a = 10 
b = 15
sum = a - b
print(sum)

#Question 7
numBeans = 500;
numJars = 3;
totalBeans = numBeans * numJars; 
print(totalBeans, "total");     #SyntaxError: invalid syntax