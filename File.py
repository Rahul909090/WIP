# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 20:39:31 2024

@author: noodl

def calculate_file_size(name of file):
    opens files and returns the number of characters in the file
"""

#Question 1
path = "grocery-list.txt"
file = open(path)

for line in file:
    print(line.strip())
    
file.close()

#Question 2
path = "pressure.txt"
file = open(path)
sum = 0

for line in file:
    listNum = line.split("	")
    for x in listNum:
        sum = sum + float(x)
    
print(sum)
file.close()

#Question 3
def calculate_file_size(path):
    sumFile = open(path)
    sumTwo = 0
    for x in sumFile:
        sumTwo = sumTwo + len(x)
    sumFile.close()
    return sumTwo

print(calculate_file_size("random.txt"))