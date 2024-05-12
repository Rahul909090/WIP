# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:38:56 2024

@author: noodl
"""

#Question 1
filename = "01-All-The-Single-Ladies.mp3"
print(filename.replace("-", " "))

#Question 2
creek_rainfall = "High, High, Low, Low, High, High, Low"
print("The number of occurrences of High is", creek_rainfall.count("High"))
print("The number of occurrences of Low is", creek_rainfall.count("Low"))

#Question 3
book = "  the-count-of-monte-cristo  "
book = book.strip()
book = book.replace("-", " ")
book = book.title()
print(book)

#Question 4
message = "Why are you shouting?"
print(message.upper())