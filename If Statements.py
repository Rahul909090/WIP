# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 21:50:58 2024

@author: noodl

ghjprg
"""

#Question 1
def can_drink(age, has_license):
    if age > 21:
        if age < 1000:
            if has_license == True:
                return "Can Drink"
            else:
                return "Doesn't have a license"
        else:
            return "Too old"
    else:
        "Too young"

#Question 2
def postiveStatistics(num1, num2, num3):
    if num1 < 0 or num2 < 0 or num3 < 0:
        print("Invalid Number")
    else:
        average = (num1 + num2 + num3) / 3
        max = 0
        min = 0
        
        if num1 > num2 and num1 > num3:
            max = num1
        elif num2 > num1 and num2 > num3:
            max = num2
        elif num3 > num1 and num3 > num2:
            max = num3
        
        if num1 < num2 and num1 < num3:
             min = num1
        elif num2 < num1 and num2 < num3:
             min = num2
        elif num3 < num1 and num3 < num2:
             min = num3
             
        print("Average =", average , ", min =" , min , ", max =" , max)
        
#Question 3
def incomeTax(income):
    if income < 0:
        return float(0)
    
    if income < 20000:
        return float(0.1 * income)
    elif income > 20000 and income < 50000:
        return float(0.2 * income)
    elif income > 50000 and income < 100000:
        return float(0.3 * income)
    elif income > 100000:
        return 0.4 * income
    
#Question 4
def is_leap(year):
    temp = int((year - 1) // 100 + 1) * 100
    print(temp)
    if year % 4 == 0 or temp * 400 == 0:
        return True
    else: 
        return False

#Question 5
def loginName(firstName, lastName, year):
    if len(firstName) < 6:
        return firstName + lastName[0] + "_" + str(int(year % 10))
    else:
        return firstName[:6] + lastName[0] + "_" + str(int(year % 10))

print(loginName("Nicolas", "North", 2024))