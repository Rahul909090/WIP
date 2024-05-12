# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:05:24 2024

def starts_with_letter(word):
    returns a boolean value stating if the first index of word is a letter or not
    
@author: noodl
"""

#Question 1
from math import pi
print(pi)

#Question 2
from string import ascii_letters
def starts_with_letter(word):
    letters = ascii_letters
    return word[0] in letters

print(starts_with_letter("word"))

#Question 3
from random import choice
dinnerSpots = ["KFC", "Taco Bell", "PDQ", "Millers"]
print(choice(dinnerSpots))

#Question 4
from pprint import pprint
data = {
    'Name': 'John Doe',
    'Age': 30,
    'Address': {
        'Street': '123 Main St',
        'City': 'Anytown',
        'State': 'CA',
        'Zip': '12345'
    },
    'Interests': ['Reading', 'Traveling', 'Coding'],
    'Friends': [
        {'Name': 'Jane Smith', 'Age': 28},
        {'Name': 'Tom Brown', 'Age': 32},
        {'Name': 'Emily Johnson', 'Age': 31}
    ]
}
pprint(data)

#Question 5
import simple_math as sm
print(sm.addition(1, 2))
print(sm.subtraction(2, 1))
print(sm.multiplication(3, 3))
print(sm.division(9, 2))
