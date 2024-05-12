# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:23:30 2024

@author: noodl
"""
import re

#Question 1
phrase = "cat dog mouse"
match = re.search("dog", phrase)
print(phrase[match.start():match.end()])

#Question 2
clientName = "Dan Danielson is stupid"
match = re.search("is stupid", clientName)
print(clientName[0:match.start() - 1])

#Question 3
print("www.facebook.com"[4:12])

#Question 4
a_phrase = "order out of"
print(a_phrase[6:9] + a_phrase[9:12] + a_phrase[5] + a_phrase[0:5])

#Question 5
userInput = input("Enter text: ")
print("dog" in userInput)