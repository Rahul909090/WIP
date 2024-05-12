# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:26:43 2024
def countDracula(url):
    returns the number of times 'dracula' is found in the requested web file
    
def getJacksonvilleTemp(url):
    returns a list of temperatures in Jacksonville by requesting the JSON file from a web server.
@author: noodl
"""
import requests

#Question 1
header = requests.get("https://pastebin.com/raw/V7tWn1Rj")
info = header.text
print(info)

#Question 2
def countDracula(url):
    response = requests.get(url)
    data = response.text
    count = data.lower().count("dracula")
    return count

print(countDracula("http://www.gutenberg.org/cache/epub/345/pg345.txt"))

#Question 3
def getJacksonvilleTemp(url):
    response = requests.get(url)
    data = response.json()
    return data["data"]["temperature"]
    
print(getJacksonvilleTemp("https://forecast.weather.gov/MapClick.php?lat=30.3322&lon=-81.6557&unit=0&lg=english&FcstType=json"))