# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:11:57 2024

@author: noodl
"""

#Question 1
sum = 0
pages_count_list = [223, 251, 317, 636]
for x in pages_count_list:
    sum = sum + x
    
print("Total pages:", sum)

#Question 2
def treatmentCount(listOfBooleans):
    count = 0
    for x in listOfBooleans:
        if x == True:
            count = count + 1
    
    return count

print(treatmentCount([True, False,False,True,False,False,False,True ]))

#Question 3
def hasHarry(listOfStrings):
    for x in listOfStrings:
        return "harry potter" in x
    
print(hasHarry(["harry potter","fight club","home alone"]))

#Question 4
def average(listOfInts):
    sum = 0
    count = 0
    for x in listOfInts:
        sum = sum + x
        count = count + 1
        
    return float(sum / count)

print(average([10, 7, 10]))

#Question 5
def maximum_odd(listOfInts):
    max = 0
    for x in listOfInts:
        if x % 2 != 0:
            if x > max:
                max = x
    
    return max

print(maximum_odd([10, 7, 2,4,16,17,27]))