# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 23:23:05 2024

@author: noodl
"""

#Question 1
def make_list(one, two, three):
    return [one, two, three]

#Question 2
def is_weekend(daysOfWeek):
    for x in daysOfWeek:
        if x == "Saturday" or x == "Sunday":
            return True
        else:
            continue
    return False
        
#Question 3
def bookend_list(listOfValues):
    return [listOfValues[0], listOfValues[len(listOfValues) - 1]]

#Question 4
def check_length(listOfValues):
    length = len(listOfValues)
    if length >= 3 and length <= 5:
        return True
    else:
        return False
    
#Question 5
def zooList(an_animal):
    animals = ["dog", "cat", "capybara", "danger noodle"]
    for x in animals:
        if x == an_animal:
            return True
        else:
            continue
    return False
