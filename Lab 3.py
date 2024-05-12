# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:12:44 2024

def printContent():
    prints all count variables created in the constructor
    
def analyze():
    calculates the count of words, capital words, lines and sentences
    
def getPopulationDensity():
    returns the population density, number of people per square kilometer of area
    
def getUrbanRation():
    returns the urban ratio, urban population over total population (urban calculated using rural - total population)
    
def getPopulationChange():
    returns population change, birthrate minus deathrate
    
def getMobileRatio():
    returns the number of mobile phone subscriptions to the total population


@author: Rahul
"""
import csv

#Question 1
class TextAnalyzer:
    def __init__(self):
        self.fileName = input("Enter the file name: ")
        self.lineCount = 0
        self.wordCount = 0
        self.largeWordCount = 0
        self.sentenceCount = 0
        self.capitalizedWordCount = 0
        
    #Setters
    def setName(self, name):
        self.fileName = name
    def setLine(self, line):
        self.lineCount = line
    def setWord(self, word):
        self.wordCount = word
    def setLargeWord(self, largeWord):
        self.largeWordCount = largeWord
    def setSentence(self, sentence):
        self.sentenceCount = sentence
    def setCapitalized(self, cap):
        self.capitalizedWordCount = cap
    
    #Getters
    def getName(self):
        return self.fileName
    def getLine(self):
        return self.lineCount
    def getWord(self):
        return self.wordCount
    def getLargeWord(self):
        return self.largeWordCount
    def getSentence(self):
        return self.sentenceCount
    def getCapitalized(self):
        return self.capitalizedWordCount
    
    #Print contents
    def printContent(self):
        print(f"Number of Lines: {self.lineCount} \nNumber of words: {self.wordCount} \nNumber of long words: {self.largeWordCount} \nNumber of sentences: {self.sentenceCount} \nNumber of capitalized words: {self.capitalizedWordCount}\n")
    
    #Analyze text function
    def analyze(self):
        file = open(self.getName(), "r")
        for x in file:
            self.lineCount = self.lineCount + 1
            
            temp = x.split()
            self.wordCount = self.wordCount + len(temp)
            
            for y in temp:
                if len(y) > 5:
                    self.largeWordCount = self.largeWordCount + 1
                if '.' in y:
                    self.sentenceCount = self.sentenceCount + 1
                if y[0].isupper():
                    self.capitalizedWordCount = self.capitalizedWordCount + 1
        file.close()
    
#Question 2
class Country():
    def __init__(self, name, area, population, birthRate, deathRate, fertilityRate, ruralPopulation, telephoneLines, mobilePhoneSub):
        self.countryName = name
        self.surfaceArea = area
        self.totalPopulation = population
        self.birthRate = birthRate
        self.deathRate = deathRate
        self.fertilityRate = fertilityRate
        self.ruralPopulation = ruralPopulation
        self.telephoneLines = telephoneLines
        self.mobilePhoneSubscriptions = mobilePhoneSub
    
    def __str__(self):
        return f"{self.countryName} (Population: {self.totalPopulation})"
    
    #Getters
    def getFertilityRate(self):
        return self.fertilityRate
    def getTelephoneLines(self):
        return self.telephoneLines
    
    #Returns population density
    def getPopulationDensity(self):
        return self.totalPopulation / self.surfaceArea
    
    #Returns Urban Ration
    def getUrbanRatio(self):
        return (self.totalPopulation - self.ruralPopulation) / self.totalPopulation
    
    #Returns population change
    def getPopulationChange(self):
        return self.birthRate - self.deathRate
    
    #Returns mobile phone subscription ratio
    def getMobileRatio(self):
        return self.mobilePhoneSubscriptions / self.totalPopulation

class CountryAnalyzer():
    def analyze(self):
        fileName = input("Enter the country file name: ")
        countryList = []
        countryName = ""
        minPhone = 100
        
        with open(fileName, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            
            for row in csvreader:
                countryList.append(Country(row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8])))
        
        for x in countryList:
            print(x)
            print("        Population Density:", round(x.getPopulationDensity(), 1))
            print("        Percent Urban:", str(round(x.getUrbanRatio() * 100, 1)) + '%')
            
            if x.getPopulationChange() < 0:
                print("        POPULATION DECLINE")
            if x.getMobileRatio() * 100 < minPhone:
                minPhone = x.getMobileRatio() * 100
                countryName = f"{x.countryName} (Population: {x.totalPopulation})"
        
        print("Country with the lowest mobile phone ratio: ")
        print(countryName)
        print("Mobile phone percentage:", str(round(minPhone, 1)) + '%')

def main():
    '''#Question 1
    text1 = TextAnalyzer()
    text1.analyze()
    text1.printContent()'''
    
    #Question 2
    countries = CountryAnalyzer()
    countries.analyze()

if __name__ == "__main__":
    main()