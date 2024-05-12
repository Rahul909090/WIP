# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 23:34:00 2024

@author: noodl
"""

#Question 1
def sumValues():
    values = input("Enter the numbers: ").split(",")
    sum = 0
    for x in values:
        sum = sum + int(x)
    return sum


#Question 2
def all_cats(animals):
    words = animals.split(",")
    for x in words:
        if "cat" not in x:
            return False    
    return True

print(all_cats("cat,catfish"))

#Question 3
def add_hot_cold(temp):
    hot = 0
    cold = 0
    for x in temp:
        if x == 'H':
            hot = hot + 1
        elif x == 'C':
            cold = cold + 1
    return hot - cold

print(add_hot_cold("CHCC"))