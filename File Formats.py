# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 20:56:00 2024

@author: noodl
"""
import json

#Question 1
json_file = open('customers.json')
data = json.load(json_file)

for x in data:
    print(x["company"] + "    ----    " + x["country"])
json_file.close()
#Question 2
file = open('states.json')
dataTwo = json.load(file)

print(dataTwo["FL"])
file.close()
#Question 3
total = 0
file = open('employees.json')
dataThree = json.load(file)

for x in dataThree:
    total = total + x["salary"]

print(total)
file.close()