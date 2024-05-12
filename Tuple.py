# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:49:24 2024

@author: noodl

def get_ends(String):
    return tuple of first and last letter of string parameter
"""

#Question 1
dict = {"Length" : 6, "Width" : 8, "Height" : 4}
tuple = (6, 8, 4)

print(dict["Length"])
print(tuple[0])

#Question 2
date = "10/31/2017"
var = date.split("/")
print(var[0] + "/" + var[1] + "/" + var[2])

#Question 3
def get_ends(word):
    return (word[0], word[-1])

print(get_ends("Python"))
