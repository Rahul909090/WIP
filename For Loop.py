# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:05:51 2024

@author: noodl
"""

#Question 1
names = ["Harry", "Hermione", "Ron"]
for x in names:
    print(x)
    
#Question 2
temperatures = [10, 20, 5]
for x in temperatures:
    print(x * (9/5) + 32)
    
#Question 3
def convert_fahrenheit(temp):
    return temp * (9/5) + 32

temp = [10.0, 20.0, 30.0]
for x in temp:
    print(convert_fahrenheit(x))