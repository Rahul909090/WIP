# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:44:14 2024

def createLabel(self, rowNum, colNum, labelText):
    creates label
    
def createNameEntry(self, rowNum, colNum):
    creates name textbox
    
def createPasswordEntry(self, rowNum, colNum):
    creates password textbox
    
def createContactEntry(self, rowNum, colNum):
    creates contact textbox
    
def createEmailEntry(self, rowNum, colNum):
    creates email textbox
    
def spinBox(self, rowNum, colNum, fromRange, toRange):
   creates spinbox for age count

def radioButton(self, rowNum, colNum, radioText, radioValue):
   creates radio buttons for gender selection

def dropDownList(self, rowNum, colNum, listOfCountries):
   creates dropdown list for country selection

def checkButton(self, rowNum, colNum, checkText, checkOffValue, checkOnValue):
    creates check button for programming language select

def createButton(self, rowNum, colNum, title, functionName):
   creates button to submit and clear data

def validateName(self, test):
   ensures name entry only letters

def validatePassword(self, test):
   ensures password entry contains a digit, lowercase letter, uppercase letter,
   and a special character. also ensures password entry is less than 32 but 
   more than 8 charactes long.

def validateContact(self, test):
    ensures contact number is all digits
    
def main():
    creates a RegistrationForm object that is used to create all widgets

@author: noodl
"""

import tkinter as tk

class RegistrationForm(tk.Tk):
   def __init__(self):
      super().__init__()
      self.config(bg='#87CEEB')
      self.geometry("400x600")
      self.title("Registration Form")
      self.grid_columnconfigure(0, weight=1)
      self.grid_rowconfigure(1, weight=0)
      
      #StringVar objects
      self.name = tk.StringVar()
      self.password = tk.StringVar()
      self.contact = tk.StringVar()
      self.email = tk.StringVar()
      self.country = tk.StringVar(self)
      self.country.set('Select a country')
      self.checkbox = tk.StringVar()
      
      headLabel = tk.Label(self, text = "Registration Form", bg="white", font=("Arial", 15))
      headLabel.grid(row = 0, column= 1)
      #headLabel.place(relx=.5, rely=0.1, anchor="center")
   
   def createLabel(self, rowNum, colNum, labelText):
      label = tk.Label(self, text = labelText, bg="yellow")
      label.grid(column = colNum, row = rowNum, sticky = 'w', padx=10, pady=10)
   
   def createNameEntry(self, rowNum, colNum):
      entry_value = tk.Entry(self)
      entry_value.grid(row = rowNum, column = colNum, padx=10, pady=10)
   
   def createPasswordEntry(self, rowNum, colNum):
      entry_value = tk.Entry(self)
      entry_value.grid(row = rowNum, column = colNum)
     
   def createContactEntry(self, rowNum, colNum):
      entry_value = tk.Entry(self)
      entry_value.grid(row = rowNum, column = colNum)
   
   def createEmailEntry(self, rowNum, colNum):
      entry_value = tk.Entry(self)
      entry_value.grid(row = rowNum, column = colNum)
   
   def spinBox(self, rowNum, colNum, fromRange, toRange):
      spinbox = tk.Spinbox(self, from_= fromRange, to = toRange)
      spinbox.grid(row = rowNum, column = colNum)
   
   def radioButton(self, rowNum, colNum, radioText, radioValue):
      radio = tk.Radiobutton(text = radioText, value = radioValue, variable = self.checkbox)
      radio.grid(row = rowNum, column = colNum)
   
   def dropDownList(self, rowNum, colNum, listOfCountries):
      dropdown = tk.OptionMenu(self, self.country, *listOfCountries)
      dropdown.grid(row = rowNum, column = colNum)
   
   def checkButton(self, rowNum, colNum, checkText, checkOffValue, checkOnValue):
       
      button = tk.Checkbutton(self, text = checkText, onvalue = checkOnValue, offvalue = checkOffValue, variable = self.checkbox)
      button.grid(row = rowNum, column = colNum)
   
   def createButton(self, rowNum, colNum, title, functionName):
      button = tk.Button(self, text = title, command = functionName)
      button.grid(row = rowNum, column = colNum)
   
   def validateName(self, test):
      return test.replace(' ', '').isalpha()
   
   def validatePassword(self, test):
      if len(test) < 8 or len(test) > 32:
          return False
      
      hasDigit = False
      hasLower = False
      hasUpper = False
      hasSpecial = False
      
      for char in test:
          if char.isdigit():
              hasDigit = True
          elif char.isLower():
              hasLower = True
          elif char.isUpper():
              hasUpper = True
          elif char in "!@#$%^&*()_-+={};:,<.>":
              hasSpecial = True
        
      return hasDigit and hasLower and hasUpper and hasSpecial
   
   def validateContact(self, test):
      return test.isdigit()

def main():
    app = RegistrationForm()
    
    app.createLabel(3, 0, 'Your Name')
    app.createNameEntry(3, 1)
    
    #password
    app.createLabel(4, 0, 'Password')
    app.createPasswordEntry(4, 1)
    
    #contact
    app.createLabel(5, 0, 'Contact')
    app.createContactEntry(5, 1)
    
    #email
    app.createLabel(6, 0, 'Email')
    app.createEmailEntry(6, 1)
    
    #age
    app.createLabel(7, 0, 'Your Age')
    app.spinBox(7, 1, 1, 70)
    
    #gender
    app.createLabel(8, 0, 'Gender')
    app.radioButton(8, 1, 'Male', 'Male')
    app.radioButton(8, 2, 'Female', 'Female')
    
    #country
    listOfCountries = ['Belize', 'Armenia', 'India', 'America', 'Italy' , 'England']
    app.createLabel(9, 0, 'Your Country')
    app.dropDownList(9, 1, listOfCountries)
    
    #programming
    app.createLabel(10, 0, 'Programming')
    app.checkButton(10, 1, 'Java', 1, 0)
    app.checkButton(10, 2, 'Python', 1, 0)
    app.checkButton(10, 3, 'C', 1, 0)
    
    #button
    app.createButton(11, 1, 'Clear Data', 'ClearFunctionName')
    app.createButton(11, 2, 'Submit', 'ClearFunctionName')
    
    app.mainloop()

if __name__ == "__main__":
    main()