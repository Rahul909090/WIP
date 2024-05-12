# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:58:34 2024

@author: noodl

def sum_dictionary(dict):
    returns a dictionary of numbers representing the sum of the elements in the lists in dict.
    
def extract_key(key, dict):
    returns a list of just the values associated with that key.
    
"""

#Question 1
course = {
    "Instructors": ["Klaus", "Wrex"],
    "ID": {
        "Department": "CS",
        "Number": 1064
    },
    "Name": "Introduction to Python",
    "Assignments": {
        "Day 1": {
            "Points": 10,
            "Title": "Introduction"
        },
        "Day 2":{
            "Points": 5,
            "Title": "Installing Python"
        },
    }
}

print(course["Instructors"][0])
print(course["Assignments"]["Day 2"]["Title"])


#Question 2
movies = [
    {"Name": "Beauty and the Beast", "Run Time": 92, "IMDB": .8}, 
    {"Name": "Hercules", "Run Time": 93, "IMDB": .72},
    {"Name": "Up", "Run Time": 96, "IMDB": .83}
    ]

for x in movies:
    print(x["Name"])

#Question 3
games = [
    {"Name": "UD", "Score": 27, "Away?": False},
    {"Name": "Clemson", "Score": 14, "Away?": True},
    {"Name": "Pitt", "Score": 32, "Away?": True},
]
total = 0
for x in games:
    total = total + x["Score"]

print(total)

#Question 4
forecast = [
    {"Day": "Friday", "Location": "Blacksburg",
     "Weather": {"Rainfall": 2, "Temperature": 60, "Windy?": False}},
    {"Day": "Saturday", "Location": "Blacksburg",
     "Weather": {"Rainfall": 4, "Temperature": 65, "Windy?": True}},
    {"Day": "Sunday", "Location": "Blacksburg",
     "Weather": {"Rainfall": 1, "Temperature": 72, "Windy?": True}},
]
totalRain = 0
for x in forecast:
    if x["Weather"]["Windy?"]:
        totalRain = totalRain + x["Weather"]["Rainfall"]

print(totalRain)

#Question 5
hourly_donations_per_day = [
    [44, 33, 56, 27, 33, 25],
    [12, 15, 22, 19, 21],
    [36, 34, 32, 37, 28, 11, 35],
    [20, 19, 29],
    [22, 27, 21, 15, 26, 15]
    ]
totalDonations = 0
for x in hourly_donations_per_day:
    for y in x:
        totalDonations = totalDonations + y
    
print(totalDonations)

#Question 6
def sum_dictionary(dict):
    temp = {}
    i = 1
    while i <= len(dict):
        tot = 0
        for x in dict["Module " + str(i)]:
            tot = tot + x
        temp["Module " + str(i)] = tot
        i = i + 1
    return temp

print(sum_dictionary( { "Module 1": [10, 5, 3, 5], "Module 2": [7, 3, 4, 5, 3], "Module 3": [10, 12, 4, 3, 2]}))

#Question 7
def extract_key(key, dict):
    temp = []
    for x in dict:
        temp.append(x[key])
    return temp

print(extract_key("Height", [ {"Name": "Klaus", "Weight": 27, "Height": 18}, {"Name": "Pumpkin", "Weight": 20, "Height": 16}, {"Name": "Wrex", "Weight": 3, "Height": 2}]))