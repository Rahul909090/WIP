# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 18:49:29 2024

@author: noodl
"""
import math

#Number 1
def is_morning(currentHour):
    return currentHour > 5 and currentHour < 12

#Number 2
def calculate_volume(radius, height):
    return float("{:.2f}".format(math.pi * (radius ** 2) * height))
    
#Number 3
def get_half(inputString):
    halfString = inputString[:len(inputString)//2] 
    return halfString

#Number 4
def to_pig_latin(word):
    pigLatinWord = word[1:] + word[0] + "ay"
    return pigLatinWord

#Number 5
def calculate_distance(x1, y1, x2, y2):
    distance = float("{:.2f}".format(((y2-y1) ** 2 + (x2-x1) ** 2) ** 0.5))
    return distance

#Number 6
def hide_letter(word):
    wordWithHiddenLetter = "?" + word[1:]
    return wordWithHiddenLetter

