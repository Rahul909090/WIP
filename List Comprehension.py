# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 23:47:41 2024

@author: noodl
"""

#Question 1
def make_exclamations(listOfStrings):
    stringsList = []
    for x in listOfStrings:
        stringsList.append(x + "!")
    return stringsList

print(make_exclamations(["harry potter","fight club","home alone"]))

#Question 2
original_prices = [50, 100, 200]
half_off_prices = []

for x in original_prices:
    half_off_prices.append(x / 2)

print(half_off_prices)

#Question 3
original_price = [50, 100, 200]
low_prices = []
count = 0

for x in original_price:
    if x > 100:
        original_price.pop(count)
    else:
        low_prices.append(x)
    count = count + 1
print(low_prices)

#Question 4
names =  [" Doctor Bark  ", " Virginia Woof ", "Jabba the Mutt     "]
empty = []
for x in names:
    empty.append(x.strip())

print(empty)