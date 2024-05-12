# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 13:32:45 2024

@author: noodl
"""

values=[1,2,3]
#Question 1
x = int(input("Enter a number: "))
sum = 0
while x != -999:
    sum = sum + x
    x = int(input("Enter a number: "))

print(sum)

#Question 2
i = 2
while i <= 10:
    print(i)
    if(i == 10):
        print("Goodbye!")
    i = i + 2

#Question 3
i = 10
while i >= 2:
    print(i)
    i = i - 2

