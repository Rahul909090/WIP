# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:25:54 2024

@author: noodl

def highwayNumberInfo(highway num):
    returns whether highway is primary or auxilary and its direction of travel
    
def Num2Binary(decimal number):
    returns the decimal number in binary format
    
def CharCount(char, string):
    returns the total number of times the character is in the string
    
def wordFrequency(listOfWords):
    returns the frequency of each word in the list
    
def lessThanFifty(listOfInt):
    returns a list containing the integers less than or equal to 50 from the given list
    
def coinFlip(num):
    returns "Heads" if num is equal to 1 or "Tails" if num is equal to 0
    
def Statistics(x, y, z):
    returns a tuple of x to the power of z, x to the power of (y to the power of z), the absolute value of y, and the square root of (xy to the power of z).
    
def calCalories():
    returns the total calories calculated based on the input of age, weight, heartrate and time (Uses the given calories function).
    
def calChange(changeAmount):
    returns the change  as string using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies
    
def inList(listOfWords, char):
    returns a list comprehension with words having the passed character
"""

#Question 1
def highwayNumberInfo(num):
    direction = ""
    hwType = ""
    if (num % 2) == 0:
        direction = "east/west"
    else:
        direction = "north/south"
    if num < 100 and num > 0:
        hwType = "primary"
        return ("I-" + str(num) + " is " + hwType + ", going " + direction + ".")
    elif num > 99 and num < 1000:
        hwType = "auxiliary"
        if((abs(num) % 100) == 00):
            return ("Not an " + hwType + ", going " + direction + ".")
        else:
            return ("I-" + str(num) + " is " + hwType + ", serving I-" + str(abs(num) % 100) + ", going " + direction + ".")

print(highwayNumberInfo(295))

#Question 2
def Num2Binary(num):
    if num == 0:
        return 0
    else:
        binary = ""
        while num > 0:
            binary = binary + str(num % 2)
            num = int(num / 2)
        return binary[::-1]

print(Num2Binary(8))

#Question 3
def CharCount(char, string):
    count = 0
    for x in string:
        if char == x.lower():
            count = count + 1
    return count

print(CharCount('n', "It's a sunny day"))

#Question 4
def wordFrequency(listOfWords):
    dict = {}
    for x in listOfWords:
        if x in dict:
            dict[x] = dict[x] + 1
        else:
            dict[x] = 1 
    return dict

print(wordFrequency(["hey","hi","Mark","hi","mark"]))

#Question 5
def lessThanFifty(intList):
    subFifty = []
    for x in intList:
        if x <= 50:
            subFifty.append(x)
    return subFifty

print(lessThanFifty([10,20,30,40,50,60,70]))

#Question 6
def coinFlip(num):
    if num == 1:
        return "Heads"
    elif num == 0:
        return "Tails"
    else:
        return "Invalid Input"
    
for x in [0,1,1,0,1,0,0]:
    print(coinFlip(x))

#Question 7
def Statistics(x, y, z):
    stats = (pow(x, z), pow(x, pow(y, z)), abs(y), (pow(x * y, z))**0.5)
    return stats

print(Statistics(10, 2, 3))

#Question 8
def calCalories():
    age = float(input("Enter your age: "))
    weight = float(input("Enter your weight: "))
    heartRate = float(input("Enter your heart rate: "))
    time = float(input("Enter your time: "))
    
    return ((age * 0.2757 + weight * 0.03295 + heartRate * 1.0781 - 75.4991) * time) / 8.368

#print(calCalories())

#Question 9
def calChange(changeAmount):
    dollars = changeAmount // 100
    quarters = (changeAmount % 100) // 25
    dimes = ((changeAmount % 100) % 25) // 10
    nickels = (((changeAmount % 100) % 25) % 10) // 5
    pennies = (((changeAmount % 100) % 25) % 10) % 5
    
    result = []
    if dollars == 1:
        result.append(str(dollars) + " Dollar")
    else:
        result.append(str(dollars) + " Dollars")
    if quarters == 1:
        result.append(str(quarters) + " Quarter")
    else:
        result.append(str(quarters) + " Quarters")
    if dimes == 1:
        result.append(str(dimes) + " Dime")
    else:
        result.append(str(dimes) + " Dimes")
    if nickels == 1:
        result.append(str(nickels) + " Nickel")
    else:
        result.append(str(nickels) + " Nickels")
    if pennies == 1:
        result.append(str(pennies) + " Penny")
    else:
        result.append(str(pennies) + " Pennies")
    for x in result[:]:
        if '0' in x:
            result.remove(x)
    return ' '.join(result)

print(calChange(45))

#Question 10
def inList(words, char):
    result = []
    for x in words:
        if char in x:
            result.append(x)
    return result

print(inList(["hello", "zoo", "sleep", "drizzle"], 'z'))